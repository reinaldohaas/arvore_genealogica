"""Gera as árvores do livro em imagens/ (arvore_*.png): nascimento, morte, casamento e partida.

Dados conferidos nos capítulos, nas certidões e no GEDCOM privado. Pessoas vivas só com o ano ou sem data.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SAIDA = Path(__file__).resolve().parents[1] / "imagens"
plt.rcParams.update({"font.family": "DejaVu Serif"})
TINTA, FUNDO, BORDA = "#2b2620", "#f7f2e6", "#a89f8c"
CASA, NAVIO = "#a4361f", "#1f5d7a"


def P(nome, *linhas, navio=None):
    return {"nome": nome, "linhas": list(linhas), "navio": navio}


def caixa(ax, x, y, w, h, p):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.008",
                                fc=FUNDO, ec=BORDA, lw=0.7, zorder=2))
    linhas = [(p["nome"], TINTA, "bold")] + [(l, TINTA, "normal") for l in p["linhas"]]
    if p["navio"]:
        linhas.append((p["navio"], NAVIO, "bold"))
    passo = h / (len(linhas) + 0.6)
    for i, (t, c, fw) in enumerate(linhas):
        ax.text(x + 0.006, y + h - passo * (i + 0.8), t, fontsize=6.6 if i else 7.1, color=c, fontweight=fw,
                va="center", ha="left", zorder=3)


def arvore(nome, titulo, raiz, casal_raiz, geracoes, casamentos, rodape):
    """geracoes[g] tem 2^(g+1) pessoas; casamentos[g] tem um texto para cada casal da geração g."""
    fig = plt.figure(figsize=(8.3, 11.0))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.01, 0.985, titulo, fontsize=14, fontweight="bold", color=TINTA, va="top")
    topo, fundo = 0.945, 0.055
    n = len(geracoes)
    larg = (0.99 - 0.17) / n - 0.012
    folhas = 2 ** n
    alt = (topo - fundo) / folhas
    def yc(g, i):  # centro da pessoa i na geração g
        bloco = folhas // (2 ** (g + 1))
        return topo - alt * bloco * (i + 0.5)
    xg = lambda g: 0.17 + g * (larg + 0.012)
    h_caixa = [0.085, 0.078, 0.064, alt * 0.93]
    # raiz
    yr = (yc(0, 0) + yc(0, 1)) / 2
    caixa(ax, 0.01, yr - 0.05, 0.145, 0.10, raiz)
    ax.plot([0.155, xg(0) - 0.004], [yr, yr], color=BORDA, lw=0.8)
    ax.text(0.01, yr + 0.06, casal_raiz, fontsize=6.5, color=CASA, fontweight="bold", va="bottom")
    for g, pessoas in enumerate(geracoes):
        hc = h_caixa[min(g, 3)] if n == 4 else alt * 0.9
        for i, p in enumerate(pessoas):
            y = yc(g, i)
            caixa(ax, xg(g), y - hc / 2, larg, hc, p)
        for c in range(len(pessoas) // 2):
            y1, y2 = yc(g, 2 * c), yc(g, 2 * c + 1)
            ax.plot([xg(g) - 0.005] * 2, [y1, y2], color=BORDA, lw=0.8, zorder=1)
            for yy in (y1, y2):
                ax.plot([xg(g) - 0.005, xg(g)], [yy, yy], color=BORDA, lw=0.8, zorder=1)
            if g > 0:
                ax.plot([xg(g) - 0.012 - 0.002, xg(g) - 0.005], [(y1 + y2) / 2] * 2, color=BORDA, lw=0.8, zorder=1)
            txt = casamentos[g][c]
            if txt:
                ax.text(xg(g) + 0.006, (y1 + y2) / 2, txt, fontsize=5.9, color=CASA, va="center", ha="left",
                        fontweight="bold", zorder=4,
                        bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    ax.text(0.01, 0.022, rodape, fontsize=6.2, color=TINTA, va="center", style="italic")
    fig.savefig(SAIDA / nome, dpi=220, facecolor="white")
    plt.close(fig)
    print(nome)


LEG = "n. nascimento   † morte   ∞ casamento   c. = cerca de.   ? = tradição, sem documento."

# ------------------------------------------------------------ lado Haas e Doerner
arvore(
    "arvore_haas_doerner.png",
    "A árvore do pai de Matheus e Lucas",
    P("Reinaldo Haas", "n. 1965, Vidal Ramos", "∞ 1995 Bárbara Funke", "filhos: Matheus e Lucas"),
    "",
    [
        [P("Baldoíno Haas", "n. 20/04/1924, Rio Novo", "† 18/12/2013, Ituporanga"),
         P("Adelina Doerner", "n. 30/10/1926, São Martinho", "† 22/02/2019, Vidal Ramos")],
        [P("Johann Haas, o Fata", "n. 11/07/1884, Leonberg", "† 19/03/1969", navio="chegou: Rio, 26/03/1913"),
         P("Maria Meier, a Mota", "n. 07/04/1888, Heumaden", "† 08/11/1973", navio="chegou: Rio, 26/03/1913"),
         P("Fernando Dörner", "n. 24/08/1897, São Martinho", "† 21/05/1981, Brusque"),
         P("Gertrudes Preiss", "n. 05/03/1896, São Martinho", "† 09/04/1970, Brusque")],
        [P("Josef Haas", "n. 19/05/1847, Stoffen"),
         P("Franziska Dengler", "Baviera"),
         P("Georg Adam Meier", "n. 09/03/1859, Heumaden"),
         P("Franziska Voit", "n. 29/06/1861, Burgtreswitz"),
         P("Carlos Dörner", "n. c. 1855, Europa"),
         P("Anna Eller", "n. c. 1858–60, † c. 1898"),
         P("Emanuel Preis", "n. 31/03/1864", "† 27/03/1927"),
         P("Helena Michels", "n. 01/01/1864", "† 08/06/1945")],
        [P("Georg Haas", "oleiro, Stoffen"), P("Maria Anna Albrecht", "Stoffen"),
         P("pai de Franziska", "a descobrir"), P("mãe de Franziska", "a descobrir"),
         P("Michael Meier", "n. c. 1820, Heumaden"), P("Margaretha Pfannenstein", "n. c. 1825"),
         P("Johann Voit", "n. c. 1820, Burgtreswitz"), P("Barbara Woppmann", "n. c. 1825"),
         P("Guilherme Dörner", "Solingen?"), P("Joanna Lauterjung", "Solingen?"),
         P("Franz Adam Eller", "bat. 03/03/1832, Vestfália", navio="chegou: década de 1860"), P("Anna Maria Knopker", "Alemanha"),
         P("Bernard Preis", "n. 1827, Schweich", "† 11/10/1893"), P("Ignazia Loch", "n. c. 1828–30"),
         P("Anton Michels", "n. 11/05/1822, Hermeskeil", "† 1874", navio="chegou: Desterro, 12/11/1828"),
         P("Angela C. Arns", "n. 05/12/1827, † 15/09/1924", navio="chegou: Desterro, 05/01/1847")],
    ],
    [
        ["∞ 1947 (igreja); 09/03/1948 (civil), Vidal Ramos"],
        ["∞ 03/08/1907, Eibenstock?", "∞ 09/07/1921 (igreja); 25/02/1923 (civil)"],
        ["", "∞ 23/11/1884, Moosbach", "∞ c. 1877; viúvo, ∞ 1900 Hulda Peters", ""],
        ["", "", "", "", "", "", "∞ 31/01/1855, São José", "∞ 1847"],
    ],
    LEG,
)

# ------------------------------------------------------------ lado Funke e Lohmann
arvore(
    "arvore_funke_lohmann.png",
    "A árvore da mãe de Matheus e Lucas",
    P("Bárbara Funke", "n. 1972", "∞ 1995 Reinaldo Haas", "filhos: Matheus e Lucas"),
    "",
    [
        [P("Dr. Carlos Heinz Funke", "n. 10/08/1939, Joinville", "† 29/05/1989"),
         P("Ilusca Leocádia Hoeveler", "Joinville")],
        [P("Oscar Martin Funke", "n. 01/12/1910, Glauchau", "† 21/07/1974", navio="veio da Saxônia: quando?"),
         P("Dora Marta Aenishaenslin", "n. 25/09/1914, Joinville", "† 03/09/2001"),
         P("Erno Hoeveler", "n. 1915 ou 1920?", "professor"),
         P("Rosita Érica Lohmann", "n. 1918", "† 2014, Joinville")],
        [P("Paulo Funke", "n. 19/06/1881, Glauchau"),
         P("Hulda", "n. 30/04/1889, Glauchau"),
         P("Jacques Aenishaenslin", "n. 25/07/1880, Suíça", "† 28/03/1946"),
         P("Frida Liechti", "n. 15/01/1884", "† 15/02/1958"),
         P("Walter Hoeveler", "a descobrir"),
         P("Frida", "a descobrir"),
         P("Francisco Jacob Lohmann", "n. 20/11/1889", "† 24/01/1975"),
         P("Miguelina Leocádia Endres", "n. 09/12/1891")],
        [P("pai de Paulo", "a descobrir"), P("mãe de Paulo", "a descobrir"),
         P("pai de Hulda", "a descobrir"), P("mãe de Hulda", "a descobrir"),
         P("Emil Aenishaenslin", "n. 26/08/1848, Ormalingen", "† 22/05/1909"), P("Maria Lidia Bussinger", "n. 22/05/1849", "† 22/02/1919"),
         P("pai de Frida Liechti", "a descobrir"), P("mãe de Frida Liechti", "a descobrir"),
         P("pai de Walter", "a descobrir"), P("mãe de Walter", "a descobrir"),
         P("pai de Frida", "a descobrir"), P("mãe de Frida", "a descobrir"),
         P("Friedrich Lohmann", "n. 18/02/1853", "† 31/01/1937"), P("Suzana Regina Schnack", "n. 09/07/1858", "† 16/12/1889"),
         P("pai de Miguelina", "a descobrir"), P("mãe de Miguelina", "a descobrir")],
    ],
    [
        [""],
        ["", ""],
        ["", "", "", "∞ 05/09/1914"],
        ["", "", "∞ 18/05/1874", "", "", "", "", ""],
    ],
    LEG + "\nFriedrich Lohmann é filho de Georg Karl (1821–1899) e Bárbara Wingert. Suzana é filha de Julius Georg Schnack, que chegou ao Brasil em 1851.",
)
