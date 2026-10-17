"""Sherka – "Der Weg": eine durchgehende Lichtlinie führt durch den Ablauf (Erstgespräch > Entwurf > Freigabe > Online).
Alles per Code gerendert (PIL + numpy), 1080x1920, 30 fps. Aufruf: python3 path_video.py [test]"""
import math, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from multiprocessing import Pool

W, H, FPS, S = 1080, 1920, 30, 2
TOTAL = 21.6
BGC = (8, 9, 12)
WHITE = (245, 245, 247); GREY = (150, 158, 168); DARK = (19, 31, 36); EDGE = (55, 70, 79)
OR = (255, 159, 28); OR_L = (255, 205, 120); OR_D = (198, 110, 0)
BLUE = (10, 111, 224); BLUE_D = (6, 78, 160)
FD = "/usr/share/fonts/opentype/inter/Inter-"

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def seg(t, a, b): return clamp((t - a) / (b - a))
def sst(x): x = clamp(x); return x * x * x * (x * (6 * x - 15) + 10)
def eo(x): x = clamp(x); return 1 - (1 - x) ** 3
def eback(x, k=1.9): x = clamp(x); return 1 + (k + 1) * (x - 1) ** 3 + k * (x - 1) ** 2
def lerp(a, b, u): return a + (b - a) * u
def lerpc(a, b, u): return tuple(int(lerp(a[i], b[i], u)) for i in range(3))

_fc = {}
def F(w, s):
    k = (w, int(s * S))
    if k not in _fc: _fc[k] = ImageFont.truetype(f"{FD}{w}.otf", int(s * S))
    return _fc[k]
def tw(s, size, w="Bold"): return F(w, size).getlength(s) / S
def T(d, x, y, s, size, w="Bold", fill=WHITE, a=1.0, anchor="ms"):
    if a <= 0.004: return
    d.text((x * S, y * S), s, font=F(w, size), fill=(*fill, int(255 * clamp(a))), anchor=anchor)
def C(d, x, y, r, fill, a=1.0, ry=None):
    if a <= 0.004: return
    ry = r if ry is None else ry
    d.ellipse(((x - r) * S, (y - ry) * S, (x + r) * S, (y + ry) * S), fill=(*fill, int(255 * clamp(a))))
def RR(d, box, r, fill, a=1.0, outline=None, ow=0):
    if a <= 0.004: return
    kw = {}
    if outline: kw = dict(outline=(*outline, int(255 * clamp(a))), width=int(ow * S))
    d.rounded_rectangle([v * S for v in box], r * S, fill=(*fill, int(255 * clamp(a))), **kw)
def LN(d, pts, width, fill, a=1.0):
    if a <= 0.004 or len(pts) < 2: return
    d.line([(x * S, y * S) for x, y in pts], fill=(*fill, int(255 * clamp(a))), width=max(1, int(width * S)), joint="curve")

# ---------- Zeitplan ----------
A = [2.4, 4.8, 7.2, 9.6]                 # Ankunft Stationen
YS = [1900, 3400, 4900, 6400]            # Welt-y der Stationen
NODE_Y = 1450; DEV_UP = 560              # Bildschirm-y der Node / Abstand Gerät
CYS = [y - NODE_Y for y in YS]
ZE = 0.32; CYE = 3650 - 960 / ZE
Y0 = 938; BASE = 960; DOTR = 22
_wa = F("Bold", 190).getlength("sherka") / S
_tot = _wa + 12 + 2 * DOTR; X0 = (W - _tot) / 2; XD = X0 + _wa + 12 + DOTR

def interp(keys, t):
    if t <= keys[0][0]: return keys[0][1:] if len(keys[0]) > 2 else keys[0][1]
    for i in range(len(keys) - 1):
        a, b = keys[i], keys[i + 1]
        if t <= b[0]:
            u = sst((t - a[0]) / (b[0] - a[0]) if b[0] > a[0] else 1)
            if len(a) > 2: return tuple(lerp(a[j], b[j], u) for j in range(1, len(a)))
            return lerp(a[1], b[1], u)
    return keys[-1][1:] if len(keys[-1]) > 2 else keys[-1][1]

HK = [(0, Y0), (1.67, Y0)]
for k in range(4):
    HK.append((A[k] - 0.12, YS[k]))
    if k < 3: HK.append((A[k] + 1.4, YS[k]))
CK = [(0, 0, 1), (1.67, 0, 1)]
for k in range(4):
    CK.append((A[k], CYS[k], 1))
    if k < 3: CK.append((A[k] + 1.5, CYS[k], 1))
