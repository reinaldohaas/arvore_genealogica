#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator Genealógico do Gmail — Famílias Haas, Meier, Voit, Doerner, Preiss, Michels, Funke & Hoeveler
Autor: Prof. Dr. Reinaldo Haas (reinaldohaas@gmail.com)
Repositório: C:\\Users\\haas\\github\\arvore_genealogica

Busca automaticamente no Gmail todas as contribuições genealógicas enviadas por:
  - agenorhaas@hotmail.com (Agenor Haas)
  - Outros familiares, pesquisadores e cartórios/arquivos (Brasil e Alemanha)

Autenticação segura (sem expor senhas no código ou no Git):
  Lê GMAIL_APP_PASSWORD (Senha de App de 16 caracteres do Google) diretamente de ~/.env
  (C:\\Users\\haas\\.env) via protocolo seguro IMAP SSL (imap.gmail.com:993).
"""

import argparse
import datetime
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime
import hashlib
import html
import imaplib
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(r"C:\Users\haas\github\arvore_genealogica")
DOCS_DIR = REPO_ROOT / "docs"
DADOS_DIR = REPO_ROOT / "dados"
ANEXOS_DIR = REPO_ROOT / "anexos_gmail"

DEFAULT_EMAIL = "reinaldohaas@gmail.com"
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993

# Consultas X-GM-RAW (sintaxe nativa da busca do Gmail via IMAP!)
GMAIL_QUERIES = [
    ("Agenor Haas (agenorhaas@hotmail.com)", "agenorhaas@hotmail.com OR \"Agenor Haas\" OR agenorhaas"),
    ("Arquivos da Baviera (Leonberg, Maxhütte-Haidhof, Moosbach, Heumaden)", "Maxhütte OR Haidhof OR Heumaden OR Moosbach OR Burgtreswitz OR Sandberg OR \"Johann Haas\" OR \"Maria Meier\" OR \"Maria Meyer\""),
    ("História e Família Haas (Vapor Formosa, Ituporanga, Anitápolis, Aurora)", "\"Vapor Formosa\" OR \"navio Formosa\" OR \"Marise Haas\" OR \"Baldoíno Haas\" OR \"Baldoino Haas\" OR \"árvore genealógica\" OR genealogia OR \"familia haas\" OR \"família haas\""),
    ("Ramo Doerner, Preiss, Michels & Arend (Solingen, São Martinho, Vidal Ramos)", "Doerner OR Dörner OR \"Adelina Doerner\" OR \"Fernando Doerner\" OR \"Gertrudes Preiss\" OR \"Gertrudes Preuss\" OR Solingen OR \"São Pedro de Alcântara\""),
    ("Ramo Funke & Hoeveler (Bárbara Funke Haas)", "Hoeveler OR \"Erno Hoeveler\" OR \"Oma Rosita\" OR \"Carlos Heinz Funke\" OR \"Ilusca\" OR (Funke genealogia) OR (Funke bisavô) OR (Funke Alemanha)"),
]

# Termos acadêmicos/administrativos para filtrar falsos positivos quando a busca for ampla
NOISE_SUBJECT_PATTERNS = [
    r"\[FSC\d+",
    r"Moodle",
    r"Prova \d",
    r"Gabarito",
    r"Boletim UFSC",
    r"Fala\.BR",
    r"SeTIC",
]

ALLOWED_ATTACHMENT_EXTS = {
    ".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt",
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".jfif",
    ".ged", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".zip",
}


def load_env_file(env_path: Path) -> dict:
    """Lê variáveis de ~/.env com suporte a BOM UTF-8 sem imprimir segredos."""
    env_vars = {}
    if env_path.exists():
        content = env_path.read_text(encoding="utf-8-sig", errors="ignore")
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            env_vars[k] = v
    return env_vars


def decode_mime_str(value: str) -> str:
    if not value:
        return ""
    parts = decode_header(value)
    decoded = []
    for content, charset in parts:
        if isinstance(content, bytes):
            enc = charset or "utf-8"
            try:
                decoded.append(content.decode(enc, errors="replace"))
            except LookupError:
                decoded.append(content.decode("utf-8", errors="replace"))
        else:
            decoded.append(str(content))
    return "".join(decoded).strip()


def html_to_text(raw_html: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", raw_html)
    text = re.sub(r"(?i)<br\s*/?>", "\n", text)
    text = re.sub(r"(?i)</p\s*>", "\n\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in text.splitlines()]
    cleaned = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    return name.strip(" ._")[:140] or "anexo"


def select_all_mail_folder(imap: imaplib.IMAP4_SSL) -> str:
    """Seleciona '[Gmail]/Todos os e-mails' ou '[Gmail]/All Mail' ou 'INBOX'."""
    status, folders = imap.list()
    all_mail_name = None
    if status == "OK" and folders:
        for f in folders:
            raw = f.decode("utf-8", errors="ignore")
            # Procura atributo \All (padrão RFC 6154 do Gmail para Todos os E-mails)
            if "\\All" in raw:
                m = re.search(r'"([^"]+)"\s*$', raw)
                if m:
                    all_mail_name = m.group(1)
                    break
    for candidate in [all_mail_name, "[Gmail]/Todos os e-mails", "[Gmail]/All Mail", "INBOX"]:
        if not candidate:
            continue
        try:
            st, _ = imap.select(f'"{candidate}"', readonly=True)
            if st == "OK":
                return candidate
        except Exception:
            continue
    imap.select("INBOX", readonly=True)
    return "INBOX"


def extract_message_content(msg: email.message.Message, msg_uid: str, save_attachments: bool = True):
    plain_parts = []
    html_parts = []
    saved_attachments = []

    for part in msg.walk():
        if part.is_multipart():
            continue
        ctype = (part.get_content_type() or "").lower()
        cdisp = str(part.get("Content-Disposition") or "")
        raw_filename = part.get_filename()
        filename = decode_mime_str(raw_filename) if raw_filename else ""

        is_attachment = "attachment" in cdisp.lower() or bool(filename)
        if is_attachment and filename:
            ext = os.path.splitext(filename)[1].lower()
            payload = part.get_payload(decode=True)
            if payload and ext in ALLOWED_ATTACHMENT_EXTS:
                # Ignorar ícones minúsculos de assinatura (< 5 KB) em imagens
                if ext in {".png", ".jpg", ".jpeg", ".gif"} and len(payload) < 5120:
                    continue
                if save_attachments:
                    ANEXOS_DIR.mkdir(parents=True, exist_ok=True)
                    digest = hashlib.sha1(payload).hexdigest()[:8]
                    safe_fn = sanitize_filename(f"{msg_uid}_{digest}_{filename}")
                    out_path = ANEXOS_DIR / safe_fn
                    if not out_path.exists():
                        out_path.write_bytes(payload)
                    saved_attachments.append({
                        "original_name": filename,
                        "saved_name": safe_fn,
                        "size_bytes": len(payload),
                    })
            continue

        payload = part.get_payload(decode=True)
        if not payload:
            continue
        charset = part.get_content_charset() or "utf-8"
        try:
            text = payload.decode(charset, errors="replace")
        except LookupError:
            text = payload.decode("utf-8", errors="replace")

        if ctype == "text/plain":
            plain_parts.append(text.strip())
        elif ctype == "text/html":
            html_parts.append(html_to_text(text))

    body = "\n\n".join([p for p in plain_parts if p])
    if not body and html_parts:
        body = "\n\n".join([h for h in html_parts if h])
    return body.strip(), saved_attachments


def is_noise_email(subject: str, sender: str) -> bool:
    # Nunca filtrar nada de agenorhaas!
    if "agenorhaas" in sender.lower() or "agenor" in sender.lower():
        return False
    for pat in NOISE_SUBJECT_PATTERNS:
        if re.search(pat, subject, flags=re.IGNORECASE):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Importador de contribuições genealógicas do Gmail")
    parser.add_argument("--email", default=None, help=f"Conta do Gmail (default: {DEFAULT_EMAIL})")
    parser.add_argument("--max-per-query", type=int, default=80, help="Máximo de mensagens por consulta")
    parser.add_argument("--no-attachments", action="store_true", help="Não baixar anexos")
    args = parser.parse_args()

    env_vars = load_env_file(Path.home() / ".env")
    user_email = args.email or os.environ.get("GMAIL_USER") or env_vars.get("GMAIL_USER") or DEFAULT_EMAIL
    app_password = os.environ.get("GMAIL_APP_PASSWORD") or env_vars.get("GMAIL_APP_PASSWORD")

    if not app_password:
        print("ERRO: Variável GMAIL_APP_PASSWORD não encontrada em ~/.env (C:\\Users\\haas\\.env).", file=sys.stderr)
        print("Gere uma Senha de App em https://myaccount.google.com/apppasswords e salve em ~/.env.", file=sys.stderr)
        sys.exit(2)

    # Remove espaços caso a senha de app de 16 letras tenha sido copiada com espaços ("xxxx xxxx xxxx xxxx")
    app_password_clean = app_password.replace(" ", "").strip()

    print(f"[1/4] Conectando via IMAP SSL a {IMAP_HOST}:{IMAP_PORT} como {user_email}...")
    imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    try:
        imap.login(user_email, app_password_clean)
    except imaplib.IMAP4.error as e:
        print(f"FALHA de autenticação IMAP: {e}", file=sys.stderr)
        sys.exit(1)

    folder = select_all_mail_folder(imap)
    print(f"[2/4] Autenticado com sucesso! Pasta selecionada: {folder}")

    uid_to_categories = {}
    for label, gm_query in GMAIL_QUERIES:
        # Usa extensão oficial X-GM-RAW do Gmail para busca completa (remetente, corpo, anexos, acentos)
        escaped_q = gm_query.replace('\\', '\\\\').replace('"', '\\"')
        typ, data = imap.uid("SEARCH", "CHARSET", "UTF-8", f'X-GM-RAW "{escaped_q}"'.encode("utf-8"))
        if typ != "OK":
            # Fallback sem CHARSET UTF-8 (apenas ASCII)
            ascii_q = gm_query.encode("ascii", errors="ignore").decode("ascii").replace('"', '\\"')
            typ, data = imap.uid("SEARCH", None, f'X-GM-RAW "{ascii_q}"')
        uids = data[0].decode().split() if (typ == "OK" and data and data[0]) else []
        print(f"  • [{label}]: {len(uids)} mensagens encontradas")
        for uid in uids[-args.max_per_query:]:
            uid_to_categories.setdefault(uid, []).append(label)

    print(f"\n[3/4] Baixando e processando {len(uid_to_categories)} mensagens únicas...")
    records = []
    for uid in sorted(uid_to_categories.keys(), key=lambda x: int(x)):
        typ, msg_data = imap.uid("FETCH", uid, "(RFC822)")
        if typ != "OK" or not msg_data or not msg_data[0]:
            continue
        raw_bytes = msg_data[0][1]
        if not isinstance(raw_bytes, bytes):
            continue
        msg = email.message_from_bytes(raw_bytes)
        subject = decode_mime_str(msg.get("Subject", "(Sem assunto)"))
        sender = decode_mime_str(msg.get("From", ""))
        to_hdr = decode_mime_str(msg.get("To", ""))
        cc_hdr = decode_mime_str(msg.get("Cc", ""))
        date_raw = msg.get("Date", "")
        try:
            dt = parsedate_to_datetime(date_raw)
            date_iso = dt.strftime("%Y-%m-%d %H:%M")
        except Exception:
            date_iso = date_raw

        if is_noise_email(subject, sender):
            continue

        body, attachments = extract_message_content(
            msg, msg_uid=uid, save_attachments=not args.no_attachments
        )

        is_agenor = any(
            "agenorhaas" in h.lower() or "agenor haas" in h.lower()
            for h in (sender, to_hdr, cc_hdr, body[:2000])
        )

        records.append({
            "uid": uid,
            "date": date_iso,
            "from": sender,
            "to": to_hdr,
            "cc": cc_hdr,
            "subject": subject,
            "is_agenor": is_agenor,
            "categories": uid_to_categories[uid],
            "attachments": attachments,
            "body": body[:25000],
        })

    imap.logout()

    # Ordena cronologicamente, destacando primeiro Agenor Haas no relatório
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    DADOS_DIR.mkdir(parents=True, exist_ok=True)

    json_out = DADOS_DIR / "emails_genealogia.json"
    json_out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    agenor_recs = [r for r in records if r["is_agenor"]]
    other_recs = [r for r in records if not r["is_agenor"]]

    md_lines = [
        "# 📧 Contribuições Genealógicas Extraídas do Gmail",
        "",
        f"- **Conta pesquisada:** `{user_email}`",
        f"- **Data da extração:** {datetime.datetime.now():%d/%m/%Y %H:%M}",
        f"- **Total de mensagens genealógicas relevantes:** **{len(records)}**",
        f"  - Contribuições diretas / threads com **Agenor Haas (`agenorhaas@hotmail.com`)**: **{len(agenor_recs)}**",
        f"  - Contribuições de **outros familiares, arquivos e pesquisadores**: **{len(other_recs)}**",
        "",
        "---",
        "",
        "## 1. Contribuições de Agenor Haas (`agenorhaas@hotmail.com`)",
        "",
    ]

    if not agenor_recs:
        md_lines.append("_Nenhuma mensagem com `agenorhaas@hotmail.com` encontrada nos critérios atuais._\n")
    else:
        for idx, r in enumerate(agenor_recs, 1):
            md_lines.extend([
                f"### 1.{idx}. {r['subject']}",
                f"- **Data:** {r['date']}",
                f"- **De:** `{r['from']}`",
                f"- **Para:** `{r['to']}`" + (f" | **Cc:** `{r['cc']}`" if r["cc"] else ""),
            ])
            if r["attachments"]:
                att_str = ", ".join(
                    f"[`{a['original_name']}`](../anexos_gmail/{a['saved_name']}) ({a['size_bytes']//1024} KB)"
                    for a in r["attachments"]
                )
                md_lines.append(f"- **Anexos salvos:** {att_str}")
            md_lines.extend([
                "",
                "```text",
                r["body"][:8000] if r["body"] else "(Sem corpo de texto)",
                "```",
                "",
            ])

    md_lines.extend([
        "---",
        "",
        "## 2. Contribuições de Outros Familiares, Arquivos e Pesquisadores",
        "",
    ])

    for idx, r in enumerate(other_recs, 1):
        md_lines.extend([
            f"### 2.{idx}. {r['subject']}",
            f"- **Data:** {r['date']} | **Categorias:** {', '.join(r['categories'])}",
            f"- **De:** `{r['from']}`",
            f"- **Para:** `{r['to']}`",
        ])
        if r["attachments"]:
            att_str = ", ".join(
                f"[`{a['original_name']}`](../anexos_gmail/{a['saved_name']}) ({a['size_bytes']//1024} KB)"
                for a in r["attachments"]
            )
            md_lines.append(f"- **Anexos salvos:** {att_str}")
        md_lines.extend([
            "",
            "<details><summary>Ver conteúdo da mensagem</summary>",
            "",
            "```text",
            r["body"][:6000] if r["body"] else "(Sem corpo de texto)",
            "```",
            "",
            "</details>",
            "",
        ])

    md_out = DOCS_DIR / "contribuicoes_gmail.md"
    md_out.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"[4/4] Concluído!")
    print(f"  • Dossiê Markdown salvo em: {md_out}")
    print(f"  • Dados JSON salvos em:     {json_out}")
    print(f"  • Pasta de anexos:          {ANEXOS_DIR}")


if __name__ == "__main__":
    main()
