"""
Gerador de arte (pixel art) da trilha "Meu Primeiro Jogo" - React + Phaser.
Desenha em "pixels lógicos" e amplia x2 (NEAREST) => visual pixel art nítido.

Convenções importantes (para as poses encaixarem entre si):
- Herói: canvas lógico 32x32. Os pés terminam SEMPRE na última linha (y=31),
  assim dá para usar origin (0.5, 1) no Phaser e o pé "colar" no chão.
- Inimigo (gosma): canvas 26x20, base do corpo em y=18.
- outline() não usa wrap: contorno nunca aparece do lado oposto da imagem.
"""
import os
import numpy as np
from PIL import Image
from math import sin, cos, pi, floor

S = 4   # escala dos SPRITES (personagens, itens, tiles) - 4 pixels reais por pixel lógico
SBG = 2 # escala dos FUNDOS de tela cheia (céu, nuvens, montanhas)

C = {
    "contorno":  (28, 34, 51, 255),
    "pele":      (244, 199, 158, 255),
    "pele2":     (216, 165, 122, 255),
    "cabelo":    (74, 47, 27, 255),
    "cabelo2":   (56, 34, 18, 255),
    "blusa":     (58, 123, 213, 255),
    "blusa2":    (42, 90, 160, 255),
    "blusa3":    (30, 68, 124, 255),
    "calca":     (47, 58, 86, 255),
    "calca2":    (35, 44, 66, 255),
    "tenis":     (224, 90, 58, 255),
    "tenis2":    (184, 68, 42, 255),
    "branco":    (255, 255, 255, 255),
    "preto":     (28, 34, 51, 255),
    "verde":     (126, 217, 87, 255),
    "verde2":    (79, 168, 50, 255),
    "verde3":    (46, 107, 30, 255),
    "dourado":   (255, 210, 63, 255),
    "dourado2":  (224, 168, 0, 255),
    "dourado3":  (176, 128, 0, 255),
    "vermelho":  (233, 75, 75, 255),
    "vermelho2": (184, 48, 47, 255),
    "grama":     (126, 200, 80, 255),
    "grama2":    (90, 168, 60, 255),
    "grama3":    (64, 128, 44, 255),
    "terra":     (169, 113, 63, 255),
    "terra2":    (139, 90, 47, 255),
    "terra3":    (110, 70, 36, 255),
    "pedra":     (201, 183, 156, 255),
    "pedra2":    (170, 150, 122, 255),
}

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "art_out")