CK += [(12.0, CYS[3], 1), (14.4, CYE, ZE)]

def pathx(y):
    u = y - Y0; e = math.exp(-max(u, 0) / 450)
    return 540 + (XD - 540) * e + 210 * math.sin(2 * math.pi * u / 3000) * (1 - e)

class Cam: Z = 1.0; CY = 0.0; SX = 0.0; SY = 0.0
def ws(wx, wy): return ((wx - 540) * Cam.Z + 540 + Cam.SX, (wy - Cam.CY) * Cam.Z + Cam.SY)

# ---------- Sprites ----------
_shot = Image.open("assets/bledi.png").convert("RGB")
_zshot = Image.open("assets/zahnarzt.png").convert("RGB")
_icon0 = Image.open("assets/logo/icon-dark-transparent-1024.png").convert("RGBA")
ICON = _icon0.crop(_icon0.getbbox())

def new_layer(w, h): return Image.new("RGBA", (int(w * S), int(h * S)), (0, 0, 0, 0))

def btn3d(d, box, r, face, lip, text, size, press=0.0, tcol=WHITE):
    x0, y0, x1, y1 = box; off = 10 * (1 - press); dy = 10 * press
    RR(d, (x0, y0 + 10, x1, y1 + 10 - dy * 0 ), r, lip)
    RR(d, (x0, y0 + dy, x1, y1 - 0 + dy - 0 - (10 - off) * 0), r, face)
    T(d, (x0 + x1) / 2, (y0 + y1) / 2 + dy + size * 0.35, text, size, "Bold", tcol)

def phone_sprite(tau):
    cw, chh = 560, 800
    ph_w = 416
    lay = new_layer(cw, chh)
    d = ImageDraw.Draw(lay, "RGBA")
    px0 = 60
    RR(d, (px0 - 10, 0, px0 + ph_w + 10, chh), 52, (50, 50, 58))
    sh = _shot.resize((ph_w * S, int(_shot.height * ph_w * S / _shot.width)), Image.LANCZOS).crop((0, 0, ph_w * S, (chh - 20) * S))
    m = Image.new("L", sh.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, sh.width, sh.height), 42 * S, fill=255)
    lay.paste(sh, (px0 * S, 10 * S), m)
    # Kommentar-Pin
    p = eback((tau - 0.7) / 0.35)
    if tau > 0.7:
        done = tau > 1.55
        txt = "Erledigt" if done else "Button grösser?"
        w_ = tw(txt, 34, "Bold") + (70 if done else 44)
        cx, cy_ = 400, 250
        sc = clamp(p, 0, 1.15)
        bx0, bx1 = cx - w_ / 2 * sc, cx + w_ / 2 * sc; by0, by1 = cy_ - 36 * sc, cy_ + 36 * sc
        col = (60, 190, 90) if done else OR
        RR(d, (bx0, by0 + 6, bx1, by1 + 6), 36 * sc, lerpc(col, (0, 0, 0), 0.3))
        RR(d, (bx0, by0, bx1, by1), 36 * sc, col)
        if sc > 0.5:
            if done:
                x0_ = cx - tw(txt, 34) / 2 - 18
                T(d, cx + 22, cy_ + 12, txt, 34, "Bold", (255, 255, 255))
                LN(d, [(x0_ - 4, cy_ + 2), (x0_ + 8, cy_ + 14), (x0_ + 30, cy_ - 12)], 6, (255, 255, 255))
            else:
                T(d, cx, cy_ + 12, txt, 34, "Bold", (30, 20, 0))
    return lay, (cw, chh)

