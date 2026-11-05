"""Monta o livro "Nossa Família" em LaTeX/PDF e em HTML.

Uso (a partir da raiz do repositório):
    python livro/build.py            # LaTeX + PDF + HTML
    python livro/build.py --sem-pdf  # pula a compilação do PDF

Saídas:
    livro/latex/livro.tex, livro/latex/livro.pdf
    livro/site/  (index.html + uma página por capítulo + imagens/)
"""
import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
LIVRO = RAIZ / "livro"
CAPS = LIVRO / "capitulos"
IMG_ORIG = RAIZ / "imagens"
LATEX = LIVRO / "latex"
SITE = LIVRO / "site"

TITULO = "Nossa Família"
SUBTITULO = "Da Alemanha ao Sul do Brasil"
AUTOR = "Reinaldo Haas"
DEDICATORIA = ("Para Matheus e Lucas — ponto de encontro de todos os navios, serras e sonhos "
               "que nos trouxeram até aqui — e para Bárbara, companheira de todas as travessias.")

# (numeral, título, boletim, prefixos dos arquivos)
PARTES = [
    ("I", "Ecos na Serra Catarinense",
     "Situação sinótica: frente fria estacionária sobre o Vale do Itajaí. "
     "Tendência: perda gradual das vozes antigas. Recomenda-se ouvir enquanto é tempo.",
     ["01", "02", "03"]),
    ("II", "O Vapor Formosa e a Floresta",
     "Deslocamento previsto: Marselha, Rio de Janeiro, Laguna. Mar de través, quarentena "
     "prolongada. Na serra, mata fechada e promessas que não se cumprem.",
     ["04", "05", "06", "07"]),
    ("III", "Os Pioneiros de 1828, o Mosela e as Lâminas de Solingen",
     "Alísios de nordeste. Veleiros retidos na calmaria equatorial. "
     "Visibilidade: quase dois séculos.",
     ["08", "09", "10"]),
    ("IV", "Os Horizontes de Bárbara",
     "Ar úmido subindo o Vale do Taquari. Correntes contínuas entre Joinville, "
     "Estrela e Arroio do Meio. Microclimas de família.",
     ["11", "12"]),
    ("V", "Três Rios, o Clima e uma Herança",
     "Alerta hidrológico para as bacias do Tubarão, do Itajaí e do Taquari; granizo na Ilha. "
     "Tempo de retorno: uma geração.",
     ["13", "14", "15"]),
    ("VI", "Inverno na Baviera",
     "Anticiclone continental sobre a Europa Central. Temperaturas negativas. "
     "Céu limpo para a leitura de arquivos.",
     ["16", "17", "18", "19"]),
]

PANDOC = shutil.which("pandoc") or "pandoc"


def capitulos():
    return sorted(p for p in CAPS.glob("[0-9][0-9]_*.md"))


def parte_de(prefixo):
    for parte in PARTES:
        if prefixo in parte[3]:
            return parte
    return None


def titulo_do_capitulo(texto):
    m = re.search(r"^##\s+(.+?)\s*(\{[^}]*\})?\s*$", texto, re.M)
    return m.group(1).strip() if m else "Sem título"


# ---------------------------------------------------------------- imagens
def preparar_imagens(destino, lado_max):
    """Copia as imagens referenciadas pelo livro, reduzidas e em JPEG."""
    destino.mkdir(parents=True, exist_ok=True)
    usadas = set()
    for cap in capitulos():
        usadas |= set(re.findall(r"\]\(imagens/([^)\s]+)\)", cap.read_text(encoding="utf-8")))
    usadas.add("haas_despedida_abreise_brasilien_1913.jpg")  # capa
    for nome in sorted(usadas):
        orig = IMG_ORIG / nome
        if not orig.exists():
            print(f"  aviso: imagem ausente {nome}", file=sys.stderr)
            continue
        alvo = destino / (Path(nome).stem + ".jpg")
        if alvo.exists() and alvo.stat().st_mtime > orig.stat().st_mtime:
            continue
        with Image.open(orig) as im:
            im = im.convert("RGB")
            im.thumbnail((lado_max, lado_max), Image.LANCZOS)
            im.save(alvo, "JPEG", quality=85, optimize=True, progressive=True)
    return usadas


