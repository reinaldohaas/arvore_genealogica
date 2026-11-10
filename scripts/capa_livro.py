"""Gera a capa do livro (15,5 x 23 cm, 300 dpi) em português e em alemão.

A capa é um mapa em três etapas, uma cor para cada avô ou avó de Matheus e Lucas:
1. de cada lugar de origem na Europa (Alemanha, Suíça, Hungria) ao lugar onde a
   família foi viver no Sul do Brasil;
2. desses lugares a Vidal Ramos (os ramos de Reinaldo) e a Joinville (os de Bárbara);
3. as vidas dos autores: Reinaldo nasceu em Vidal Ramos (1965) e vive em Florianópolis
   desde 1985; Bárbara nasceu em Porto Alegre (1972), cresceu em Joinville e foi para
   Florianópolis, onde os dois se casaram em 1995.

Uso: python scripts/capa_livro.py   ->  imagens/capa_pt.jpg/.pdf, capa_de.jpg/.pdf
"""
from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cf
import cartopy.io.shapereader as shp
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.path import Path as MPath

RAIZ = Path(__file__).resolve().parents[1]
IMG = RAIZ / "imagens"
FUNDO, TERRA, LINHA, OURO, CREME, MUDO = "#231a14", "#3a2d22", "#6b5843", "#d9a94e", "#f2e8d5", "#c8b89a"
# Duas cores, uma por lado da família: dourado para o de Reinaldo, lilás para o de Bárbara.
DOURADO, LILAS = "#e8b04a", "#c9a0f0"
OCEANO, DESTAQUE, AGUA = "#16303f", "#5c4833", "#6f97ad"   # mar, SC e RS, nomes dos mares
plt.rcParams.update({"font.family": "Palatino Linotype"})