def laptop_sprite(tau):
    cw, chh = 880, 780
    lay = new_layer(cw, chh); d = ImageDraw.Draw(lay, "RGBA")
    sw, sh_ = 720, 450; x0 = (cw - sw) / 2; y0 = 110
    RR(d, (x0 - 22, y0 - 22, x0 + sw + 22, y0 + sh_ + 22), 24, (46, 46, 52))
    scr = _zshot.resize((sw * S, sh_ * S), Image.LANCZOS)
    lay.paste(scr, (int(x0 * S), int(y0 * S)))
    RR(d, (x0 - 60, y0 + sh_ + 22, x0 + sw + 60, y0 + sh_ + 48), 12, (196, 196, 204))
    RR(d, (cw / 2 - 70, y0 + sh_ + 22, cw / 2 + 70, y0 + sh_ + 34), 6, (150, 150, 158))
    # Online-Pille
    p = eback((tau - 0.6) / 0.35)
    if tau > 0.6:
        sc = clamp(p, 0, 1.15); cx, cy_ = cw / 2, 52
        w_ = 210 * sc
        RR(d, (cx - w_ / 2, cy_ - 34 * sc, cx + w_ / 2, cy_ + 34 * sc), 34 * sc, (22, 34, 40), outline=(60, 190, 90), ow=3)
        if sc > .6:
            C(d, cx - 56, cy_, 10, (60, 220, 100))
            T(d, cx + 14, cy_ + 12, "Online", 36, "Bold", WHITE)
    # Domain-Chip
    if tau > 1.1:
        a = eo((tau - 1.1) / 0.3); cy_ = y0 + sh_ + 120
        txt = "deine-firma.ch"; w_ = tw(txt, 38, "Bold") + 240
        RR(d, (cw / 2 - w_ / 2, cy_ - 36 + (1 - a) * 20, cw / 2 + w_ / 2, cy_ + 36 + (1 - a) * 20), 36, (22, 34, 40), a, outline=EDGE, ow=2)
        T(d, cw / 2 - 74, cy_ + 12 + (1 - a) * 20, txt, 38, "Bold", WHITE, a)
        T(d, cw / 2 + w_ / 2 - 105, cy_ + 12 + (1 - a) * 20, "gehört dir", 32, "Medium", OR, a)
    return lay, (cw, chh)

def chat_sprite(tau):
    cw, chh = 780, 600
    lay = new_layer(cw, chh); d = ImageDraw.Draw(lay, "RGBA")
    RR(d, (0, 0, cw, chh), 48, DARK, 1, outline=EDGE, ow=3)
    C(d, 70, 74, 28, OR); T(d, 112, 86, "sherka.", 38, "Bold", WHITE, anchor="ls")
    C(d, 330, 70, 7, (60, 220, 100)); T(d, 346, 80, "antwortet", 28, "Medium", GREY, anchor="ls")
    d.line((40 * S, 130 * S, (cw - 40) * S, 130 * S), fill=(*EDGE, 255), width=2 * S)
    # Nutzer
    p = eback((tau - 0.45) / 0.3)
    if tau > 0.45:
        sc = clamp(p, 0, 1.1); r = cw - 44
        RR(d, (r - 450 * sc, 180, r, 180 + 150 * sc), 36, OR)
        if sc > .7:
            T(d, r - 225, 245, "Ich brauche eine", 38, "Bold", (30, 20, 0)); T(d, r - 225, 295, "neue Website.", 38, "Bold", (30, 20, 0))
    # tippt
    if 0.95 < tau < 1.35:
        RR(d, (44, 380, 44 + 150, 380 + 84), 40, (45, 60, 68))
        for i in range(3):
            a = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(tau * 14 - i * 1.2)); C(d, 44 + 40 + i * 35, 422, 9, WHITE, a)
    p2 = eback((tau - 1.35) / 0.3)
    if tau > 1.35:
        sc = clamp(p2, 0, 1.1)
        RR(d, (44, 360, 44 + 560 * sc, 360 + 190 * sc), 36, (45, 60, 68))
        if sc > .7:
            T(d, 44 + 280, 435, "Gerne! Wir antworten", 38, "Bold", WHITE); T(d, 44 + 280, 485, "innert eines Werktags.", 38, "Bold", WHITE)
    return lay, (cw, chh)

def approval_sprite(tau):
    cw, chh = 780, 560
    lay = new_layer(cw, chh); d = ImageDraw.Draw(lay, "RGBA")
    RR(d, (0, 0, cw, chh), 48, DARK, 1, outline=EDGE, ow=3)
    if tau < 1.1:
        T(d, cw / 2, 120, "Entwurf bereit", 62, "Bold", WHITE)
        T(d, cw / 2, 190, "Passt alles so?", 40, "Medium", GREY)
        # Mini-Vorschau
        RR(d, (120, 240, cw - 120, 380), 22, (30, 44, 52)); RR(d, (150, 270, 420, 292), 10, (80, 98, 108)); RR(d, (150, 308, 520, 326), 9, (60, 76, 86)); RR(d, (150, 340, 300, 360), 10, OR)
        press = sst((tau - 0.85) / 0.1) if tau > 0.85 else 0
        btn3d(d, (160, 420, cw - 160, 510), 45, BLUE, BLUE_D, "Freigeben", 44, press)
    else:
        u = eback((tau - 1.1) / 0.4)
        sc = clamp(u, 0, 1.12)
        C(d, cw / 2, 230, 100 * sc, OR_D, ry=100 * sc); C(d, cw / 2, 220, 100 * sc, OR)
        if sc > .5:
            k = sc
            LN(d, [(cw / 2 - 48 * k, 222 * 1), (cw / 2 - 12 * k, 258), (cw / 2 + 52 * k, 188)], 16, (255, 255, 255))
        T(d, cw / 2, 420, "Freigegeben", 66, "Bold", WHITE, eo((tau - 1.3) / 0.3))
        T(d, cw / 2, 482, "Jetzt gehen wir online.", 38, "Medium", GREY, eo((tau - 1.5) / 0.3))
    return lay, (cw, chh)