def apontar_para_jpg(texto):
    return re.sub(r"(\]\(imagens/[^)\s]+?)\.(png|jpeg|jfif|tif)\)", r"\1.jpg)", texto)


# ---------------------------------------------------------------- LaTeX
LATEX_PREAMBULO = r"""
\usepackage{float}
\floatplacement{figure}{htbp}
\usepackage[most]{tcolorbox}
\newtcolorbox{ficha}{breakable, enhanced, colback=black!3, colframe=black!45,
  boxrule=0.4pt, arc=1mm, left=3mm, right=3mm, top=2mm, bottom=2mm, fontupper=\small}
\newenvironment{boletim}{\begin{center}\begin{minipage}{0.85\linewidth}\small\itshape}{\end{minipage}\end{center}}
\usepackage{truncate}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\itshape Nossa Família}
\fancyhead[RO]{\small\itshape\truncate{0.85\headwidth}{\nouppercase{\leftmark}}}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{#1}}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}}
\setlength{\emergencystretch}{3em}
\renewcommand{\figurename}{Figura}
"""

LUA_FILTRO = r"""
function Div(el)
  for _, cls in ipairs({"ficha", "boletim"}) do
    if el.classes:includes(cls) then
      return {pandoc.RawBlock("latex", "\\begin{" .. cls .. "}")}
        .. el.content .. {pandoc.RawBlock("latex", "\\end{" .. cls .. "}")}
    end
  end
end
"""


def montar_markdown_latex():
    partes_abertas = set()
    blocos = []
    for cap in capitulos():
        prefixo = cap.name[:2]
        texto = apontar_para_jpg(cap.read_text(encoding="utf-8"))
        parte = parte_de(prefixo)
        if parte and parte[0] not in partes_abertas:
            partes_abertas.add(parte[0])
            blocos.append(f"# {parte[1]}\n\n::: boletim\n{parte[2]}\n:::\n")
        # O LaTeX numera capítulos e partes: tira o prefixo "Capítulo N — ".
        texto = re.sub(r"^(##\s+)Cap[ií]tulo\s+\d+\s+[—–-]\s+", r"\1", texto, flags=re.M)
        # Notas de rodapé com o mesmo rótulo em capítulos diferentes colidiriam.
        texto = re.sub(r"\[\^([^\]]+)\]", rf"[^c{prefixo}-\1]", texto)
        blocos.append(texto)
    return "\n\n".join(blocos)