# Os quatro ramos, um por avô ou avó dos meninos: cor, nome e onde o ramo se reúne.
# Avô em linha cheia, avó em linha tracejada.
RAMOS = {
    "baldoino": (DOURADO, "Baldoíno Haas", "vidal", "-"),
    "adelina": (DOURADO, "Adelina Doerner", "vidal", (0, (4, 2))),
    "carlos": (LILAS, "Carlos Heinz Funke", "joinville", "-"),
    "ilusca": (LILAS, "Ilusca Hoeveler", "joinville", (0, (4, 2))),
}
# (sobrenomes, lugar pt, lugar de, lat, lon, ramo, onde foram viver, deslocamento do rótulo, alinhamento)
ORIGENS = [
    ("Haas", "Leonberg", "Leonberg", 49.21, 12.10, "baldoino", "anitapolis", (6, -13), "left"),
    ("Meier · Voit", "Heumaden", "Heumaden", 49.62, 12.40, "baldoino", "anitapolis", (6, -4), "left"),
    ("Dörner", "Solingen", "Solingen", 51.17, 7.08, "adelina", "smartinho", (-6, -1), "right"),
    ("Eller", "Vestfália", "Westfalen", 51.72, 8.75, "adelina", "smartinho", (-5, 9), "right"),
    ("Preis · Loch · Michels · Arns", "Mosela e Hunsrück", "Mosel und Hunsrück", 49.85, 6.90, "adelina", "spedro", (-6, -5), "right"),
    ("Funke", "Glauchau", "Glauchau", 50.82, 12.54, "carlos", "joinville", (6, -2), "left"),
    ("Aenishaenslin", "Basel-Landschaft, Suíça", "Basel-Landschaft, Schweiz", 47.47, 7.87, "carlos", "joinville", (6, -3), "left"),
    ("Hoeveler", "Hungria", "Ungarn", 47.30, 19.30, "ilusca", "npetropolis", (0, 8), "center"),
    ("Lohmann", "Harderode", "Harderode", 52.03, 9.46, "ilusca", "estrela", (6, 10), "left"),
    ("Schnack · Wacker", "Schleswig", "Schleswig", 54.55, 9.57, "ilusca", "estrela", (6, 0), "left"),
    ("Wingert", "Albig", "Albig", 49.77, 8.13, "ilusca", "nhamburgo", (2, 9), "center"),
    ("Köhnlein · Lange", "Württemberg", "Württemberg", 49.25, 9.95, "ilusca", "tforquilhas", (-5, -10), "right"),
    ("Mentz", "Tambach", "Tambach", 50.79, 10.61, "ilusca", "nhamburgo", (5, 9), "left"),
]
# Onde foram viver (etapa 1): nome pt, nome de, lat, lon, deslocamento, alinhamento
LUGARES = {
    "anitapolis": ("Anitápolis", "Anitápolis", -27.90, -49.13, (-7, -2), "right"),
    "smartinho": ("São Martinho", "São Martinho", -28.16, -48.98, (7, -3), "left"),
    "spedro": ("São Pedro\nde Alcântara", "São Pedro\nde Alcântara", -27.57, -48.80, (-2, -12), "center"),
    # Wingert e Mentz: São Leopoldo (1824-1826), depois Hamburgo Velho; Lohmann e Schnack: Estrela
    # e Arroio do Meio; Hoeveler: Nova Petrópolis, onde Erno ensinou (a chegada da família não tem papel)
    "nhamburgo": ("Novo Hamburgo", "Novo Hamburgo", -29.68, -51.13, (8, -4), "left"),
    "estrela": ("Estrela e\nArroio do Meio", "Estrela und\nArroio do Meio", -29.45, -51.95, (-7, -2), "right"),
    "npetropolis": ("Nova Petrópolis", "Nova Petrópolis", -29.37, -51.11, (8, 3), "left"),
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
# Etapa 3, na legenda: o caminho de cada autor até Florianópolis
VIDAS = {
    "pt": ("Reinaldo: de Vidal Ramos (1965) a Florianópolis (desde 1985)",
           "Bárbara: de Porto Alegre (1972), por Joinville, a Florianópolis"),
    "de": ("Reinaldo: von Vidal Ramos (1965) nach Florianópolis (seit 1985)",
           "Bárbara: von Porto Alegre (1972) über Joinville nach Florianópolis"),
}


# Nomes no mapa: (pt, de, lon, lat). Países e mares em cor discreta, para situar sem competir com os fios.
PAISES = [("Portugal", "Portugal", -8.0, 39.5), ("Espanha", "Spanien", -3.8, 40.3), ("França", "Frankreich", 2.2, 46.7),
          ("Itália", "Italien", 12.6, 42.6), ("Alemanha", "Deutschland", 14.2, 52.8)]
MARES_EU = [("Oceano Atlântico", "Atlantischer Ozean", -6.5, 46.0), ("Mar Mediterrâneo", "Mittelmeer", 5.5, 38.6),
            ("Mar do Norte", "Nordsee", 3.6, 55.0)]
ESTADOS = [("SANTA CATARINA", "SANTA CATARINA", -50.9, -27.0), ("RIO GRANDE DO SUL", "RIO GRANDE DO SUL", -53.2, -30.45)]
MARES_BR = [("Oceano Atlântico", "Atlantischer Ozean", -48.9, -30.2)]


def base(ax, extent, estados=False):
    ax.set_extent(extent, ccrs.PlateCarree())
    ax.set_facecolor(OCEANO)
    ax.add_feature(cf.NaturalEarthFeature("physical", "land", "50m", facecolor=TERRA, edgecolor="none"))
    if estados:   # Santa Catarina e Rio Grande do Sul em destaque
        regs = [x for x in shp.Reader(shp.natural_earth("50m", "cultural", "admin_1_states_provinces")).records()
                if x.attributes.get("name") in ("Santa Catarina", "Rio Grande do Sul")]
        ax.add_geometries([x.geometry for x in regs], ccrs.PlateCarree(), facecolor=DESTAQUE,
                          edgecolor=MUDO, linewidth=0.8, zorder=1.55)   # a terra do cartopy fica em 1.5
    ax.add_feature(cf.NaturalEarthFeature("cultural", "admin_0_boundary_lines_land", "50m",
                                          facecolor="none", edgecolor=LINHA, linewidth=0.5, zorder=1.7))
    ax.add_feature(cf.NaturalEarthFeature("physical", "coastline", "50m", facecolor="none",
                                          edgecolor=LINHA, linewidth=0.6, zorder=1.7))
    for s in ax.spines.values():
        s.set_visible(False)


def capa(lang):
    tit, sub, aut1, aut2 = TEXTOS[lang]
    fig = plt.figure(figsize=(15.5 / 2.54, 23 / 2.54), facecolor=FUNDO)
    W, H = fig.get_size_inches()
    eu = fig.add_axes([0.04, 0.60, 0.92, 0.38], projection=ccrs.PlateCarree())
    base(eu, [-11.0, 22.0, 35.8, 55.6])
    br = fig.add_axes([0.04, 0.02, 0.92, 0.46], projection=ccrs.PlateCarree())
    base(br, [-54.6, -47.6, -31.0, -25.8], estados=True)
    def nome(ax, lon, lat, txt, cor, tam, estilo="italic", esp=0):
        ax.text(lon, lat, txt, transform=ccrs.PlateCarree(), ha="center", va="center", fontsize=tam,
                fontstyle=estilo, color=cor, zorder=1.8, alpha=0.95)
    k = 0 if lang == "pt" else 1
    for p in PAISES:
        nome(eu, p[2], p[3], p[k], MUDO, 6.6, "normal")
    for m in MARES_EU:
        nome(eu, m[2], m[3], m[k], AGUA, 7.0)
    for e in ESTADOS:
        nome(br, e[2], e[3], e[k], MUDO, 7.2, "normal")
    for m in MARES_BR:
        nome(br, m[2], m[3], m[k], AGUA, 7.4)
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

    def fio(p0, p3, cor, lw, alpha, z, c1=None, c2=None, ls="-", seta=6):
        c1 = c1 or ((2 * p0[0] + p3[0]) / 3, (2 * p0[1] + p3[1]) / 3)
        c2 = c2 or ((p0[0] + 2 * p3[0]) / 3, (p0[1] + 2 * p3[1]) / 3)
        caminho = MPath([p0, c1, c2, p3], [MPath.MOVETO, MPath.CURVE4, MPath.CURVE4, MPath.CURVE4])
        fig.patches.append(FancyArrowPatch(path=caminho, transform=fig.transFigure, arrowstyle="-|>",
                                           mutation_scale=seta, color=cor, lw=lw, ls=ls, alpha=alpha,
                                           zorder=z, shrinkA=0, shrinkB=3))

    # etapa 1: da Europa até onde foram viver, passando pelo Atlântico (à direita)
    for nomes, lpt, lde, lat, lon, ramo, lugar, _, _ in ORIGENS:
        p0 = em_fig(eu, lon, lat)
        p3 = ponto_br(lugar)
        fio(p0, p3, RAMOS[ramo][0], 0.9, 0.7, 1,
            (min(0.97, p0[0] + 0.30), p0[1] - 0.10), (0.97, p3[1] + 0.22), RAMOS[ramo][3], 5)
    # etapa 2: dos lugares onde viveram até Vidal Ramos ou Joinville
    feitos = set()
    for _, _, _, _, _, ramo, lugar, _, _ in ORIGENS:
        destino = RAMOS[ramo][2]
        if lugar == destino or (lugar, destino) in feitos:
            continue
        feitos.add((lugar, destino))
        a, b = ponto_br(lugar), ponto_br(destino)
        meio = ((a[0] + b[0]) / 2 - 0.02, (a[1] + b[1]) / 2 + 0.01)
        fio(a, b, RAMOS[ramo][0], 1.6, 0.95, 2, meio, meio, RAMOS[ramo][3], 8)
    # etapa 3: Reinaldo, de Vidal Ramos (onde nasceu) a Florianópolis (desde 1985);
    # Bárbara, de Porto Alegre (onde nasceu) a Joinville (onde cresceu) e a Florianópolis
    vr, jv, pa, fl = (ponto_br(k) for k in ("vidal", "joinville", "poa", "floripa"))
    fio(vr, fl, DOURADO, 3.4, 1, 4, (vr[0] + 0.04, vr[1] + 0.035), (fl[0] - 0.06, fl[1] + 0.035), seta=13)
    fio(pa, jv, LILAS, 3.4, 1, 4, (pa[0] + 0.08, pa[1] + 0.18), (jv[0] - 0.17, jv[1] - 0.10), seta=13)
    fio(jv, fl, LILAS, 3.4, 1, 4, (jv[0] + 0.07, jv[1] - 0.05), (fl[0] + 0.05, fl[1] + 0.07), seta=13)

    for nomes, lpt, lde, lat, lon, ramo, lugar, off, ha in ORIGENS:
        eu.plot(lon, lat, "o", ms=4.6, color=RAMOS[ramo][0], mec=FUNDO, mew=0.6, transform=ccrs.PlateCarree(), zorder=5)
        nome_lugar = lpt if lang == "pt" else lde
        eu.annotate(f"{nomes}\n", (lon, lat), xytext=off, textcoords="offset points", ha=ha, va="center",
                    fontsize=5.9, fontweight="bold", color=CREME, zorder=6,
                    bbox=dict(fc=FUNDO, ec="none", alpha=0.55, pad=0.6), transform=ccrs.PlateCarree())
        eu.annotate(f"\n{nome_lugar}", (lon, lat), xytext=off, textcoords="offset points", ha=ha, va="center",
                    fontsize=5.3, fontstyle="italic", color=MUDO, zorder=6, transform=ccrs.PlateCarree())

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
    for i, (cor, nome, _, ls) in enumerate(RAMOS.values()):
        y = 0.425 - i * 0.022
        fig.lines.append(plt.Line2D([0.07, 0.11], [y, y], transform=fig.transFigure, color=cor, lw=1.8, ls=ls, zorder=10))
        fig.text(0.125, y, nome, fontsize=7.4, color=CREME, va="center", zorder=10,
                 bbox=dict(fc=TERRA, ec="none", alpha=0.7, pad=0.8))
    for i, (txt, cor) in enumerate(zip(VIDAS[lang], (DOURADO, LILAS))):
        y = 0.425 - (len(RAMOS) + i) * 0.022 - 0.006
        fig.patches.append(FancyArrowPatch((0.07, y), (0.112, y), transform=fig.transFigure, arrowstyle="-|>",
                                           mutation_scale=10, color=cor, lw=3.0, zorder=10))
        fig.text(0.125, y, txt, fontsize=7.0, color=CREME, va="center", zorder=10,
                 bbox=dict(fc=TERRA, ec="none", alpha=0.7, pad=0.8))

    for ext in ("jpg", "pdf"):
        fig.savefig(IMG / f"capa_{lang}.{ext}", dpi=300, facecolor=FUNDO)
    plt.close(fig)
    print(IMG / f"capa_{lang}.jpg")


if __name__ == "__main__":
    for lang in ("pt", "de"):
        capa(lang)