SPR = [chat_sprite, phone_sprite, approval_sprite, laptop_sprite]

def blit(art, spr, cx, cy_, ks, a=1.0):
    nw, nh = int(spr.width * ks), int(spr.height * ks)
    if nw < 4 or nh < 4 or a <= 0.01: return
    im = spr.resize((nw, nh), Image.BILINEAR if ks < 1 else Image.LANCZOS)
    if a < 1: im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    x, y = int(cx * S - nw / 2), int(cy_ * S - nh / 2)
    sx0, sy0 = max(0, -x), max(0, -y); sx1, sy1 = min(nw, art.width - x), min(nh, art.height - y)
    if sx1 <= sx0 or sy1 <= sy0: return
    art.alpha_composite(im.crop((sx0, sy0, sx1, sy1)), (x + sx0, y + sy0))

# ---------- Welt ----------
def draw_node(d, g, x, y, k, t):
    Z = Cam.Z; r = 62 * Z; sx, sy = ws(x, y)
    if sy < -200 or sy > H + 200: return
    L = A[k] - 0.12; u = eo((t - L) / 0.25) if t > L else 0
    face = lerpc((55, 70, 79), OR, u); lip = lerpc((35, 47, 55), OR_D, u); num = lerpc((120, 135, 145), WHITE, u)
    C(d, sx, sy + 12 * Z, r, lip); C(d, sx, sy, r, face)
    C(d, sx - r * 0.25, sy - r * 0.42, r * 0.5, lerpc((75, 92, 102), OR_L, u), 0.55, ry=r * 0.22)
    T(d, sx, sy + 20 * Z, str(k + 1), max(10, 58 * Z), "Bold", num)
    if u > 0:
        g.ellipse((sx - r * 1.5, sy - r * 1.5, sx + r * 1.5, sy + r * 1.5), fill=int(150 * u))
    tau = t - L
    if 0 < tau < 0.7:
        rr = r * (1 + 1.4 * eo(tau / 0.7)); a = 1 - tau / 0.7
        d.ellipse(((sx - rr) * S, (sy - rr) * S, (sx + rr) * S, (sy + rr) * S), outline=(*OR, int(200 * a)), width=int(6 * S * Z + 1))