def gerar_latex(compilar_pdf):
    LATEX.mkdir(parents=True, exist_ok=True)
    preparar_imagens(LATEX / "imagens", 1800)
    (LATEX / "preambulo.tex").write_text(LATEX_PREAMBULO, encoding="utf-8")
    (LATEX / "divs.lua").write_text(LUA_FILTRO, encoding="utf-8")
    frente = (r"\frontmatter" "\n"
              r"\thispagestyle{empty}\vspace*{0.3\textheight}" "\n"
              r"\begin{flushright}\itshape " + DEDICATORIA + r"\end{flushright}" "\n"
              r"\cleardoublepage\tableofcontents" "\n" r"\mainmatter" "\n")
    (LATEX / "frente.tex").write_text(frente, encoding="utf-8")
    md = LATEX / "livro.md"
    md.write_text(montar_markdown_latex(), encoding="utf-8")
    cmd = [PANDOC, md.name, "-s", "-o", "livro.tex",
           "--top-level-division=part", "--lua-filter=divs.lua",
           "-H", "preambulo.tex", "-B", "frente.tex",
           "-M", f"title={TITULO}", "-M", f"subtitle={SUBTITULO}", "-M", f"author={AUTOR}",
           "-M", "lang=pt-BR",
           "-V", "documentclass=book", "-V", "classoption=openany",
           "-V", "geometry:paperwidth=15.5cm,paperheight=23cm,inner=2cm,outer=1.8cm,top=2cm,bottom=2.2cm",
           "-V", "mainfont=Palatino Linotype", "-V", "sansfont=Segoe UI",
           "-V", "fontsize=11pt", "-V", "linestretch=1.12", "-V", "toc-depth=0",
           "-V", "colorlinks=true", "-V", "linkcolor=black", "-V", "urlcolor=blue!50!black"]
    subprocess.run(cmd, cwd=LATEX, check=True)
    print("LaTeX:", LATEX / "livro.tex")
    if compilar_pdf:
        for _ in range(2):
            r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "livro.tex"],
                               cwd=LATEX, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                print(r.stdout[-4000:], file=sys.stderr)
                raise SystemExit("xelatex falhou")
        print("PDF:", LATEX / "livro.pdf")


# ---------------------------------------------------------------- HTML
CSS = r"""
:root{--bg:#fbf8f2;--fg:#2a2622;--muted:#6f655b;--accent:#7a3b1d;--rule:#e2d9cc;--card:#f3ede3;--ficha:#f1ebe0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17150f;--fg:#ebe4d8;--muted:#a99f91;--accent:#e0a37c;--rule:#38322a;--card:#211e17;--ficha:#26221a}}
:root[data-theme="dark"]{--bg:#17150f;--fg:#ebe4d8;--muted:#a99f91;--accent:#e0a37c;--rule:#38322a;--card:#211e17;--ficha:#26221a}
*{box-sizing:border-box}
html{font-size:18px}
body{margin:0;background:var(--bg);color:var(--fg);font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;line-height:1.7;-webkit-text-size-adjust:100%}
a{color:var(--accent)}
.topo{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--rule);font-family:system-ui,"Segoe UI",sans-serif;font-size:.78rem;z-index:5}
.topo .in{max-width:46rem;margin:0 auto;padding:.6rem 1rem;display:flex;gap:1rem;align-items:center;justify-content:space-between}
.topo a{text-decoration:none;color:var(--muted)} .topo a.livro{color:var(--fg);font-weight:600}
main{max-width:40rem;margin:0 auto;padding:2.5rem 1rem 4rem}
.parte{font-family:system-ui,"Segoe UI",sans-serif;text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;color:var(--muted);margin:0 0 .5rem}
h1,h2{font-weight:500;line-height:1.25;margin:0 0 1rem}
h2{font-size:1.9rem} h3{font-size:1.2rem;margin:2.4rem 0 .6rem;color:var(--accent);font-weight:600}
main>p:first-of-type,h2+p{margin-top:0}
blockquote{margin:1.5rem 0;padding:0 1.2rem;border-left:3px solid var(--rule);color:var(--muted);font-style:italic}
figure{margin:2rem -1rem;text-align:center}
figure img{max-width:100%;height:auto;border-radius:3px;box-shadow:0 1px 6px rgba(0,0,0,.18);cursor:zoom-in}
figcaption{font-size:.82rem;color:var(--muted);margin:.6rem 1rem 0;line-height:1.5}
.ficha{background:var(--ficha);border:1px solid var(--rule);border-radius:6px;padding:.9rem 1.1rem;font-size:.88rem;margin:1.6rem 0}
.ficha p{margin:.3rem 0}
.boletim{font-style:italic;color:var(--muted);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.8rem 0;margin:0 0 2rem}
.footnotes{font-size:.82rem;color:var(--muted);border-top:1px solid var(--rule);margin-top:3rem}
.footnotes hr{display:none}
nav.pag{display:flex;justify-content:space-between;gap:1rem;margin-top:3.5rem;padding-top:1.2rem;border-top:1px solid var(--rule);font-family:system-ui,"Segoe UI",sans-serif;font-size:.82rem}
nav.pag a{text-decoration:none;max-width:48%} nav.pag .prox{text-align:right;margin-left:auto}
nav.pag small{display:block;color:var(--muted)}
.capa{text-align:center;padding-top:1rem}
.capa img{width:100%;max-width:40rem;border-radius:3px;filter:sepia(.25)}
.capa h1{font-size:2.5rem;margin:1.6rem 0 .4rem}
.capa .sub{color:var(--muted);font-style:italic;margin:0 auto 1rem;max-width:32rem}
.capa .autor{font-family:system-ui,"Segoe UI",sans-serif;letter-spacing:.14em;text-transform:uppercase;font-size:.8rem}
.dedic{font-style:italic;text-align:right;color:var(--muted);margin:2.5rem 0}
.sumario h3{margin-top:2rem;font-size:.75rem;font-family:system-ui,"Segoe UI",sans-serif;text-transform:uppercase;letter-spacing:.12em;color:var(--muted)}
.sumario ol{list-style:none;padding:0;margin:0}
.sumario li{padding:.45rem 0;border-bottom:1px solid var(--rule)}
.sumario li a{text-decoration:none;color:var(--fg)}
.downloads{display:flex;flex-wrap:wrap;gap:.6rem;justify-content:center;margin:1.5rem 0;font-family:system-ui,"Segoe UI",sans-serif;font-size:.82rem}
.downloads a{border:1px solid var(--rule);border-radius:999px;padding:.35rem .9rem;text-decoration:none;background:var(--card)}
.nota{font-size:.8rem;color:var(--muted);text-align:center;margin-top:3rem}
#zoom{position:fixed;inset:0;background:rgba(0,0,0,.88);display:none;align-items:center;justify-content:center;z-index:10;cursor:zoom-out}
#zoom img{max-width:96vw;max-height:94vh}
@media (max-width:600px){html{font-size:17px}h2{font-size:1.55rem}.capa h1{font-size:1.9rem}figure{margin:1.5rem 0}}
"""

