"""Gera a capa do livro (15,5 x 23 cm, 300 dpi) em português e em alemão.

A ideia da capa é a da retrotrajetória do prólogo: uma linha tracejada liga as
coordenadas de Heumaden, no alto, às de Florianópolis, embaixo, passando pela
fotografia de despedida de 7 de março de 1913.

Uso: python scripts/capa_livro.py   ->  imagens/capa_pt.jpg, capa_de.jpg (+ .pdf)
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

RAIZ = Path(__file__).resolve().parents[1]
IMG = RAIZ / "imagens"
DPI = 300
W, H = round(15.5 / 2.54 * DPI), round(23 / 2.54 * DPI)
FONTES = Path(r"C:\Windows\Fonts")
FUNDO, CREME, OURO, SOMBRA = (34, 26, 20), (240, 230, 210), (196, 160, 98), (20, 15, 11)

TEXTOS = {
    "pt": {"titulo": "Nossa Família", "sub": "Da Alemanha ao Sul do Brasil",
           "alto": "49,6° N · 12,4° L   Heumaden, 1888", "baixo": "Florianópolis, 2026   27,6° S · 48,5° O",
           "legenda": "Zum Andenken! vor unserer Abreise nach Brasilien, 7. März 1913"},
    "de": {"titulo": "Unsere Familie", "sub": "Von Deutschland in den Süden Brasiliens",
           "alto": "49,6° N · 12,4° O   Heumaden, 1888", "baixo": "Florianópolis, 2026   27,6° S · 48,5° W",
           "legenda": "Zum Andenken! vor unserer Abreise nach Brasilien, 7. März 1913"},
}


def fonte(nome, tam):
    return ImageFont.truetype(str(FONTES / nome), tam)


def centro(d, y, txt, f, cor):
    w = d.textlength(txt, font=f)
    d.text(((W - w) / 2, y), txt, font=f, fill=cor)


def espacado(d, y, txt, f, cor, esp):
    larg = sum(d.textlength(c, font=f) for c in txt) + esp * (len(txt) - 1)
    x = (W - larg) / 2
    for c in txt:
        d.text((x, y), c, font=f, fill=cor)
        x += d.textlength(c, font=f) + esp


def tracejado(d, pts, cor, larg, traco=22, vazio=16):
    acum, desenha = 0.0, True
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        pos = 0.0
        while pos < seg:
            lim = traco if desenha else vazio
            passo = min(lim - acum, seg - pos)
            if desenha:
                a, b = pos / seg, (pos + passo) / seg
                d.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a), (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)],
                       fill=cor, width=larg)
            pos += passo
            acum += passo
            if acum >= lim - 1e-6:
                acum, desenha = 0.0, not desenha


def bezier(p0, p1, p2, p3, n=200):
    out = []
    for i in range(n + 1):
        t = i / n
        out.append(tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * e
                         for a, b, c, e in zip(p0, p1, p2, p3)))
    return out


def capa(lang):
    T = TEXTOS[lang]
    im = Image.new("RGB", (W, H), FUNDO)
    # vinheta suave
    vin = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vin).ellipse((-W * 0.25, -H * 0.15, W * 1.25, H * 1.1), fill=255)
    vin = vin.filter(ImageFilter.GaussianBlur(260))
    claro = Image.new("RGB", (W, H), (52, 40, 30))
    im = Image.composite(claro, im, vin)
    d = ImageDraw.Draw(im)

    # fotografia de despedida, em sépia, com moldura creme e sombra
    foto = Image.open(IMG / "haas_despedida_abreise_brasilien_1913_restaurada.jpg").convert("L")
    foto = ImageOps.autocontrast(foto, cutoff=1)
    foto = ImageOps.colorize(foto, (28, 20, 12), (236, 222, 196))
    fw = int(W * 0.80)
    foto = foto.resize((fw, int(foto.height * fw / foto.width)), Image.LANCZOS)
    borda = 18
    fx, fy = (W - fw) // 2, int(H * 0.17)
    sombra = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sombra).rectangle((fx - borda + 14, fy - borda + 20, fx + fw + borda + 14, fy + foto.height + borda + 20), fill=170)
    sombra = sombra.filter(ImageFilter.GaussianBlur(28))
    im = Image.composite(Image.new("RGB", (W, H), SOMBRA), im, sombra)
    d = ImageDraw.Draw(im)

    # a retrotrajetória: de Heumaden (alto, à esquerda) a Florianópolis (embaixo, à direita)
    a0 = (int(W * 0.10), int(H * 0.085))
    a1 = (int(W * 0.90), int(H * 0.915))
    # desce pela margem esquerda, some atrás da foto (a viagem) e reaparece à direita
    tracejado(d, [a0, (a0[0], fy + 40)], OURO, 5)
    saida = (int(W * 0.88), fy + foto.height + borda)
    pts = bezier(saida, (int(W * 0.95), int(H * 0.50)), (int(W * 0.95), int(H * 0.78)), a1)
    tracejado(d, pts, OURO, 5)
    for (x, y) in (a0, a1):
        d.ellipse((x - 13, y - 13, x + 13, y + 13), outline=OURO, width=5)
        d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=OURO)

    d.rectangle((fx - borda, fy - borda, fx + fw + borda, fy + foto.height + borda), fill=CREME)
    im.paste(foto, (fx, fy))
    d = ImageDraw.Draw(im)

    f_coord = fonte("palai.ttf", 46)
    d.text((a0[0] + 34, a0[1] - 28), T["alto"], font=f_coord, fill=OURO)
    w = d.textlength(T["baixo"], font=f_coord)
    d.text((a1[0] - 34 - w, a1[1] - 28), T["baixo"], font=f_coord, fill=OURO)

    y = fy + foto.height + borda + 34
    centro(d, y, T["legenda"], fonte("palai.ttf", 40), (190, 176, 150))

    f_tit = fonte("palab.ttf", 200)
    centro(d, int(H * 0.60), T["titulo"], f_tit, CREME)
    centro(d, int(H * 0.60) + 250, T["sub"], fonte("palai.ttf", 84), (226, 210, 180))
    d.line((W * 0.38, int(H * 0.60) + 390, W * 0.62, int(H * 0.60) + 390), fill=OURO, width=3)
    espacado(d, int(H * 0.60) + 430, "REINALDO HAAS", fonte("pala.ttf", 60), CREME, 14)
    espacado(d, int(H * 0.60) + 520, "BÁRBARA FUNKE HAAS", fonte("pala.ttf", 60), CREME, 14)

    out = IMG / f"capa_{lang}.jpg"
    im.save(out, quality=92, dpi=(DPI, DPI))
    im.save(IMG / f"capa_{lang}.pdf", resolution=DPI)
    print(out)


if __name__ == "__main__":
    for lang in ("pt", "de"):
        capa(lang)