def draw_world(t, art, gW):
    d = ImageDraw.Draw(art, "RGBA"); g = ImageDraw.Draw(gW)
    Z = Cam.Z; hy = interp(HK, t)
    ytop = Cam.CY - 150 / Z; ybot = Cam.CY + (H + 150) / Z
    ya = max(Y0, ytop); yb = min(YS[3] + 700, ybot)
    def poly(a, b):
        ys = list(np.arange(a, b, 14)) + [b]
        return [ws(pathx(y), y) for y in ys]
    if yb > ya:
        LN(d, poly(ya, yb), max(14, 64 * Z), (24, 28, 36), seg(t, 1.45, 1.75))
    yl = min(hy, ybot)
    if yl > ya + 1:
        pts = poly(ya, yl)
        w_ = max(7, 15 * Z)
        LN(d, pts, w_ + 4 * Z, OR_D); LN(d, pts, w_, OR); LN(d, pts, max(3, w_ * 0.4), (255, 232, 180))
        g.line(pts, fill=255, width=int(max(14, 34 * Z)), joint="curve")
    # Wortmarke (Welt), Reveal 0.9 - 1.3
    p = seg(t, 0.85, 1.3)
    if p > 0:
        tl = new_layer(_wa + 20, 260); td = ImageDraw.Draw(tl, "RGBA")
        td.text((10 * S, 200 * S), "sherka", font=F("Bold", 190), fill=(*WHITE, int(255 * (1 - seg(t, 1.75, 2.25)))), anchor="ls")
        cw_ = int((10 + _wa * p) * S)
        tl = tl.crop((0, 0, cw_, tl.height))
        k = Z
        sx, sy = ws(X0 - 10, BASE - 200)
        im = tl.resize((max(1, int(tl.width * k)), max(1, int(tl.height * k))), Image.LANCZOS)
        art.alpha_composite(im, (max(0, int(sx * S)), max(0, int(sy * S)))) if sx * S >= 0 and sy * S >= 0 and sy < H and sy * S < art.height - im.height else None
    for k in range(4): draw_node(d, g, pathx(YS[k]), YS[k], k, t)
    for k in range(4):
        if t >= A[k]:
            tau = t - A[k]; u = eback(tau / 0.55, 1.5)
            spr, _ = SPR[k](tau)
            nx = pathx(YS[k])
            fx, fy = ws(540, YS[k] - DEV_UP); sx0, sy0 = ws(nx, YS[k])
            m = eo(tau / 0.45)
            cx, cy_ = lerp(sx0, fx, m), lerp(sy0, fy, m)
            ks = Z * clamp(0.15 + 0.85 * u, 0.05, 1.12) * (1.0 if k != 3 else 1.0)
            blit(art, spr, cx, cy_, ks, clamp(tau / 0.2))
    # Kopf
    if t > 1.66:
        hx, hyy = ws(pathx(hy), hy); r = max(8, DOTR * Z)
        C(d, hx, hyy, r, OR); C(d, hx - r * .25, hyy - r * .3, r * .35, OR_L, 0.7)
        g.ellipse((hx - r * 2.5, hyy - r * 2.5, hx + r * 2.5, hyy + r * 2.5), fill=255)

# ---------- HUD / Hero ----------
STAT = [("Erstgespräch", "Kostenlos und unverbindlich"), ("Entwurf", "Du siehst ihn, bevor wir starten"),
        ("Freigabe", "Online geht nur, was du freigibst"), ("Online", "Deine Domain gehört dir")]

def title_alpha(t):
    m = 0.0
    for k in range(4):
        a0 = A[k] + 0.05
        a = eo((t - a0) / 0.3) * (1 - sst((t - (A[k] + 1.3)) / 0.25)) if k < 3 else eo((t - a0) / 0.3) * (1 - sst((t - 11.7) / 0.3))
        m = max(m, a)
    return m

def draw_titles(t, d):
    for k in range(4):
        a0 = A[k] + 0.05
        a = eo((t - a0) / 0.3) * (1 - sst((t - (A[k] + 1.3)) / 0.25)) if k < 3 else eo((t - a0) / 0.3) * (1 - sst((t - 11.7) / 0.3))
        if a <= 0.01: continue
        y = 330 + (1 - eo((t - a0) / 0.3)) * 24
        title, sub = STAT[k]; w_ = tw(title, 92) + 100
        x0 = 540 - w_ / 2
        C(d, x0 + 38, y - 30, 38, OR_D, a, ry=38); C(d, x0 + 38, y - 36, 38, OR, a)
        T(d, x0 + 38, y - 18, str(k + 1), 46, "Bold", WHITE, a)
        T(d, x0 + 100, y, title, 92, "Bold", WHITE, a, "ls")
        T(d, 540, y + 78, sub, 44, "Medium", GREY, a)

def lockup(t, tl, d, g, ya=1.0, y_off=0):
    """tl = Zeit seit Landung des Punktes. Wortmarke mit Reveal und Punkt."""
    pass