JS = """<div id="zoom"><img alt=""></div><script>
const z=document.getElementById('zoom'),zi=z.querySelector('img');
document.querySelectorAll('figure img').forEach(i=>i.addEventListener('click',()=>{zi.src=i.src;zi.alt=i.alt;z.style.display='flex'}));
z.addEventListener('click',()=>{z.style.display='none'});
</script>"""


def pagina(titulo, corpo, extra_head=""):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(SUBTITULO)}">
<link rel="stylesheet" href="estilo.css">{extra_head}
</head><body>
<header class="topo"><div class="in"><a class="livro" href="index.html">{html.escape(TITULO)}</a><a href="index.html#sumario">Sumário</a></div></header>
<main>
{corpo}
</main>{JS}
</body></html>"""


def md_para_html(texto):
    r = subprocess.run([PANDOC, "-f", "markdown", "-t", "html5", "--wrap=none",
                        "--section-divs=false"],
                       input=texto, capture_output=True, text=True, encoding="utf-8", check=True)
    return r.stdout


def gerar_html():
    if SITE.exists():
        for p in SITE.glob("*.html"):
            p.unlink()
    SITE.mkdir(parents=True, exist_ok=True)
    preparar_imagens(SITE / "imagens", 1600)
    (SITE / "estilo.css").write_text(CSS, encoding="utf-8")

    caps = capitulos()
    itens = []
    for cap in caps:
        texto = cap.read_text(encoding="utf-8")
        itens.append({"arq": cap, "slug": cap.stem + ".html", "titulo": titulo_do_capitulo(texto),
                      "parte": parte_de(cap.name[:2])})

    for i, it in enumerate(itens):
        texto = apontar_para_jpg(it["arq"].read_text(encoding="utf-8"))
        corpo = md_para_html(texto)
        topo = ""
        parte = it["parte"]
        if parte:
            topo = f'<p class="parte">Parte {parte[0]} · {html.escape(parte[1])}</p>'
            if i == 0 or itens[i - 1]["parte"] != parte:
                corpo = re.sub(r"(</h2>)", r'\1<p class="boletim">' + html.escape(parte[2]) + "</p>",
                               corpo, count=1)
        ant = itens[i - 1] if i > 0 else None
        prox = itens[i + 1] if i + 1 < len(itens) else None
        nav = '<nav class="pag">'
        if ant:
            nav += f'<a href="{ant["slug"]}"><small>← anterior</small>{html.escape(ant["titulo"])}</a>'
        if prox:
            nav += f'<a class="prox" href="{prox["slug"]}"><small>próximo →</small>{html.escape(prox["titulo"])}</a>'
        nav += "</nav>"
        (SITE / it["slug"]).write_text(pagina(f'{it["titulo"]} — {TITULO}', topo + corpo + nav),
                                       encoding="utf-8")

    # índice
    sumario, parte_atual = [], None
    for it in itens:
        if it["parte"] != parte_atual:
            if parte_atual is not None or sumario:
                sumario.append("</ol>")
            parte_atual = it["parte"]
            rotulo = f"Parte {parte_atual[0]} — {parte_atual[1]}" if parte_atual else ""
            sumario.append(f"<h3>{html.escape(rotulo)}</h3><ol>" if rotulo else "<ol>")
        sumario.append(f'<li><a href="{it["slug"]}">{html.escape(it["titulo"])}</a></li>')
    sumario.append("</ol>")
    downloads = ""
    if (SITE / "livro.pdf").exists():
        downloads += '<a href="livro.pdf">Baixar PDF</a>'
    if (SITE / "livro_latex.zip").exists():
        downloads += '<a href="livro_latex.zip">Código-fonte LaTeX</a>'
    downloads += '<a href="https://github.com/reinaldohaas/arvore_genealogica">Repositório da árvore</a>'
    corpo = f"""<div class="capa">
