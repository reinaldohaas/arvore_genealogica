"""Gera os mapas do livro em imagens/ (mapa_*.png). Dados: Natural Earth (cartopy) e IBGE/HEC-RAS locais."""
import json
import os
from pathlib import Path

os.environ.setdefault("USERPROFILE", r"C:\Users\haas")
os.environ.setdefault("HOME", r"C:\Users\haas")

import cartopy.crs as ccrs
import cartopy.feature as cf
import cartopy.io.shapereader as sr
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "imagens"
HEC = Path(r"C:/Users/haas/github/hecras_vale")

TERRA, MAR, LIMITE, TEXTO = "#efe8d8", "#d6e4ea", "#a89f8c", "#2b2620"
HAAS, DOER, BARB, ROTA = "#a4361f", "#1f5d7a", "#5d7a1f", "#7a1f5d"
plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 9, "text.color": TEXTO})
PC = ccrs.PlateCarree()


def base(ext, tam, res="10m"):
    fig = plt.figure(figsize=tam)
    ax = fig.add_subplot(projection=PC)
    ax.set_extent(ext, PC)
    ax.set_facecolor(MAR)
    ax.add_feature(cf.NaturalEarthFeature("physical", "land", res, facecolor=TERRA, edgecolor="none"))
    ax.add_feature(cf.NaturalEarthFeature("cultural", "admin_0_boundary_lines_land", res,
                                          facecolor="none", edgecolor=LIMITE, linewidth=0.8))
    ax.add_feature(cf.NaturalEarthFeature("physical", "coastline", res, facecolor="none",
                                          edgecolor="#8a8474", linewidth=0.5))
    return fig, ax


def ponto(ax, lon, lat, nome, cor=TEXTO, dx=0.0, dy=0.0, ha="left", peso="normal", tam=8.5):
    ax.plot(lon, lat, "o", ms=4.5, color=cor, mec="white", mew=0.5, transform=PC, zorder=5)
    ax.text(lon + dx, lat + dy, nome, ha=ha, va="center", color=cor, fontsize=tam, fontweight=peso,
            transform=PC, zorder=6)


def legenda(ax, itens, loc="lower right"):
    for cor, txt in itens:
        ax.plot([], [], "o", color=cor, label=txt)
    ax.legend(loc=loc, fontsize=7.5, framealpha=0.9, facecolor="white", edgecolor=LIMITE)