def draw_hook(t, d, g, ov):
    # Streifen vor dem Slam
    if t < 0.17:
        rng = np.random.default_rng(3)
        for i in range(14):
            ang = rng.uniform(0, 2 * math.pi); s0 = 1500 - 1350 * (t / 0.17) ** 1.5 + rng.uniform(0, 200)
            ln = 260 + rng.uniform(0, 200)
            x1, y1 = 540 + math.cos(ang) * s0, 1000 + math.sin(ang) * s0 * 1.2
            x2, y2 = 540 + math.cos(ang) * (s0 + ln), 1000 + math.sin(ang) * (s0 + ln) * 1.2
            LN(d, [(x1, y1), (x2, y2)], 5, OR_L, 0.9)
            g.line((x1, y1, x2, y2), fill=200, width=14)
    # Punkt
    cx, cy_, rx, ry = None, None, 0, 0
    if t < 0.17:
        r = 6 + (470 - 6) * (t / 0.17) ** 3; cx, cy_, rx, ry = 540, 1000, r, r
    elif t < 1.5:
        mv = sst((t - 0.45) / 0.8)
        r = lerp(470, DOTR, mv); cx = lerp(540, XD, mv); cy_ = lerp(1000, Y0, mv)
        tau = t - 0.17
        if tau < 0.3:
            q = tau / 0.3; sx_ = 1 + 0.4 * math.sin(math.pi * q) * math.exp(-1.5 * q)
            rx, ry = r * sx_, r / sx_
        else: rx = ry = r
        if 1.32 < t < 1.44:
            q = (t - 1.32) / 0.12; sq = 1 - 0.65 * math.sin(math.pi * q); rx, ry = r * (1 + 0.3 * (1 - sq)), r * sq
    elif t < 1.67:
        q = (t - 1.5) / 0.17; hop = 100 * math.sin(math.pi * q) if q < 1 else 0
        cx, cy_, rx, ry = XD, Y0 - hop, DOTR, DOTR
        if q > 0.85: ry = DOTR * (1 + 0.1)
    if cx is not None:
        sx, sy = ws(cx, cy_)
        C(d, sx, sy + min(rx, 40) * 0.18, rx, OR_D, ry=ry); C(d, sx, sy, rx, OR, ry=ry)
        C(d, sx - rx * .28, sy - ry * .34, rx * .4, OR_L, 0.55, ry=ry * .28)
        gr = min(rx * 1.8, 200 + rx * 0.3)
        g.ellipse((sx - gr, sy - gr * (ry / rx), sx + gr, sy + gr * (ry / rx)), fill=int(255 * min(1.0, 70 / max(rx, 1)) + 25))
    # Splitter
    if 0.17 <= t < 0.8:
        rng = np.random.default_rng(11); tt = t - 0.17
        for i in range(18):
            ang = rng.uniform(0, 2 * math.pi); v = rng.uniform(500, 1100); sz = rng.uniform(8, 22)
            x = 540 + math.cos(ang) * v * tt; y = 1000 + math.sin(ang) * v * tt + 900 * tt * tt
            a = 1 - tt / 0.63; C(d, x, y, sz, OR if i % 3 else OR_L, a)
    # Unterstreichung 0.85 - 1.3
    if 0.85 < t < 1.55:
        p = sst((t - 0.85) / 0.45); a = 1 - seg(t, 1.3, 1.55)
        y = BASE + 40; xe = lerp(X0 - 10, XD, p)
        LN(d, [(X0 - 10, y), (xe, y)], 10, OR, a); g.line((X0 - 10, y, xe, y), fill=int(220 * a), width=26)
    # Blitz
    if 0.17 <= t < 0.30: ov[0] = 0.16 * (1 - (t - 0.17) / 0.13)

def draw_tagline_phase(t, d, g):
    if not 14.3 < t < 16.7: return
    fo = 1 - sst((t - 16.2) / 0.35)
    a1 = eo((t - 14.7) / 0.35) * fo; a2 = eo((t - 15.05) / 0.35) * fo
    T(d, 540, 860 + (1 - eo((t - 14.7) / 0.35)) * 40, "Mehr Kunden.", 150, "Bold", WHITE, a1)
    T(d, 540, 1040 + (1 - eo((t - 15.05) / 0.35)) * 40, "Weniger Aufwand.", 104, "Bold", WHITE, a2)
    p = sst((t - 15.5) / 0.6)
    if p > 0:
        y = 1130; xe = lerp(120, 960, p)
        LN(d, [(120, y), (xe, y)], 14, OR, fo); LN(d, [(120, y), (xe, y)], 5, (255, 232, 180), fo)
        g.line((120, y, xe, y), fill=int(230 * fo), width=34)
        C(d, xe, y, 14, OR, fo); 
        g.ellipse((xe - 30, y - 30, xe + 30, y + 30), fill=int(255 * fo))