<img src="imagens/haas_despedida_abreise_brasilien_1913.jpg" alt="Fotografia de despedida da família Haas antes da partida para o Brasil, 7 de março de 1913">
<h1>{html.escape(TITULO)}</h1>
<p class="sub">{html.escape(SUBTITULO)}</p>
<p class="autor">{html.escape(AUTOR)}</p>
<div class="downloads">{downloads}</div>
</div>
<p class="dedic">{html.escape(DEDICATORIA)}</p>
<section class="sumario" id="sumario"><h2>Sumário</h2>{''.join(sumario)}</section>
<p class="nota">Versão de trabalho. Reconstituições históricas vêm sinalizadas no texto; correções e lembranças da família são bem-vindas.</p>"""
    (SITE / "index.html").write_text(pagina(TITULO, corpo), encoding="utf-8")
    print("HTML:", SITE / "index.html")


def empacotar_latex():
    """Copia PDF e um zip do fonte LaTeX para o site."""
    if (LATEX / "livro.pdf").exists():
        shutil.copy2(LATEX / "livro.pdf", SITE / "livro.pdf")
    import zipfile
    with zipfile.ZipFile(SITE / "livro_latex.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for nome in ["livro.tex", "preambulo.tex", "frente.tex", "divs.lua", "livro.md"]:
            z.write(LATEX / nome, nome)
        for img in sorted((LATEX / "imagens").glob("*.jpg")):
            z.write(img, f"imagens/{img.name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sem-pdf", action="store_true")
    a = ap.parse_args()
    gerar_latex(not a.sem_pdf)
    SITE.mkdir(parents=True, exist_ok=True)
    empacotar_latex()
    gerar_html()


if __name__ == "__main__":
    main()