def fechar(fig, ax, nome, titulo):
    ax.set_title(titulo, fontsize=11, fontweight="bold", loc="left")
    fig.savefig(SAIDA / nome, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(nome)


def estados(ax, nomes, res="10m", cor=LIMITE):
    leitor = sr.Reader(sr.natural_earth(resolution=res, category="cultural", name="admin_1_states_provinces"))
    for reg in leitor.records():
        if reg.attributes.get("name") in nomes and reg.attributes.get("admin") == "Brazil":
            ax.add_geometries([reg.geometry], PC, facecolor="none", edgecolor=cor, linewidth=0.8, zorder=2)


def rios_geojson(ax, arquivo, cor="#5b8fb0", lw=0.7):
    with open(arquivo, encoding="utf-8") as f:
        dados = json.load(f)
    for ft in dados["features"]:
        g = ft["geometry"]
        if not g:
            continue
        linhas = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
        for l in linhas:
            xs = [p[0] for p in l]
            ys = [p[1] for p in l]
            if abs(xs[0]) > 180:  # coordenadas projetadas: ignora
                return False
            ax.plot(xs, ys, color=cor, lw=lw, transform=PC, zorder=3)
    return True


# 1 ---------------------------------------------------------------- Europa
fig, ax = base([3.5, 16.0, 43.0, 55.2], (7.2, 8.4))
for lon, lat, n, c, dx, dy, ha in [
    (10.91, 47.99, "Stoffen\n(Josef Haas, 1847)", HAAS, 0.18, 0, "left"),
    (12.09, 49.20, "Leonberg, hoje Maxhütte-Haidhof\n(Johann Haas, 1884)", HAAS, -0.15, -0.28, "right"),
    (12.41, 49.60, "Heumaden e Moosbach\n(Maria Meier, 1888)", HAAS, 0.18, 0, "left"),
    (12.60, 50.49, "Eibenstock\n(casamento, 1907)", HAAS, 0.18, -0.08, "left"),
    (12.92, 50.83, "Chemnitz (1913?)", HAAS, 0.18, 0.12, "left"),
    (12.37, 50.48, "Falkenstein\n(as cartas)", HAAS, -0.15, 0, "right"),
    (7.08, 51.17, "Solingen (Dörner?)", DOER, 0.18, 0, "left"),
    (6.75, 49.82, "Schweich (Preis e Loch)", DOER, -0.15, -0.1, "right"),
    (6.95, 49.66, "Hermeskeil (Michels)", DOER, -0.15, -0.38, "right"),
    (7.13, 50.04, "Pünderich (Arns)", DOER, 0.18, 0, "left"),
    (12.54, 50.82, "Glauchau (Funke)", BARB, -0.1, 0.28, "right"),
    (9.56, 51.97, "Região de Holzminden (Lohmann)", BARB, 0.18, 0, "left"),
    (9.60, 54.50, "Schleswig (Schnack)", BARB, 0.18, 0, "left"),
    (7.87, 47.47, "Ormalingen (Aenishaenslin)", BARB, -0.15, -0.3, "right"),
    (5.37, 43.30, "Marselha (embarque, 1913)", ROTA, 0.18, 0.15, "left"),
]:
    ponto(ax, lon, lat, n, c, dx, dy, ha)
legenda(ax, [(HAAS, "Haas e Meier"), (DOER, "Dörner, Preis, Michels, Arns"), (BARB, "ramos de Bárbara"), (ROTA, "porto")], "lower right")
fechar(fig, ax, "mapa_europa_origens.png", "De onde vieram")

# 2 ---------------------------------------------------------------- Viagem
fig, ax = base([-58, 24, -34, 54], (7.6, 8.0), "50m")
rota = [(5.37, 43.30), (1.5, 39.0), (-5.8, 36.0), (-10.5, 33), (-16.5, 26), (-20, 15), (-26, 2), (-33, -8), (-37, -15), (-40.5, -23.6), (-43.15, -22.95)]
ax.plot(*zip(*rota), "--", color=ROTA, lw=1.4, transform=PC, zorder=4)
costa = [(-43.15, -22.95), (-46.3, -24.4), (-48.5, -27.6)]
ax.plot(*zip(*costa), ":", color=HAAS, lw=1.6, transform=PC, zorder=4)
ponto(ax, 12.1, 49.2, "Baviera", HAAS, 0.8, 0)
ponto(ax, 12.92, 50.83, "Chemnitz?", HAAS, 0.8, 0.5)
ax.plot([12.92, 5.37], [50.83, 43.30], ":", color=HAAS, lw=1.2, transform=PC)
ponto(ax, 5.37, 43.30, "Marselha", ROTA, 0.9, -0.6, peso="bold")
ponto(ax, -43.15, -22.95, "Rio de Janeiro\n26 de março de 1913", ROTA, 6.0, -1.2, peso="bold")
ponto(ax, -48.5, -27.6, "Santa Catarina\n(Florianópolis ou Laguna?)", HAAS, 1.0, -1.8)
ax.text(-27, 17, "Vapor Formosa\ntraçado esquemático", fontsize=8, style="italic", color=ROTA, transform=PC, ha="center")
fechar(fig, ax, "mapa_viagem_1913.png", "A viagem de 1913")

# 3 ---------------------------------------------------------------- Sul do Brasil
fig, ax = base([-54.5, -47.6, -31.0, -23.4], (6.6, 7.6))
estados(ax, {"Paraná", "Santa Catarina", "Rio Grande do Sul"})
for lon, lat, n, c, dx, dy, ha in [
    (-51.68, -24.25, "Ivaiporã (Gertrudes Haas)", HAAS, 0.1, 0, "left"),
    (-52.03, -23.30, "", HAAS, 0, 0, "left"),
    (-48.85, -26.30, "Joinville (Funke)", BARB, -0.1, 0, "right"),
    (-48.55, -27.60, "Florianópolis", ROTA, -0.1, 0, "right"),
    (-49.60, -27.41, "Ituporanga", HAAS, -0.1, 0, "right"),
    (-49.13, -27.90, "Anitápolis", HAAS, -0.1, 0.0, "right"),
    (-48.98, -28.16, "São Martinho", DOER, -0.1, 0, "right"),
    (-48.92, -27.10, "Brusque", DOER, -0.1, 0.05, "right"),
    (-51.96, -29.50, "Estrela", BARB, -0.1, 0, "right"),
    (-51.95, -29.38, "Arroio do Meio", BARB, -0.1, 0.05, "right"),
    (-51.23, -30.03, "Porto Alegre", TEXTO, 0.1, 0, "left"),
]:
    if n:
        ponto(ax, lon, lat, n, c, dx, dy, ha)
for lon, lat, n in [(-51.6, -24.9, "PARANÁ"), (-51.0, -27.2, "SANTA CATARINA"), (-53.3, -29.9, "RIO GRANDE\nDO SUL")]:
    ax.text(lon, lat, n, fontsize=9, color="#8a8474", ha="center", transform=PC)
legenda(ax, [(HAAS, "Haas"), (DOER, "Doerner e Preis"), (BARB, "ramos de Bárbara")], "lower right")
fechar(fig, ax, "mapa_sul_do_brasil.png", "Onde a família se espalhou")

# 4 ---------------------------------------------------------------- SC central
fig, ax = base([-50.1, -48.2, -28.75, -26.6], (6.8, 7.6))
estados(ax, {"Santa Catarina"})
for arq in ("rios_itajai_unificados.geojson", "rios_itajai_mirin.geojson", "rios_tubarao.geojson", "rios_tijucas.geojson"):
    if (HEC / arq).exists():
        print(arq, rios_geojson(ax, HEC / arq))
for lon, lat, n, c, dx, dy, ha in [
    (-48.55, -27.60, "Florianópolis\n(antiga Desterro)", ROTA, 0.05, 0.0, "left"),
    (-48.80, -27.57, "São Pedro de Alcântara\n(1828)", DOER, -0.04, 0.06, "right"),
    (-48.82, -27.70, "Águas Mornas\n(antiga Teresópolis)", DOER, -0.04, -0.05, "right"),
    (-48.93, -27.90, "São Bonifácio", DOER, 0.04, 0, "left"),
    (-49.13, -27.90, "Anitápolis, Rio do Ouro\n(1913–1918)", HAAS, -0.04, 0, "right"),
    (-48.98, -28.16, "São Martinho, Vargem do Cedro", DOER, 0.04, 0, "left"),
    (-48.82, -28.34, "Imaruí", DOER, 0.04, 0, "left"),
    (-48.78, -28.48, "Laguna", ROTA, 0.04, 0, "left"),
    (-49.01, -28.47, "Tubarão", TEXTO, -0.04, 0, "right"),
    (-49.33, -27.70, "Alfredo Wagner, Catuíra", HAAS, -0.04, -0.07, "right"),
    (-49.60, -27.41, "Ituporanga", HAAS, -0.04, 0, "right"),
    (-49.63, -27.31, "Aurora", HAAS, -0.04, 0.02, "right"),
    (-49.36, -27.39, "Vidal Ramos", DOER, 0.04, -0.02, "left"),
    (-48.92, -27.10, "Brusque", DOER, 0.04, 0, "left"),
    (-49.07, -26.92, "Blumenau", TEXTO, 0.04, 0, "left"),
    (-48.66, -26.91, "Itajaí", TEXTO, 0.04, 0, "left"),
]:
    ponto(ax, lon, lat, n, c, dx, dy, ha)
legenda(ax, [(HAAS, "Haas"), (DOER, "Dörner, Preis, Michels, Arns"), (ROTA, "portos"), (TEXTO, "referências")], "lower left")
fechar(fig, ax, "mapa_santa_catarina.png", "Santa Catarina da família")