def draw_hero(t, d, g, ov):
    if t < 16.4: return
    LAND = 16.8
    aA = 1 - seg(t, 19.1, 19.5)
    # Punkt fällt
    if aA > 0:
        if t < LAND:
            q = (t - 16.45) / 0.35
            if q > 0:
                y = lerp(-80, Y0, clamp(q) ** 2)
                C(d, XD, y, DOTR, OR, 1, ry=DOTR * (1 + 0.5 * clamp(q))); g.ellipse((XD - 40, y - 60, XD + 40, y + 60), fill=255)
                for i in range(3): LN(d, [(XD, y - 40 - i * 40), (XD, y - 140 - i * 50)], 6, OR_L, 0.3 * (1 - i * 0.3))
        else:
            tau = t - LAND
            sq = 1 + 0.6 * math.sin(math.pi * clamp(tau / 0.3)) * math.exp(-2 * tau) if tau < 0.3 else 1
            C(d, XD, Y0 + (1 - 1 / sq) * DOTR * 0.2, DOTR * sq, OR, aA, ry=DOTR / sq)
            g.ellipse((XD - 34, Y0 - 34, XD + 34, Y0 + 34), fill=int(110 * aA))
            if tau < 0.6:
                rr = 40 + 520 * eo(tau / 0.6); a = (1 - tau / 0.6) * 0.8
                d.ellipse(((XD - rr) * S, (Y0 - rr * 0.35) * S, (XD + rr) * S, (Y0 + rr * 0.35) * S), outline=(*OR_L, int(255 * a)), width=5 * S)
            if tau < 0.12: ov[0] = max(ov[0], 0.22 * (1 - tau / 0.12))
            # Wortmarke
            p = seg(t, 16.95, 17.4)
            if p > 0:
                tl = new_layer(_wa + 20, 260); td = ImageDraw.Draw(tl, "RGBA")
                td.text((10 * S, 200 * S), "sherka", font=F("Bold", 190), fill=(*WHITE, int(255 * aA)), anchor="ls")
                tl = tl.crop((0, 0, int((10 + _wa * sst(p)) * S), tl.height))
                d._image.alpha_composite(tl, (int((X0 - 10) * S), int((BASE - 200) * S)))
                y = BASE + 40; xe = lerp(X0 - 10, XD, sst(p)); a = (1 - seg(t, 17.4, 17.7)) * aA
                LN(d, [(X0 - 10, y), (xe, y)], 10, OR, a); g.line((X0 - 10, y, xe, y), fill=int(220 * a), width=26)
            T(d, 540, 1100 + (1 - eo((t - 17.6) / 0.4)) * 30, "Websites, die Kunden bringen.", 54, "Medium", GREY, eo((t - 17.6) / 0.4) * aA)
    # End card Logo
    aB = seg(t, 19.3, 19.8)
    if aB > 0:
        ih = 320; iw = ICON.width * ih / ICON.height
        ic = ICON.resize((int(iw * S), int(ih * S)), Image.LANCZOS)
        if aB < 1: ic.putalpha(ic.getchannel("A").point(lambda v: int(v * aB)))
        d._image.alpha_composite(ic, (int((540 - iw / 2) * S), int((560 - ih / 2 + (1 - eo(aB)) * 30) * S)))
        w1 = tw("sherka", 124); w2 = tw(".ch", 124); x0 = 540 - (w1 + w2) / 2
        yy = 900 + (1 - eo(aB)) * 30
        T(d, x0, yy, "sherka", 124, "Bold", WHITE, aB, "ls"); T(d, x0 + w1, yy, ".ch", 124, "Bold", OR, aB, "ls")
    # CTA
    if t > 18.2:
        u = eback((t - 18.2) / 0.4)
        sc = clamp(u, 0, 1.08); cy_ = 1330
        bw, bh = 700 * sc, 130 * sc
        RR(d, (540 - bw / 2, cy_ - bh / 2 + 12, 540 + bw / 2, cy_ + bh / 2 + 12), 65 * sc, BLUE_D)
        RR(d, (540 - bw / 2, cy_ - bh / 2, 540 + bw / 2, cy_ + bh / 2), 65 * sc, BLUE)
        if sc > .5: T(d, 540, cy_ + 20 * sc, "Erstgespräch anfragen", 54, "Bold", WHITE)
        a = eo((t - 18.7) / 0.4)
        T(d, 540, cy_ + 130, "Kostenlos und unverbindlich", 44, "Medium", GREY, a)
        T(d, 540, cy_ + 200, "Link in der Bio", 44, "Bold", OR, a)