class Pixel:
    """Tela de pixels lógicos com fundo transparente."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.a = np.zeros((h, w, 4), dtype=np.uint8)

    def _put(self, x, y, c):
        x, y = int(x), int(y)
        if 0 <= x < self.w and 0 <= y < self.h:
            self.a[y, x] = c

    def rect(self, x, y, w, h, c):
        for yy in range(int(round(y)), int(round(y + h))):
            for xx in range(int(round(x)), int(round(x + w))):
                self._put(xx, yy, c)

    def ellipse(self, cx, cy, rx, ry, c):
        for yy in range(int(cy - ry), int(cy + ry) + 1):
            for xx in range(int(cx - rx), int(cx + rx) + 1):
                dx = (xx - cx) / rx if rx else 0
                dy = (yy - cy) / ry if ry else 0
                if dx * dx + dy * dy <= 1.0:
                    self._put(xx, yy, c)

    def blend_ellipse(self, cx, cy, rx, ry, c, alpha):
        """Elipse translúcida: mistura com o que já existe (halos e brilhos)."""
        for yy in range(int(cy - ry), int(cy + ry) + 1):
            for xx in range(int(cx - rx), int(cx + rx) + 1):
                if not (0 <= xx < self.w and 0 <= yy < self.h):
                    continue
                dx = (xx - cx) / rx if rx else 0
                dy = (yy - cy) / ry if ry else 0
                if dx * dx + dy * dy > 1.0:
                    continue
                dst = self.a[yy, xx].astype(float)
                if dst[3] == 0:
                    continue
                nova = dst[:3] * (1 - alpha) + np.array(c[:3]) * alpha
                self.a[yy, xx] = [int(nova[0]), int(nova[1]), int(nova[2]), int(dst[3])]

    def mask(self):
        return self.a[..., 3] > 0

    def outline(self, c=None):
        """Contorno de 1px em volta da silhueta (sem wrap-around nas bordas)."""
        c = c or C["contorno"]
        m = self.mask()
        pad = np.pad(m, 1, constant_values=False)
        d = np.zeros_like(m)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                d |= pad[1 + dy:1 + dy + self.h, 1 + dx:1 + dx + self.w]
        self.a[d & ~m] = c
        return self

    def to_image(self, scale=S):
        return Image.fromarray(self.a, "RGBA").resize((self.w * scale, self.h * scale), Image.NEAREST)


def save(img, name):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    img.save(p, optimize=True)
    print(f"  {name}  {img.size[0]}x{img.size[1]}")


def sheet(frames, nome, scale=S):
    """Junta os frames lado a lado em um spritesheet horizontal."""
    w, h = frames[0].w, frames[0].h
    img = Image.new("RGBA", (w * scale * len(frames), h * scale), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        img.alpha_composite(f.to_image(scale), (i * w * scale, 0))
    save(img, nome)


# ==========================================================================
# HERÓI (Milo) - canvas 32x32, pés na linha y=31
# ==========================================================================
def heroi(pose="parado", frame=0):
    p = Pixel(32, 32)

    # ------- deslocamento vertical: só a cabeca "respira" no parado
    cabeca_dy = 0
    if pose == "parado" and frame == 1:
        cabeca_dy = 1
    if pose == "pulando":
        cabeca_dy = -1

    # ---------------- CABEÇA (linhas 1..13) ----------------
    hy = cabeca_dy
    p.ellipse(16, 7 + hy, 7, 6.4, C["pele"])          # rosto
    p.rect(9, 1 + hy, 14, 5, C["cabelo"])             # topo do cabelo
    p.rect(9, 5 + hy, 14, 2, C["cabelo"])             # franja
    p.rect(9, 7 + hy, 2, 4, C["cabelo"])              # costeleta esquerda
    p.rect(21, 7 + hy, 2, 4, C["cabelo"])             # costeleta direita
    p.rect(10, 1 + hy, 12, 1, C["cabelo2"])           # sombra/volume do cabelo

    # orelhas
    p.rect(9, 8 + hy, 1, 2, C["pele2"])
    p.rect(22, 8 + hy, 1, 2, C["pele2"])

    # ---------------- OLHOS ----------------
    if pose == "dano":
        p.rect(12, 8 + hy, 3, 1, C["preto"])          # olhos fechados (tonto)
        p.rect(18, 8 + hy, 3, 1, C["preto"])
        p.rect(12, 9 + hy, 1, 1, C["preto"])
        p.rect(20, 9 + hy, 1, 1, C["preto"])
    else:
        p.rect(12, 7 + hy, 3, 4, C["branco"])
        p.rect(18, 7 + hy, 3, 4, C["branco"])
        p.rect(13, 8 + hy, 2, 2, C["preto"])          # pupila
        p.rect(19, 8 + hy, 2, 2, C["preto"])
        p.rect(13, 8 + hy, 1, 1, C["branco"])         # brilho no olho

    # bochechas e boca
    p.rect(11, 11 + hy, 2, 1, C["pele2"])
    p.rect(20, 11 + hy, 2, 1, C["pele2"])
    if pose == "dano":
        p.rect(14, 12 + hy, 5, 1, C["pele2"])         # boca aberta
        p.rect(15, 13 + hy, 3, 1, C["preto"])
    else:
        p.rect(15, 12 + hy, 3, 1, C["pele2"])

    # ---------------- TRONCO (linhas 14..22) ----------------
    p.rect(11, 14, 10, 9, C["blusa"])
    p.rect(15, 14, 1, 9, C["blusa2"])                 # divisão do casaco
    p.rect(11, 20, 10, 2, C["calca"])                 # cinto
    p.rect(15, 20, 2, 2, C["dourado"])                # fivela
    p.rect(11, 14, 10, 1, C["blusa2"])                # ombro/ombro sombra
    p.rect(11, 15, 1, 5, C["blusa3"])                 # sombra lateral

    # ---------------- BRAÇOS ----------------
    if pose == "correndo":
        sw = [(-3, 2), (0, 0), (3, -2), (0, 0)][frame]
        p.rect(8, 15 + sw[0], 3, 4, C["blusa"])       # esquerdo
        p.rect(8, 19 + sw[0], 3, 3, C["pele"])
        p.rect(21, 15 + sw[1], 3, 4, C["blusa"])      # direito
        p.rect(21, 19 + sw[1], 3, 3, C["pele"])
    elif pose == "pulando":
        p.rect(7, 10, 3, 4, C["pele"])                # braços levantados
        p.rect(8, 13, 3, 4, C["blusa"])
        p.rect(22, 10, 3, 4, C["pele"])
        p.rect(21, 13, 3, 4, C["blusa"])
    elif pose == "dano":
        p.rect(6, 12, 3, 4, C["blusa"])
        p.rect(6, 15, 3, 3, C["pele"])
        p.rect(23, 12, 3, 4, C["blusa"])
        p.rect(23, 15, 3, 3, C["pele"])
    else:
        dy = 1 if (pose == "parado" and frame == 1) else 0
        p.rect(8, 15 + dy, 3, 4, C["blusa"])
        p.rect(8, 19 + dy, 3, 3, C["pele"])
        p.rect(21, 15 + dy, 3, 4, C["blusa"])
        p.rect(21, 19 + dy, 3, 3, C["pele"])

    # ---------------- PERNAS (23..27) + TÊNIS (28..31) ----------------
    if pose == "correndo":
        # f0: esquerda na frente; f1: passos curtos; f2: direita na frente; f3: passos curtos
        pernas = [
            {"e": (13, 23, 4, 5), "d": (17, 23, 4, 4), "te": (12, 28, 5, 3), "td": (18, 28, 5, 3)},
            {"e": (13, 23, 3, 4), "d": (16, 23, 3, 4), "te": (12, 27, 5, 3), "td": (17, 27, 5, 3)},
            {"e": (11, 23, 4, 4), "d": (15, 23, 4, 5), "te": (11, 28, 5, 3), "td": (17, 28, 5, 3)},
            {"e": (13, 23, 3, 4), "d": (16, 23, 3, 4), "te": (12, 27, 5, 3), "td": (17, 27, 5, 3)},
        ][frame]
        p.rect(*pernas["e"], C["calca"])
        p.rect(*pernas["d"], C["calca"])
        p.rect(*pernas["te"], C["tenis"])
        p.rect(*pernas["td"], C["tenis"])
        p.rect(pernas["te"][0], pernas["te"][1] + 2, pernas["te"][2], 1, C["tenis2"])
        p.rect(pernas["td"][0], pernas["td"][1] + 2, pernas["td"][2], 1, C["tenis2"])
    elif pose == "pulando":
        # pernas encolhidas (personagem está no ar)
        p.rect(11, 23, 4, 5, C["calca"])
        p.rect(17, 22, 4, 6, C["calca"])
        p.rect(10, 27, 5, 3, C["tenis"])
        p.rect(17, 28, 5, 4, C["tenis"])
        p.rect(10, 29, 5, 1, C["tenis2"])
        p.rect(17, 31, 5, 1, C["tenis2"])
    elif pose == "dano":
        p.rect(10, 23, 4, 5, C["calca"])
        p.rect(18, 23, 4, 5, C["calca"])
        p.rect(9, 28, 5, 4, C["tenis"])
        p.rect(18, 28, 5, 4, C["tenis"])
        p.rect(9, 31, 5, 1, C["tenis2"])
        p.rect(18, 31, 5, 1, C["tenis2"])
    else:
        p.rect(12, 23, 3, 5, C["calca"])
        p.rect(17, 23, 3, 5, C["calca"])
        p.rect(11, 28, 5, 3, C["tenis"])
        p.rect(17, 28, 5, 3, C["tenis"])
        p.rect(11, 30, 11, 1, C["tenis2"])
        p.rect(12, 31, 10, 1, C["calca2"])            # sombra de contato com o chão

    p.outline()
    return p


# ==========================================================================
# INIMIGO (Gosma) - canvas 26x20, base em y=18
# ==========================================================================
def gosma(frame=0, derrotada=False):
    p = Pixel(26, 20)
    if derrotada:
        larg = 21 - frame * 7
        p.ellipse(13, 16, larg / 2, 3 - frame * 0.9, C["verde"])
        p.ellipse(10, 16, 2, 1, C["verde2"])
        p.outline()
        return p

    squash = [0, 2, 0, 2][frame]        # "respira": achata e estica
    cy = 12 + squash * 0.7
    ry = 7.2 - squash * 0.55

    p.ellipse(13, cy, 10.5, ry, C["verde"])                    # corpo
    p.rect(2.5, cy, 21, 18 - cy, C["verde"])                   # barriga até a base
    p.ellipse(13, 17.5, 10, 1.6, C["verde2"])                  # sombra na base
    p.blend_ellipse(9, cy - 3.5, 4, 2, C["branco"], 0.55)      # brilho (gelatina)

    p.ellipse(9, cy - 0.5, 3, 3, C["branco"])                  # olhos
    p.ellipse(17, cy - 0.5, 3, 3, C["branco"])
    p.rect(9, cy - 0.5, 2, 2, C["preto"])                      # pupilas
    p.rect(17, cy - 0.5, 2, 2, C["preto"])
    p.rect(9, cy - 0.5, 1, 1, C["branco"])
    p.rect(17, cy - 0.5, 1, 1, C["branco"])

    p.rect(11, cy + 3, 4, 1, C["verde3"])                      # boca
    p.rect(10, cy + 2.5, 1, 1, C["verde3"])
    p.rect(15, cy + 2.5, 1, 1, C["verde3"])

    p.rect(3, 16, 2, 2, C["verde2"])                           # gotas
    p.rect(21, 15, 2, 2, C["verde2"])
    p.outline()
    return p


# ==========================================================================
# ITENS
# ==========================================================================
def moeda(frame):
    p = Pixel(16, 16)
    largura = [6.5, 4.5, 1.5, 4.5][frame]     # gira: larga -> fina -> larga
    p.ellipse(8, 8, largura, 6.5, C["dourado"])
    p.ellipse(8, 8, max(0.8, largura - 2), 4.5, C["dourado2"])
    if frame in (0, 3):
        p.rect(6, 3, 2, 9, C["dourado"])
        p.rect(7, 4, 1, 7, C["dourado3"])
    p.blend_ellipse(6, 5, 2, 2, C["branco"], 0.7)
    p.outline(C["dourado3"])
    return p


def estrela():
    p = Pixel(16, 16)
    pts = [(8, 0.6), (10, 5.8), (15.4, 5.8), (11, 9.4), (12.6, 14.6),
           (8, 11.4), (3.4, 14.6), (5, 9.4), (0.6, 5.8), (6, 5.8)]
    for y in range(16):
        xs = []
        for i in range(len(pts)):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % len(pts)]
            if (y1 <= y < y2) or (y2 <= y < y1):
                xs.append(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
        xs.sort()
        for i in range(0, len(xs) - 1, 2):
            for x in range(int(floor(xs[i])), int(floor(xs[i + 1])) + 1):
                p._put(x, y, C["dourado"])
    p.rect(7, 2, 2, 2, C["branco"])
    p.rect(6, 3, 2, 1, C["branco"])
    p.rect(10, 7, 3, 3, C["dourado2"])
    p.rect(4, 12, 3, 2, C["dourado2"])
    p.outline(C["dourado3"])
    return p


def coracao():
    p = Pixel(16, 16)
    p.ellipse(5, 5.6, 4.5, 4.3, C["vermelho"])
    p.ellipse(11, 5.6, 4.5, 4.3, C["vermelho"])
    for y in range(7, 15):
        half = (14 - y) * 0.95
        if half > 0:
            p.rect(8 - half, y, half * 2 + 1, 1, C["vermelho"])
    p.rect(3, 3, 2, 2, C["branco"])
    p.rect(2, 4, 1, 1, C["branco"])
    p.rect(9, 11, 3, 2, C["vermelho2"])
    p.outline(C["vermelho2"])
    return p


# ==========================================================================
# CENÁRIO
# ==========================================================================
def chao_tile():
    """Tile 32x32 lógico sem emenda na horizontal."""
    p = Pixel(32, 32)
    p.rect(0, 0, 32, 32, C["terra"])
    p.rect(0, 16, 32, 16, C["terra2"])
    # Grama na BORDA de cima, com tufinhos que "espiam" para fora do chão.
    # (o padrão de 8 colunas cabe 4 vezes em 32: repete sem emenda!)
    for x in range(32):
        topo = 1 + int(round(1.0 * sin(x * 2 * pi / 8)))   # 0, 1 ou 2
        for y in range(0, topo):                            # deixa transparente
            p._put(x, y, (0, 0, 0, 0))
        p.rect(x, topo, 1, 9 - topo, C["grama"])
    p.rect(0, 7, 32, 2, C["grama2"])
    p.rect(0, 9, 32, 2, C["grama3"])
    for (x, y, w, h) in [(5, 18, 3, 2), (14, 24, 4, 3), (23, 14, 3, 2), (9, 28, 3, 2), (26, 26, 4, 3)]:
        p.rect(x, y, w, h, C["terra3"])
        p.rect(x, y, w, 1, C["pedra2"])
    for (x, y) in [(7, 21), (17, 29), (28, 19), (3, 25)]:
        p.rect(x, y, 2, 2, C["pedra2"])
    return p


def plataforma():
    """Plataforma 48x16 lógico (repete na horizontal)."""
    p = Pixel(48, 16)
    p.rect(0, 0, 48, 16, C["terra"])
    p.rect(0, 0, 48, 5, C["grama"])
    p.rect(0, 3, 48, 2, C["grama2"])
    p.rect(0, 5, 48, 2, C["grama3"])
    p.rect(0, 7, 48, 6, C["terra2"])
    p.rect(0, 12, 48, 4, C["terra3"])
    for x in range(2, 48, 7):
        p.rect(x, 9, 3, 2, C["terra3"])
    for x in range(0, 48, 5):
        p.rect(x, 0, 2, 1, C["grama2"])
    p.rect(0, 15, 48, 1, C["pedra2"])
    return p


def _nuvem(p, cx, cy, r=6):
    p.ellipse(cx, cy, r * 1.8, r, C["branco"])
    p.ellipse(cx - r, cy + 2, r, r * 0.8, C["branco"])
    p.ellipse(cx + r, cy + 3, r * 0.9, r * 0.7, C["branco"])
    p.ellipse(cx, cy - r * 0.5, r * 0.8, r * 0.6, C["branco"])


def nuvens_faixa(largura=640, altura=150):
    """Faixa de nuvens com repetição perfeita (perfeita para tileSprite)."""
    p = Pixel(largura, altura)
    nuvens = [(60, 40, 9), (200, 90, 6), (330, 35, 7), (470, 80, 8), (570, 25, 5), (130, 110, 5), (400, 120, 4)]
    for (x, y, r) in nuvens:
        for desloc in (-largura, 0, largura):        # desenha e repete nas bordas
            _nuvem(p, x + desloc, y, r)
    m = p.mask()                                     # base levemente sombreada
    for y in range(altura):
        for x in range(largura):
            if m[y, x] and not (y + 1 < altura and m[y + 1, x]):
                p._put(x, y, (223, 236, 250, 255))
    return p


def montanhas_faixa(largura=640, altura=160):
    """Montanhas médias com repetição perfeita (senoides de período inteiro)."""
    p = Pixel(largura, altura)
    camadas = [(C["grama3"], 62, 42, 3, 2), (C["verde3"], 34, 26, 5, 3)]
    for (cor, base_y, amp, f1, f2) in camadas:
        for x in range(largura):
            h = base_y + amp * (0.6 * sin(x * f1 * 2 * pi / largura) + 0.4 * sin(x * f2 * 2 * pi / largura + 1.2))
            topo = int(altura - h)
            p.rect(x, topo, 1, altura - topo, cor)
        for x in range(0, largura, 19):              # "arvorezinhas" no topo
            h = base_y + amp * (0.6 * sin(x * f1 * 2 * pi / largura) + 0.4 * sin(x * f2 * 2 * pi / largura + 1.2))
            topo = int(altura - h)
            p.rect(x, topo - 8, 5, 8, cor)
            p.rect(x + 1, topo - 12, 3, 4, cor)
    return p


def montanhas_claras(largura=640, altura=120):
    """Colinas distantes e clarinhas (camada mais ao fundo)."""
    p = Pixel(largura, altura)
    for x in range(largura):
        h = 62 + 36 * sin(x * 2 * pi / largura) + 18 * sin(x * 4 * pi / largura + 0.6)
        topo = int(altura - h)
        p.rect(x, topo, 1, altura - topo, (150, 205, 160, 255))
        p.rect(x, topo, 1, 6, (176, 222, 182, 255))
    return p


def ceu(largura=640, altura=360):
    """Céu com degradê, sol e nuvens - versão estática usada na Aula 01."""
    a = np.zeros((altura, largura, 4), dtype=np.uint8)
    topo = np.array([74, 160, 232])
    base = np.array([190, 232, 248])
    for y in range(altura):
        t = (y / (altura - 1)) ** 1.25
        cor = (topo * (1 - t) + base * t).astype(np.uint8)
        a[y, :] = [int(cor[0]), int(cor[1]), int(cor[2]), 255]
    p = Pixel(largura, altura)
    p.a = a
    for r in range(52, 24, -2):                      # halo suave, sem "degraus"
        for alpha in (0.10,):
            p.blend_ellipse(500, 70, r, r, (255, 240, 175), alpha)
    p.ellipse(500, 70, 24, 24, (255, 226, 120, 255))
    p.ellipse(500, 70, 20, 20, (255, 240, 168, 255))
    p.ellipse(500, 70, 14, 14, (255, 250, 214, 255))
    p.blend_ellipse(500, 70, 9, 9, (255, 255, 240), 0.85)
    for (x, y, r) in [(90, 60, 8), (170, 120, 6), (300, 45, 7), (395, 110, 5), (600, 95, 6), (40, 150, 5)]:
        _nuvem(p, x, y, r)
    return p


if __name__ == "__main__":
    print("Gerando arte da trilha (pixel art x2)...")
    sheet([heroi("parado", 0), heroi("parado", 1)], "heroi-parado.png")
    sheet([heroi("correndo", i) for i in range(4)], "heroi-correndo.png")
    sheet([heroi("pulando")], "heroi-pulando.png")
    sheet([heroi("dano")], "heroi-dano.png")
    sheet([gosma(i) for i in range(4)], "gosma-andando.png")
    sheet([gosma(i, derrotada=True) for i in range(2)], "gosma-derrotada.png")
    sheet([moeda(i) for i in range(4)], "moeda.png")
    save(estrela().to_image(), "estrela.png")
    save(coracao().to_image(), "coracao.png")
    save(chao_tile().to_image(), "chao.png")
    save(plataforma().to_image(), "plataforma.png")
    save(nuvens_faixa().to_image(SBG), "nuvens.png")
    save(montanhas_faixa().to_image(SBG), "montanhas.png")
    save(montanhas_claras().to_image(SBG), "montanhas-claras.png")
    save(ceu().to_image(SBG), "ceu.png")
    print("Pronto!")
