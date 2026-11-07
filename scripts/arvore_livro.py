"""Gera as árvores do livro (imagens/arvore_NN.png), o capítulo 22 e a lista de lacunas para pesquisa.

Fonte: GEDCOM privado do FamilySearch, corrigido pelos documentos citados no livro (CORRECOES).
Regras: até 7 gerações acima de Matheus e Lucas; quem não existe nos dados não ganha caixa;
o que falta é indicado no texto da caixa e listado em docs/prompt_antigravity_arvore.md.
Pessoas vivas aparecem só com o ano, ou sem data, e nunca entram na lista de lacunas.
"""
import collections
import re
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

RAIZ = Path(__file__).resolve().parents[1]
GED = RAIZ / "privado" / "arvore_consolidada_myheritage_2026-11-05b.ged"
IMG = RAIZ / "imagens"
CAP = RAIZ / "livro" / "capitulos" / "22_mapas_e_arvores.md"
LACUNAS = RAIZ / "docs" / "lacunas_arvore.md"
GER_MAX = 7

LINHA = re.compile(r"^(\d+) (?:(@[^@]+@) )?(\S+)(?: (.*))?$")
MES = dict(zip("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split(), range(1, 13)))
MES_IT = dict(zip("gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split(), range(1, 13)))

VIVOS = {"G5PB-VCC", "LYPQ-GW3", "G5PB-BSV", "G5P1-K26"}

# Correções vindas dos documentos e dos capítulos do livro (têm prioridade sobre o FamilySearch).
# b/d/arr = textos prontos; pl = lugar; nota = linha extra na caixa.
CORRECOES = {
    "LYPQ-GW3": {"nome": "Reinaldo Haas", "b": "1965", "pl": "Vidal Ramos"},
    "G5PB-BSV": {"nome": "Bárbara Funke", "b": "1972", "pl": ""},
    "G5P1-K26": {"nome": "Ilusca Leocádia Hoeveler", "b": "", "pl": "", "nota": "Joinville"},
    "G5P1-8FD": {"nome": "Dr. Carlos Heinz Funke"},
    "GX1B-HM1": {"nome": "Johann Haas, o Fata", "pl": "Leonberg, hoje Maxhütte-Haidhof", "arr": "Rio de Janeiro, 26/03/1913"},
    "PXN3-8ZG": {"nome": "Maria Meier, a Mota", "arr": "Rio de Janeiro, 26/03/1913"},
    # O batismo de Stoffen (1847) era de um homônimo: o casamento de Leonberg de 1878
    # (Leonberg_Bul012, p. 8, nº 4) dá como pais Michael Haas e Kunigunde Stadelmann.
    "GX1B-XK7": {"nome": "Josef Haas", "b": "", "pl": "", "d": "", "nota": "operário em Leonberg"},
    "GX1B-22C": {"nome": "Franziska Dengler", "d": ""},
    "GX1B-868": {"nome": "Georg Adam Meier", "b": "09/03/1859", "pl": "Heumaden", "d": ""},
    "GX1B-4GX": {"nome": "Franziska Voit", "b": "29/06/1861", "pl": "Burgtreswitz", "d": ""},
    "GDGT-8H8": {"nome": "Carlos Dörner", "b": "c. 1855", "pl": "Europa (Solingen?)"},
    "K84V-VR2": {"nome": "Anna Eller", "b": "c. 1858–1860", "pl": "Vestfália?", "d": "c. 1898", "dpl": "Imaruí"},
    "L1BB-NQ3": {"nome": "Fernando Dörner, o Opapa"},
    "L1BB-QH8": {"nome": "Gertrudes Preiss, a Omama", "d": "09/04/1970", "dpl": "Brusque"},
    "PSV9-B9Q": {"nome": "Guilherme Dörner", "nota": "Solingen? (tradição)"},
    "PSV9-6QS": {"nota": "Solingen? (tradição)"},
    "L58N-QCC": {"nome": "Bernard Preis"},
    "LV7G-Z2H": {"nome": "Ignazia Loch", "b": "c. 1828–1830", "pl": "São Pedro de Alcântara?", "d": "depois de 1872"},
    "L61J-RDG": {"nome": "Angela Catharina Arns"},
    "LD4Z-KTV": {"nome": "Nikolaus Arns"},
    "94JT-RHR": {"nome": "Johann Stephan Arns (Arens)"},
    "PXRP-LC7": {"nome": "Hulda (Funke)"},
    "29HB-C78": {"nome": "Frida Liechti"},
    "GYHT-22T": {"nome": "Peter (Liechti?)"},
    "GYHT-J8C": {"nome": "Carolina"},
    "PXPY-T29": {"nome": "Frida (Hoeveler)"},
    "G2MG-8VY": {"nome": "Rosita Érica Lohmann, a Oma Rosita", "d": "2014", "dpl": "Joinville"},
    "PXPT-X3Q": {"nome": "Dora Marta Aenishaenslin, a Oma Dora"},
    "KNYK-4J3": {"pl": "Estrela"},
    "27QQ-TM9": {"arr": "Rio de Janeiro, 05/12/1846"},
}
# Pessoas que estão nos documentos e faltam no GEDCOM: pai da chave -> (pai, mãe)
EXTRA_PAIS = {
    "GX1B-XK7": ({"id": "doc-michael-haas", "nome": "Michael Haas", "nota": "Etzgersrieth? (a conferir)"},
                 {"id": "doc-stadelmann", "nome": "Kunigunde Stadelmann", "nota": "Etzgersrieth? (a conferir)"}),
}
# Casamentos, pela chave do filho
CASAMENTOS = {
    "LYPQ-GW3": "09/03/1948 (civil) e 1947 (igreja), Vidal Ramos",
    "L1BB-H9V": "09/07/1921 (igreja) e 25/02/1923 (civil), São Martinho",
    "GVX4-ZHK": "03/08/1907, Eibenstock (tradição)",
    "GX1B-HM1": "04/03/1878, Leonberg",
    "PXN3-8ZG": "23/11/1884, Moosbach",
    "L1BB-NQ3": "c. 1877; ele casou de novo em 29/04/1900",
    "K84V-VR2": "",
    "KN1Y-GMJ": "1826, São Leopoldo (outro registro: 1865)",
    "KNYK-4J3": "06/05/1849, Hamburgo Velho",
    "G5PB-BSV": "",
    "G5PB-VCC": "1995",
}


class Rec:
    __slots__ = ("level", "xref", "tag", "value", "kids")

    def __init__(self, level, xref, tag, value):
        self.level, self.xref, self.tag, self.value, self.kids = level, xref, tag, value or "", []

    def sub(self, tag):
        return [k for k in self.kids if k.tag == tag]

    def val(self, tag):
        for k in self.kids:
            if k.tag == tag:
                return k.value
        return ""


def ler(caminho):
    raiz, pilha = [], []
    with open(caminho, encoding="utf-8-sig") as f:
        for linha in f:
            linha = linha.rstrip("\r\n")
            m = LINHA.match(linha)
            if not m:
                continue
            r = Rec(int(m.group(1)), m.group(2), m.group(3), m.group(4))
            while pilha and pilha[-1].level >= r.level:
                pilha.pop()
            (pilha[-1].kids if pilha else raiz).append(r)
            pilha.append(r)
    return raiz


def data(txt):
    """Normaliza uma data GEDCOM para dd/mm/aaaa; devolve '' se não houver data aproveitável."""
    t = (txt or "").strip()
    if not t:
        return ""
    m = re.fullmatch(r"\((\d{1,2}) (\w+) (\d{4})\)", t)
    if m and m.group(2) in MES_IT:
        return f"{int(m.group(1)):02d}/{MES_IT[m.group(2)]:02d}/{m.group(3)}"
    if t.startswith("("):
        return ""
    m = re.fullmatch(r"BET (.+) AND (.+)", t)
    if m:
        return f"entre {data(m.group(1))} e {data(m.group(2))}"
    pre = {"ABT ": "c. ", "CAL ": "c. ", "EST ": "c. ", "BEF ": "antes de ", "AFT ": "depois de "}
    for k, v in pre.items():
        if t.startswith(k):
            return v + data(t[len(k):])
    m = re.fullmatch(r"(\d{1,2}) ([A-Z]{3}) (\d{4})", t)
    if m:
        return f"{int(m.group(1)):02d}/{MES[m.group(2)]:02d}/{m.group(3)}"
    m = re.fullmatch(r"([A-Z]{3}) (\d{4})", t)
    if m:
        return f"{MES[m.group(1)]:02d}/{m.group(2)}"
    return t if re.fullmatch(r"\d{4}", t) else ""


RUIDO = re.compile(r"(?i)katholisch|kirche|friedhof|^of$|^cemit|igreja|^(alemanha|germany|deutschland|brasil|brazil|switzerland)$")


def lugar(txt):
    partes = [p.strip() for p in (txt or "").split(",") if p.strip()]
    uteis = [p for p in partes if not RUIDO.search(p)]
    if not uteis:
        return partes[0] if partes and not re.search("(?i)katholisch|kirche", partes[0]) else ""
    p = uteis[0]
    p = re.sub(r"^(of|Kreis)\s+", "", p)
    return {"Suiça": "Suíça", "Rheil": "Reil", "Vargen do Cedro": "Vargem do Cedro", "SCHWEICH": "Schweich"}.get(p, p)


def ano(txt):
    m = re.search(r"\d{4}", txt or "")
    return int(m.group()) if m else None


class Pessoa:
    def __init__(self, fid, nome, b="", pl="", bat=False, d="", dpl="", arr="", nota="", vivo=False):
        self.id, self.nome, self.b, self.pl, self.bat = fid, nome, b, pl, bat
        self.d, self.dpl, self.arr, self.nota, self.vivo = d, dpl, arr, nota, vivo
        self.pais, self.casamento, self.casamento_real, self.conflito = [], "", False, ""
        self.ger, self.continua = 0, None


def evento(r, *tags):
    for t in tags:
        for k in r.sub(t):
            if k.val("DATE") or k.val("PLAC"):
                return k, t
    return None, None


def carregar():
    R = ler(GED)
    ind = {r.xref: r for r in R if r.tag == "INDI"}
    fam = {r.xref: r for r in R if r.tag == "FAM"}

    def monta(x, ger):
        i = ind[x]
        fid = i.val("_FSFTID")
        c = CORRECOES.get(fid, {})
        nome = c.get("nome") or i.val("NAME").replace("/", "").strip()
        ev, tag = evento(i, "BIRT", "CHR", "BAPM")
        b = data(ev.val("DATE")) if ev else ""
        pl = lugar(ev.val("PLAC")) if ev else ""
        # data do batismo só se o nascimento não tiver data
        bat = False
        if not b:
            e2, _ = evento(i, "CHR", "BAPM")
            if e2 and data(e2.val("DATE")):
                b, bat = data(e2.val("DATE")), True
                pl = pl or lugar(e2.val("PLAC"))
        ev, _ = evento(i, "DEAT", "BURI")
        d = data(ev.val("DATE")) if ev else ""
        dpl = lugar(ev.val("PLAC")) if ev else ""
        ev, _ = evento(i, "IMMI")
        arr = ""
        if ev and data(ev.val("DATE")):
            lc = lugar(ev.val('PLAC'))
            if "Florianópolis" in lc or "Desterro" in lc:
                lc = "Desterro"
            arr = f"{lc}, {data(ev.val('DATE'))}".strip(", ")
        p = Pessoa(fid or x, nome, c.get("b", b), c.get("pl", pl), bat and "b" not in c, c.get("d", d),
                   c.get("dpl", dpl), c.get("arr", arr), c.get("nota", ""), fid in VIVOS)
        p.ger = ger
        if ger >= GER_MAX:
            return p
        if fid in EXTRA_PAIS:
            for e in EXTRA_PAIS[fid]:
                q = Pessoa(e["id"], e["nome"], nota=e.get("nota", ""))
                q.ger = ger + 1
                p.pais.append(q)
            return p
        for fc in i.sub("FAMC")[:1]:
            f = fam[fc.value]
            datas = []
            for m in f.sub("MARR"):
                dd = data(m.val("DATE"))
                if dd:
                    datas.append((dd, lugar(m.val("PLAC"))))
            if fid in CASAMENTOS:
                p.casamento = CASAMENTOS[fid]
                p.casamento_real = bool(p.casamento)
            elif datas:
                cont = collections.Counter(dd for dd, _ in datas)
                top = cont.most_common(1)[0][0]
                pl_m = next((l for dd, l in datas if dd == top and l), "")
                p.casamento = f"{top}, {pl_m}" if pl_m else top
                p.casamento_real = True
                outros = [k for k in cont if k != top]
                if outros:
                    p.conflito = f"{top} ou {', '.join(outros)}"
            for t in ("HUSB", "WIFE"):
                if f.val(t):
                    p.pais.append(monta(f.val(t), ger + 1))
        return p

    return monta, ind


# ------------------------------------------------------------------ desenho
TINTA, FUNDO, BORDA, CASA, NAVIO, FALTA, SEGUE = "#2b2620", "#f7f2e6", "#a89f8c", "#a4361f", "#1f5d7a", "#8a8474", "#5d7a1f"
plt.rcParams.update({"font.family": "DejaVu Serif"})
L_W, L_GAP, LH = 2.1, 0.26, 0.158


def linhas_caixa(p):
    out = []
    for l in textwrap.wrap(p.nome, 27):
        out.append((l, TINTA, "bold", 8.4))
    if p.b or p.pl:
        pre = "bat." if p.bat else "n."
        txt = f"{pre} {p.b}" if p.b else "n."
        if p.pl:
            txt = f"{txt}, {p.pl}" if p.b else p.pl
        for l in textwrap.wrap(txt, 33):
            out.append((l, TINTA, "normal", 7.5))
    generico = {"Alemanha", "Germany", "Deutschland", "Brasil", "Santa Catarina"}
    if p.d or (p.dpl and p.dpl not in generico):
        txt = "† " + ", ".join(x for x in (p.d, p.dpl) if x)
        for l in textwrap.wrap(txt, 33):
            out.append((l, TINTA, "normal", 7.5))
    if p.arr:
        for l in textwrap.wrap("chegou: " + p.arr, 33):
            out.append((l, NAVIO, "bold", 7.3))
    if p.nota:
        for l in textwrap.wrap(p.nota, 33):
            out.append((l, TINTA, "italic", 7.3))
    if p.continua:
        out.append((f"continua na árvore {p.continua}", SEGUE, "bold", 7.3))
    elif not p.pais and not p.vivo and p.ger < GER_MAX:
        out.append(("pais a descobrir", FALTA, "italic", 7.3))
    return out


def alt_caixa(p):
    return 0.12 + LH * len(linhas_caixa(p))


def desenha(raiz, n, destino, titulo, nivel=2):
    """Desenha raiz e até `nivel` gerações de pais."""
    guardado, raiz.continua = raiz.continua, None  # a raiz da página não aponta para ela mesma
    def folhas(p, d):
        return [p] if (d == nivel or not p.pais) else [q for x in p.pais for q in folhas(x, d + 1)]
    todos = []
    def visita(p, d):
        todos.append((p, d))
        if d < nivel:
            for q in p.pais:
                visita(q, d + 1)
    visita(raiz, 0)
    cols = max(d for _, d in todos) + 1
    maxh = max(alt_caixa(p) for p, _ in todos)
    passo = maxh + 0.34
    nf = len(folhas(raiz, 0))
    alt = nf * passo + 0.55
    larg = 3 * L_W + 2 * L_GAP + 0.16
    fig = plt.figure(figsize=(larg, alt))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, larg)
    ax.set_ylim(0, alt)
    ax.axis("off")
    ax.text(0.08, alt - 0.1, f"Árvore {n}: {titulo}", fontsize=10.5, fontweight="bold", color=TINTA, va="top")
    pos, cont = {}, [0]

    def coloca(p, d):
        if d == nivel or not p.pais:
            y = alt - 0.5 - passo * (cont[0] + 0.5)
            cont[0] += 1
        else:
            ys = [coloca(q, d + 1) for q in p.pais]
            y = sum(ys) / len(ys)
        pos[id(p)] = (0.08 + d * (L_W + L_GAP), y, p, d)
        return y
    coloca(raiz, 0)
    for x, y, p, d in pos.values():
        h = alt_caixa(p)
        ax.add_patch(FancyBboxPatch((x, y - h / 2), L_W, h, boxstyle="round,pad=0,rounding_size=0.05",
                                    fc=FUNDO, ec=BORDA, lw=0.8, zorder=2))
        ls = linhas_caixa(p)
        for i, (t, c, w, s) in enumerate(ls):
            ax.text(x + 0.07, y + h / 2 - 0.06 - LH * (i + 0.5), t, fontsize=s, color=c, va="center",
                    fontweight="bold" if w == "bold" else "normal", fontstyle="italic" if w == "italic" else "normal", zorder=3)
        if d < nivel and p.pais:
            ys = [pos[id(q)][1] for q in p.pais]
            xm = x + L_W + L_GAP / 2
            ax.plot([x + L_W, xm], [y, y], color=BORDA, lw=0.9, zorder=1)
            ax.plot([xm, xm], [min(ys), max(ys)], color=BORDA, lw=0.9, zorder=1)
            for yy in ys:
                ax.plot([xm, x + L_W + L_GAP], [yy, yy], color=BORDA, lw=0.9, zorder=1)
            if len(p.pais) == 2:
                ym = sum(ys) / 2
                xc = x + L_W + L_GAP + 0.07
                if p.casamento_real:
                    rotulo = chr(10).join(textwrap.wrap("∞ " + p.casamento, 36))
                    ax.text(xc, ym, rotulo, fontsize=7.2, linespacing=1.05, color=CASA, fontweight="bold", va="center", zorder=4,
                            bbox=dict(fc="white", ec="none", pad=0.8))
                elif not p.vivo or p.casamento:
                    ax.text(xc, ym, "∞ data a descobrir", fontsize=7, color=FALTA, fontstyle="italic", va="center", zorder=4,
                            bbox=dict(fc="white", ec="none", pad=0.8))
    fig.savefig(destino, dpi=230, facecolor="white")
    plt.close(fig)
    raiz.continua = guardado


# ------------------------------------------------------------------ páginas em paisagem
# Tamanho real da mancha do livro (15,5 x 23 cm) virada em paisagem, descontada a legenda:
# a figura é desenhada nesse tamanho, para que as letras saiam no corpo em que foram escolhidas.
PAG_W, PAG_H = 7.35, 4.05


def linhas_compactas(p, larg_chars):
    out = []
    for l in textwrap.wrap(p.nome, larg_chars):
        out.append((l, TINTA, "bold"))
    if p.b or p.pl:
        pre = "bat." if p.bat else "n."
        txt = f"{pre} {p.b}" if p.b else "n."
        if p.pl:
            txt = f"{txt}, {p.pl}" if p.b else p.pl
        out += [(l, TINTA, "normal") for l in textwrap.wrap(txt, larg_chars)]
    generico = {"Alemanha", "Germany", "Deutschland", "Brasil", "Santa Catarina"}
    if p.d or (p.dpl and p.dpl not in generico):
        txt = "† " + ", ".join(x for x in (p.d, p.dpl) if x)
        out += [(l, TINTA, "normal") for l in textwrap.wrap(txt, larg_chars)]
    if p.arr:
        out += [(l, NAVIO, "bold") for l in textwrap.wrap("chegou: " + p.arr, larg_chars)]
    if p.nota:
        out += [(l, TINTA, "italic") for l in textwrap.wrap(p.nota, larg_chars)]
    if len(p.pais) == 2:
        if p.casamento_real:
            out += [(l, CASA, "bold") for l in textwrap.wrap("pais ∞ " + p.casamento, larg_chars)]
    if p.continua:
        c = p.continua
        txt = f"continua na árvore {c}" if isinstance(c, int) else f"continua nas árvores {c}"
        out.append((txt, SEGUE, "bold"))
    elif not p.pais and not p.vivo and p.ger < GER_MAX:
        out.append(("pais a descobrir", FALTA, "italic"))
    return out


def desenha_pagina(raizes, n, destino, titulo):
    """Uma página em paisagem com uma ou duas raízes empilhadas, até a geração GER_MAX."""
    def prof(r):
        return GER_MAX - r.ger
    def folhas(p, d, pr):
        return [p] if (d == pr or not p.pais) else [q for x in p.pais for q in folhas(x, d + 1, pr)]
    todos = []
    def visita(p, d, pr):
        todos.append((p, d))
        if d < pr:
            for q in p.pais:
                visita(q, d + 1, pr)
    nf = 0
    for r in raizes:
        visita(r, 0, prof(r))
        nf += len(folhas(r, 0, prof(r)))
    cols = max(d for _, d in todos) + 1
    margem, topo, gap, folga = 0.03, 0.30, 0.10, 0.035
    col_w = (PAG_W - 2 * margem - (cols - 1) * gap) / cols
    util = PAG_H - topo - 0.02

    def tenta(fs):
        lh = fs * 1.22 / 72
        chars = max(14, int((col_w - 0.08) * 72 / (fs * 0.62)))
        alt = {id(q): 0.045 + lh * len(linhas_compactas(q, chars)) for q, _ in todos}
        pos, cur = {}, [PAG_H - topo]

        def coloca(q, d, pr):
            if d == pr or not q.pais:
                h = alt[id(q)]
                y = cur[0] - h / 2
                cur[0] -= h + folga
            else:
                ys = [coloca(z, d + 1, pr) for z in q.pais]
                y = sum(ys) / len(ys)
            pos[id(q)] = (margem + d * (col_w + gap), y, q, d, pr)
            return y
        for i, r in enumerate(raizes):
            if i:
                cur[0] -= 0.12
            coloca(r, 0, prof(r))
        ok = cur[0] + folga >= PAG_H - topo - util
        porcol = {}
        for x, y, q, d, pr in pos.values():
            porcol.setdefault(d, []).append((y + alt[id(q)] / 2, y - alt[id(q)] / 2))
        for caixas in porcol.values():
            caixas.sort(reverse=True)
            for (t1, b1), (t2, b2) in zip(caixas, caixas[1:]):
                if t2 > b1 - 0.01:
                    ok = False
        return ok, lh, chars, alt, pos
    for fs in [7.6, 7.3, 7.0, 6.7, 6.4, 6.1, 5.9, 5.7, 5.5, 5.3, 5.1]:
        ok, lh, chars, alt, pos = tenta(fs)
        if ok:
            break
    fig = plt.figure(figsize=(PAG_W, PAG_H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, PAG_W)
    ax.set_ylim(0, PAG_H)
    ax.axis("off")
    ax.text(margem, PAG_H - 0.03, f"Árvore {n}: {titulo}", fontsize=9.5, fontweight="bold", color=TINTA, va="top")
    for x, y, p, d, pr in pos.values():
        h = alt[id(p)]
        ax.add_patch(FancyBboxPatch((x, y - h / 2), col_w, h, boxstyle="round,pad=0,rounding_size=0.03",
                                    fc=FUNDO, ec=BORDA, lw=0.6, zorder=2))
        for i, (tx, c, w) in enumerate(linhas_compactas(p, chars)):
            ax.text(x + 0.04, y + h / 2 - 0.025 - lh * (i + 0.5), tx, fontsize=fs, color=c, va="center",
                    fontweight="bold" if w == "bold" else "normal",
                    fontstyle="italic" if w == "italic" else "normal", zorder=3)
        if d < pr and p.pais:
            ys = [pos[id(q)][1] for q in p.pais]
            xm = x + col_w + gap / 2
            ax.plot([x + col_w, xm], [y, y], color=BORDA, lw=0.7, zorder=1)
            ax.plot([xm, xm], [min(ys + [y]), max(ys + [y])], color=BORDA, lw=0.7, zorder=1)
            for yy in ys:
                ax.plot([xm, x + col_w + gap], [yy, yy], color=BORDA, lw=0.7, zorder=1)
    fig.savefig(destino, dpi=300, facecolor="white")
    plt.close(fig)


def _folhas(p):
    return [p] if not p.pais else [q for x in p.pais for q in _folhas(x)]


def paginas_paisagem(raiz):
    """Página 1: os meninos até os bisavós. Depois, os ramos de cada casal de bisavós,
    até a 7ª geração; um ramo grande demais é dividido entre o pai e a mãe."""
    LIM = 12
    paginas = [([raiz], "Matheus e Lucas, até os bisavós", raiz, 3)]
    destino = {}
    for pai in raiz.pais:
        for avo in pai.pais:
            casal = [b for b in avo.pais if b.pais]
            if not casal:
                continue
            total = sum(len(_folhas(b)) for b in casal)
            if total <= LIM:
                nomes = " e ".join(b.nome.split(",")[0] for b in casal)
                paginas.append((casal, f"antepassados de {nomes}", None, None))
                for b in casal:
                    destino[id(b)] = [len(paginas)]
            else:
                for b in casal:
                    if len(_folhas(b)) <= LIM:
                        paginas.append(([b], f"antepassados de {b.nome.split(',')[0]}", None, None))
                        destino[id(b)] = [len(paginas)]
                    else:
                        destino[id(b)] = []
                        for q in b.pais:
                            if q.pais:
                                rel = "pai" if q is b.pais[0] else "mãe"
                                paginas.append(([q], f"{rel} de {b.nome.split(',')[0]}: antepassados de {q.nome.split(',')[0]}", None, None))
                                destino[id(b)].append(len(paginas))
    for pai in raiz.pais:
        for avo in pai.pais:
            for b in avo.pais:
                nums = destino.get(id(b))
                if nums:
                    b.continua = nums[0] if len(nums) == 1 else " e ".join(map(str, nums))
    return paginas


def paginar(raiz):
    paginas, fila = [], [raiz]
    while fila:
        p = fila.pop(0)
        n = len(paginas) + 1
        paginas.append(p)

        def ponta(q, d):
            if d == 2:
                return [q] if q.pais else []
            return [z for x in q.pais for z in ponta(x, d + 1)]
        for q in ponta(p, 0):
            fila.append(q)
    # numera as continuações
    num = {id(p): i + 1 for i, p in enumerate(paginas)}
    for p in paginas:
        def marca(q, d):
            if d == 2:
                if q.pais:
                    q.continua = num[id(q)]
                return
            for x in q.pais:
                marca(x, d + 1)
        marca(p, 0)
    return paginas


def incoerencias(raiz):
    out = []
    vistos = []

    def visita(p):
        vistos.append(p)
        by, dy = ano(p.b), ano(p.d)
        if by and dy and dy - by > 100:
            out.append(f"{p.nome} ({p.id}): viveu {dy - by} anos? n. {p.b}, † {p.d}.")
        if by and dy and dy < by:
            out.append(f"{p.nome} ({p.id}): morte ({p.d}) antes do nascimento ({p.b}).")
        for q in p.pais:
            qy = ano(q.b)
            if by and qy and by - qy < 15:
                out.append(f"{q.nome} ({q.id}), n. {q.b}, teria {by - qy} anos quando nasceu {p.nome} (n. {p.b}).")
            if by and qy and by - qy > 55:
                out.append(f"{q.nome} ({q.id}), n. {q.b}, teria {by - qy} anos quando nasceu {p.nome} (n. {p.b}).")
            qd = ano(q.d)
            if by and qd and qd < by - 1:
                out.append(f"{q.nome} ({q.id}), † {q.d}, morreu antes do nascimento de {p.nome} (n. {p.b}).")
            mc = ano(p.casamento)
            if mc and qy and mc - qy < 14:
                out.append(f"Casamento dos pais de {p.nome} ({p.casamento}) incompatível com o nascimento de {q.nome} ({q.b}).")
        if p.conflito:
            out.append(f"Casamento dos pais de {p.nome}: registros divergentes ({p.conflito}).")
        for q in p.pais:
            visita(q)
    visita(raiz)
    return out, vistos


def lacunas(vistos):
    linhas = []
    for p in vistos:
        if p.vivo:
            continue
        falta = []
        if not p.b:
            falta.append("data de nascimento ou batismo")
        elif not re.fullmatch(r"\d{2}/\d{2}/\d{4}", p.b):
            falta.append(f"data exata de nascimento (hoje: {p.b})")
        if not p.pl:
            falta.append("lugar de nascimento")
        if not p.d:
            falta.append("data de morte")
        elif not re.fullmatch(r"\d{2}/\d{2}/\d{4}", p.d):
            falta.append(f"data exata de morte (hoje: {p.d})")
        if p.ger < GER_MAX and not p.pais:
            falta.append("nomes dos pais")
        if p.ger < GER_MAX and len(p.pais) == 1:
            falta.append("nome do outro genitor")
        if len(p.pais) == 2 and not p.casamento_real and p.ger < GER_MAX:
            falta.append("data e lugar do casamento dos pais")
        if falta:
            b = f"n. {p.b}" if p.b else "nascimento desconhecido"
            pl = f", {p.pl}" if p.pl else ""
            pais = " e ".join(q.nome for q in p.pais)
            filho = f"; filho(a) de {pais}" if pais else ""
            linhas.append((p.ger, f"- **{p.nome}** (`{p.id}`; {b}{pl}{filho}). Falta: {'; '.join(falta)}."))
    return linhas


def principal():
    monta, ind = carregar()
    m = next(x for x, r in ind.items() if r.val("_FSFTID") == "G5PB-VCC")
    raiz = monta(m, 0)
    raiz.nome = "Matheus e Lucas Haas"
    raiz.b, raiz.pl, raiz.vivo = "", "", True
    raiz.casamento, raiz.casamento_real = "1995", True
    pags = paginas_paisagem(raiz)
    paginas = [r for rs, _, _, _ in pags for r in rs]
    for a in IMG.glob("arvore_*.png"):
        a.unlink()
    figs = []
    for n, (rs, tit, _, _) in enumerate(pags, 1):
        nome = f"arvore_{n:02d}.png"
        salvos = []
        if n > 1:
            for r in rs:
                salvos.append((r, r.continua))
                r.continua = None
        if n == 1:
            # na página 1 a raiz desce só até os bisavós
            g = GER_MAX
            globals()["GER_MAX"] = 3
            desenha_pagina(rs, n, IMG / nome, tit)
            globals()["GER_MAX"] = g
        else:
            desenha_pagina(rs, n, IMG / nome, tit)
        for r, c in salvos:
            r.continua = c
        figs.append((nome, tit))
        print(nome, tit)
    txt = ["## As Árvores da Família {#arvores .unnumbered}\n",
           "Estas são as árvores de vocês até a sétima geração, até onde sei hoje, com as datas de nascimento, de morte, de casamento e de chegada ao Brasil. Comecem pela árvore 1, que vai de vocês até os bisavós, e sigam os avisos \"continua na árvore\": cada uma das outras é um ramo da família, até a sétima geração. A data do casamento dos pais de cada pessoa aparece na caixa dela, em vermelho, depois de \"pais ∞\". Quem não aparece é porque ainda não conheço; \"pais a descobrir\" é a pergunta que deixo para vocês. Boa parte das datas mais antigas vem do FamilySearch, uma árvore colaborativa, e ainda precisa ser conferida nos livros. Pessoas vivas aparecem só com o ano, ou sem data.\n"]
    for nome, tit in figs:
        txt.append(f"![{tit[0].upper() + tit[1:]}.](imagens/{nome}){{width=100%}}\n")
    CAP.write_text("\n".join(txt), encoding="utf-8")
    inc, vistos = incoerencias(raiz)
    lac = lacunas(vistos)
    corpo = [f"# Lacunas e incoerências da árvore ({len(vistos)} pessoas em {len(pags)} árvores)\n",
             "Gerado por `scripts/arvore_livro.py`. Pessoas vivas ficam de fora.\n", "## Incoerências a resolver\n"]
    corpo += [f"- {x}" for x in dict.fromkeys(inc)]
    for g in range(0, GER_MAX + 1):
        ls = list(dict.fromkeys(l for gg, l in lac if gg == g))
        if ls:
            corpo.append(f"\n## Geração {g} acima de Matheus e Lucas\n")
            corpo += ls
    LACUNAS.write_text("\n".join(corpo) + "\n", encoding="utf-8")
    print(len(vistos), "pessoas;", len(pags), "árvores;", len(lac), "com lacunas;", len(set(inc)), "incoerências")


if __name__ == "__main__":
    principal()
