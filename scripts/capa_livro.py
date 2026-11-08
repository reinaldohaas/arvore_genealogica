"""Gera a capa do livro (15,5 x 23 cm, 300 dpi) em português e em alemão.

A capa é um mapa em três etapas, uma cor para cada avô ou avó de Matheus e Lucas:
1. de cada lugar de origem na Europa (Alemanha, Suíça, Hungria) ao lugar onde a
   família foi viver no Sul do Brasil;
2. desses lugares a Vidal Ramos (os ramos de Reinaldo) e a Joinville (os de Bárbara);
3. de Vidal Ramos a Florianópolis, e de Joinville, passando por Porto Alegre, onde
   Bárbara nasceu, a Florianópolis.

Uso: python scripts/capa_livro.py   ->  imagens/capa_pt.jpg/.pdf, capa_de.jpg/.pdf
"""
from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MPath

RAIZ = Path(__file__).resolve().parents[1]
IMG = RAIZ / "imagens"
FUNDO, TERRA, LINHA, OURO, CREME, MUDO = "#231a14", "#3a2d22", "#6b5843", "#d9a94e", "#f2e8d5", "#c8b89a"
plt.rcParams.update({"font.family": "Palatino Linotype"})

# Os quatro ramos, um por avô ou avó dos meninos: cor, nome e onde o ramo se reúne.
RAMOS = {
    "baldoino": ("#e0b04f", "Baldoíno Haas", "vidal"),
    "adelina": ("#e07a5f", "Adelina Doerner", "vidal"),
    "carlos": ("#7fc4b8", "Carlos Heinz Funke", "joinville"),
    "ilusca": ("#9db8e8", "Ilusca Hoeveler", "joinville"),
}
# (sobrenomes, lugar pt, lugar de, lat, lon, ramo, onde foram viver, deslocamento do rótulo, alinhamento)
ORIGENS = [
    ("Haas", "Leonberg", "Leonberg", 49.21, 12.10, "baldoino", "anitapolis", (6, -10), "left"),
    ("Meier · Voit", "Heumaden", "Heumaden", 49.62, 12.40, "baldoino", "anitapolis", (6, 4), "left"),
    ("Dörner", "Solingen", "Solingen", 51.17, 7.08, "adelina", "smartinho", (-6, 2), "right"),
    ("Eller", "Vestfália", "Westfalen", 51.72, 8.75, "adelina", "smartinho", (-6, 3), "right"),
    ("Preis · Loch · Michels · Arns", "Mosela e Hunsrück", "Mosel und Hunsrück", 49.85, 6.90, "adelina", "spedro", (-6, -2), "right"),
    ("Funke", "Glauchau", "Glauchau", 50.82, 12.54, "carlos", "joinville", (6, 2), "left"),
    ("Aenishaenslin", "Basel-Landschaft, Suíça", "Basel-Landschaft, Schweiz", 47.47, 7.87, "carlos", "joinville", (6, -3), "left"),
    ("Hoeveler", "Hungria", "Ungarn", 47.30, 19.30, "ilusca", "taquari", (0, 8), "center"),
    ("Lohmann", "Harderode", "Harderode", 52.03, 9.46, "ilusca", "taquari", (6, 5), "left"),
    ("Schnack · Wacker", "Schleswig", "Schleswig", 54.55, 9.57, "ilusca", "taquari", (6, 0), "left"),
    ("Wingert", "Albig", "Albig", 49.77, 8.13, "ilusca", "taquari", (5, 7), "left"),
    ("Köhnlein · Lange", "Württemberg", "Württemberg", 49.25, 9.95, "ilusca", "tforquilhas", (-6, -9), "right"),
    ("Mentz", "Tambach", "Tambach", 50.79, 10.61, "ilusca", "taquari", (-6, 4), "right"),
]
# Onde foram viver (etapa 1): nome pt, nome de, lat, lon, deslocamento, alinhamento
LUGARES = {
    "anitapolis": ("Anitápolis", "Anitápolis", -27.90, -49.13, (-7, -2), "right"),
    "smartinho": ("São Martinho", "São Martinho", -28.16, -48.98, (7, -3), "left"),
    "spedro": ("São Pedro\nde Alcântara", "São Pedro\nde Alcântara", -27.57, -48.80, (-2, -12), "center"),
    "taquari": ("Vale do Taquari", "Taquari-Tal", -29.50, -51.96, (0, -10), "center"),
    "tforquilhas": ("Três Forquilhas", "Três Forquilhas", -29.53, -50.07, (7, -2), "left"),
}
# Onde os ramos se reúnem (etapas 2 e 3)
ENCONTROS = {
    "vidal": ("Vidal Ramos", -27.39, -49.36, (-8, 0), "right"),
    "joinville": ("Joinville", -26.30, -48.85, (8, 2), "left"),
    "poa": ("Porto Alegre", -30.03, -51.23, (-8, -2), "right"),
    "floripa": ("Florianópolis", -27.60, -48.55, (8, 2), "left"),
}
TEXTOS = {
    "pt": ("Nossa Família", "Da Alemanha ao Sul do Brasil", "REINALDO HAAS", "BÁRBARA FUNKE HAAS"),
    "de": ("Unsere Familie", "Von Deutschland in den Süden Brasiliens", "REINALDO HAAS", "BÁRBARA FUNKE HAAS"),
}