def render_frame(i, sub=0.0):
    t = max(0.0, i / FPS + sub)
    cy_, z = interp(CK, t)
    Cam.CY, Cam.Z = cy_, z
    sh = 0.0
    if 0.17 <= t < 0.9:
        q = t - 0.17; sh = 26 * math.exp(-q * 9) * math.sin(q * 70)
    Cam.SX, Cam.SY = sh, sh * 0.7
    wa = (1 - 0.78 * sst((t - 14.3) / 0.5)) * (1 - sst((t - 16.2) / 0.35))
    art = new_layer(W, H); gW = Image.new("L", (W, H), 0)
    top = new_layer(W, H); gT = Image.new("L", (W, H), 0)
    ov = [0.0]
    if wa > 0.01 and t < 16.6: draw_world(t, art, gW)
    d = ImageDraw.Draw(top, "RGBA"); g = ImageDraw.Draw(gT)
    draw_hook(t, d, g, ov); draw_titles(t, d); draw_tagline_phase(t, d, g); draw_hero(t, d, g, ov)
    def down(im):
        im = im.convert("RGBa").resize((W, H), Image.LANCZOS).convert("RGBA")
        return np.asarray(im, dtype=np.float32) / 255.0
    gw = np.asarray(gW.filter(ImageFilter.GaussianBlur(20)), dtype=np.float32) / 255.0 * wa
    gt = np.asarray(gT.filter(ImageFilter.GaussianBlur(22)), dtype=np.float32) / 255.0
    out = BG.copy()
    glow = np.clip(gw + gt, 0, 1)[..., None] * (np.array(OR, dtype=np.float32) / 255.0) * 0.85
    out = out + glow
    aw = down(art); aw[..., 3] *= wa
    out = out * (1 - aw[..., 3:4]) + aw[..., :3] * aw[..., 3:4]
    ta = title_alpha(t)
    if ta > 0.01:
        yy_ = np.arange(H, dtype=np.float32)
        band = 1 - np.vectorize(lambda v: sst((v - 380) / 150))(yy_[::6]).repeat(6)[:H].astype(np.float32)
        b = (band * 0.93 * ta)[:, None, None]
        out = out * (1 - b) + (np.array(BGC, dtype=np.float32) / 255.0)[None, None, :] * b
    at = down(top)
    out = out * (1 - at[..., 3:4]) + at[..., :3] * at[..., 3:4]
    if ov[0] > 0: out = out + ov[0]
    # Parallax-Staub
    out = dust(out, t)
    out = out * VIG
    rng = np.random.default_rng(abs(i * 7 + int(sub * 1000)))
    out = out + rng.normal(0, 0.012, (H, W, 1)).astype(np.float32)
    return np.clip(out, 0, 1)

def dust(out, t):
    rng = np.random.default_rng(5)
    n = 60
    xs = rng.uniform(0, W, n); ys0 = rng.uniform(0, H, n); pz = rng.uniform(0.25, 0.9, n); sz = rng.uniform(1.5, 3.8, n); br = rng.uniform(0.25, 0.7, n)
    for i in range(n):
        y = (ys0[i] - Cam.CY * Cam.Z * pz[i] * 0.4 - t * 14 * pz[i]) % H
        x = int(xs[i]); yi = int(y); r = int(sz[i])
        out[max(0, yi - r):yi + r, max(0, x - r):x + r] += np.array([0.35, 0.3, 0.22]) * br[i] * 0.55
    return out

def frame_bytes(i):
    mb = (0 <= i / FPS < 1.7) or (12.0 <= i / FPS < 14.4)
    if mb:
        fr = (render_frame(i, -1 / 90) + render_frame(i, 0) + render_frame(i, 1 / 90)) / 3
    else:
        fr = render_frame(i)
    return (fr * 255 + 0.5).astype(np.uint8).tobytes()

def init():
    global BG, VIG
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - 540) / 900) ** 2 + ((yy - 1000) / 1100) ** 2)
    glow = np.clip(1 - r, 0, 1) ** 2
    base = np.array(BGC, dtype=np.float32) / 255
    BG = base[None, None, :] + glow[..., None] * np.array([0.06, 0.045, 0.03], dtype=np.float32) * 0.9
    rv = np.sqrt(((xx - 540) / 700) ** 2 + ((yy - 960) / 1250) ** 2)
    VIG = (1 - 0.35 * np.clip(rv - 0.5, 0, 1) ** 1.5)[..., None].astype(np.float32)

if __name__ == "__main__":
    init()
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        times = [float(x) for x in sys.argv[2:]]
        for tt in times:
            fr = render_frame(int(tt * FPS))
            Image.fromarray((fr * 255).astype(np.uint8)).resize((540, 960)).save(f"/tmp/pt_{tt}.png")
        sys.exit()
    n = int(TOTAL * FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", "sherka-path-audio.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium",
           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", "sherka-der-weg.mp4"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(4, initializer=init) as pool:
        for k, b in enumerate(pool.imap(frame_bytes, range(n), chunksize=2)):
            p.stdin.write(b)
            if k % 60 == 0: print(k, "/", n, flush=True)
    p.stdin.close(); p.wait(); print("fertig")