def base(ax, extent):
    ax.set_extent(extent, ccrs.PlateCarree())
    ax.set_facecolor(FUNDO)
    ax.add_feature(cf.NaturalEarthFeature("physical", "land", "50m", facecolor=TERRA, edgecolor="none"))
    ax.add_feature(cf.NaturalEarthFeature("cultural", "admin_0_boundary_lines_land", "50m",
                                          facecolor="none", edgecolor=LINHA, linewidth=0.5))
    ax.add_feature(cf.NaturalEarthFeature("physical", "coastline", "50m", facecolor="none",
                                          edgecolor=LINHA, linewidth=0.6))
    for s in ax.spines.values():
        s.set_visible(False)


def capa(lang):
    tit, sub, aut1, aut2 = TEXTOS[lang]
    fig = plt.figure(figsize=(15.5 / 2.54, 23 / 2.54), facecolor=FUNDO)
    W, H = fig.get_size_inches()
    eu = fig.add_axes([0.04, 0.60, 0.92, 0.38], projection=ccrs.PlateCarree())
    base(eu, [3.0, 21.5, 46.4, 55.4])
    br = fig.add_axes([0.04, 0.02, 0.92, 0.46], projection=ccrs.PlateCarree())
    base(br, [-53.3, -47.6, -30.4, -25.8])
    fig.canvas.draw()   # fixa a posição real dos mapas antes de traçar os fios

    def em_fig(ax, lon, lat):
        x, y = ax.transData.transform(ax.projection.transform_point(lon, lat, ccrs.PlateCarree()))
        return fig.transFigure.inverted().transform((x, y))

    def ponto_br(chave):
        if chave in LUGARES:
            l = LUGARES[chave]
            return em_fig(br, l[3], l[2])
        e = ENCONTROS[chave]
        return em_fig(br, e[2], e[1])

    def fio(p0, p3, cor, lw, alpha, z, c1=None, c2=None):
        c1 = c1 or ((2 * p0[0] + p3[0]) / 3, (2 * p0[1] + p3[1]) / 3)
        c2 = c2 or ((p0[0] + 2 * p3[0]) / 3, (p0[1] + 2 * p3[1]) / 3)
        caminho = MPath([p0, c1, c2, p3], [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
        fig.patches.append(PathPatch(caminho, transform=fig.transFigure, fc="none", ec=cor, lw=lw, alpha=alpha, zorder=z))

    # etapa 1: da Europa até onde foram viver, passando pelo Atlântico (à direita)
    for nomes, lpt, lde, lat, lon, ramo, lugar, _, _ in ORIGENS:
        p0 = em_fig(eu, lon, lat)
        p3 = ponto_br(lugar)
        fio(p0, p3, RAMOS[ramo][0], 1.15, 0.8, 1,
            (min(0.97, p0[0] + 0.30), p0[1] - 0.10), (0.97, p3[1] + 0.22))
    # etapa 2: dos lugares onde viveram até Vidal Ramos ou Joinville
    feitos = set()
    for _, _, _, _, _, ramo, lugar, _, _ in ORIGENS:
        destino = RAMOS[ramo][2]
        if lugar == destino or (lugar, destino) in feitos:
            continue
        feitos.add((lugar, destino))
        a, b = ponto_br(lugar), ponto_br(destino)
        meio = ((a[0] + b[0]) / 2 - 0.02, (a[1] + b[1]) / 2 + 0.01)
        fio(a, b, RAMOS[ramo][0], 1.9, 0.95, 2, meio, meio)
    # etapa 3: Vidal Ramos → Florianópolis; Joinville → Porto Alegre (onde Bárbara nasceu) → Florianópolis
    vr, jv, pa, fl = (ponto_br(k) for k in ("vidal", "joinville", "poa", "floripa"))
    fio(vr, fl, CREME, 2.4, 1, 3, (vr[0] + 0.02, vr[1] + 0.03), (fl[0] - 0.01, fl[1] + 0.03))
    fio(jv, pa, CREME, 2.4, 1, 3, (jv[0] - 0.06, jv[1] - 0.02), (pa[0] + 0.02, pa[1] + 0.08))
    fio(pa, fl, CREME, 2.4, 1, 3, (pa[0] + 0.10, pa[1] - 0.06), (fl[0] + 0.06, fl[1] - 0.07))

    for nomes, lpt, lde, lat, lon, ramo, lugar, off, ha in ORIGENS:
        eu.plot(lon, lat, "o", ms=4.6, color=RAMOS[ramo][0], mec=FUNDO, mew=0.6, transform=ccrs.PlateCarree(), zorder=5)
        nome_lugar = lpt if lang == "pt" else lde
        eu.annotate(f"{nomes}\n", (lon, lat), xytext=off, textcoords="offset points", ha=ha, va="center",
                    fontsize=6.6, fontweight="bold", color=CREME, zorder=6,
                    bbox=dict(fc=FUNDO, ec="none", alpha=0.55, pad=0.6), transform=ccrs.PlateCarree())
        eu.annotate(f"\n{nome_lugar}", (lon, lat), xytext=off, textcoords="offset points", ha=ha, va="center",
                    fontsize=6.0, fontstyle="italic", color=MUDO, zorder=6, transform=ccrs.PlateCarree())

    def rotulo(x, y, off, ha, txt, tam, negrito):
        fig.text(x + off[0] / 72 / W, y + off[1] / 72 / H, txt, ha=ha, va="center", zorder=10,
                 fontsize=tam, fontweight="bold" if negrito else "normal", fontstyle="italic", color=CREME,
                 bbox=dict(fc=FUNDO, ec="none", alpha=0.8, pad=1.0))
    for chave, (npt, nde, lat, lon, off, ha) in LUGARES.items():
        x, y = em_fig(br, lon, lat)
        fig.add_artist(plt.Line2D([x], [y], marker="o", ms=4.2, color=MUDO, mec=FUNDO, mew=0.6, zorder=8))
        rotulo(x, y, off, ha, npt if lang == "pt" else nde, 5.8, False)
    for chave, (nome, lat, lon, off, ha) in ENCONTROS.items():
        x, y = em_fig(br, lon, lat)
        fig.add_artist(plt.Line2D([x], [y], marker="o", ms=7.5 if chave == "floripa" else 5.8,
                                  color=CREME, mec=FUNDO, mew=0.8, zorder=9))
        rotulo(x, y, off, ha, nome, 7.4 if chave == "floripa" else 6.6, chave == "floripa")

    fig.text(0.06, 0.545, tit, fontsize=26, fontweight="bold", color=CREME, va="bottom", zorder=10)
    fig.text(0.06, 0.515, sub, fontsize=10.5, fontstyle="italic", color=MUDO, va="bottom", zorder=10)
    fig.text(0.06, 0.490, aut1 + "  ·  " + aut2, fontsize=8.6, color=CREME, va="bottom", zorder=10)
    for i, (cor, nome, _) in enumerate(RAMOS.values()):
        y = 0.425 - i * 0.022
        fig.lines.append(plt.Line2D([0.07, 0.11], [y, y], transform=fig.transFigure, color=cor, lw=2.2, zorder=10))
        fig.text(0.125, y, nome, fontsize=7.4, color=CREME, va="center", zorder=10,
                 bbox=dict(fc=TERRA, ec="none", alpha=0.7, pad=0.8))

    for ext in ("jpg", "pdf"):
        fig.savefig(IMG / f"capa_{lang}.{ext}", dpi=300, facecolor=FUNDO)
    plt.close(fig)
    print(IMG / f"capa_{lang}.jpg")


if __name__ == "__main__":
    for lang in ("pt", "de"):
        capa(lang)
