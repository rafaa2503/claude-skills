import math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
BG = (10, 10, 12)
WHITE = (245, 245, 247)
GREY = (160, 160, 168)
ORANGE = (255, 159, 28)
BLUE = (10, 111, 224)
FD = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(f"{FD}Inter-{w}.otf", s)

def ease(t): t = max(0, min(1, t)); return 1 - (1 - t) ** 3
def seg(t, a, b): return ease((t - a) / (b - a))

# Hintergrund mit weichem Glow
bg = Image.new("RGB", (W, H), BG)
glow = Image.new("RGB", (W, H), (0, 0, 0))
ImageDraw.Draw(glow).ellipse((150, 350, 930, 1130), fill=(26, 30, 44))
bg = Image.blend(bg, Image.composite(glow, bg, glow.convert("L").point(lambda v: 255 if v else 0)), 0.0)
glow = glow.filter(ImageFilter.GaussianBlur(260))
bg = Image.fromarray(__import__("numpy").clip(__import__("numpy").asarray(bg, dtype="int16") + __import__("numpy").asarray(glow, dtype="int16"), 0, 255).astype("uint8"))

shot = Image.open("assets/bledi.png").convert("RGB")
PW = 640
shot = shot.resize((PW, int(shot.height * PW / shot.width)), Image.LANCZOS)
PHONE_H = 1230
shot = shot.crop((0, 0, PW, PHONE_H))
mask = Image.new("L", (PW, PHONE_H), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, PW, PHONE_H), 56, fill=255)

def text(d, xy, s, f, fill, alpha=1.0, anchor="ma"):
    if alpha <= 0: return
    c = tuple(int(BG[i] + (fill[i] - BG[i]) * alpha) for i in range(3))
    d.text(xy, s, font=f, fill=c, anchor=anchor)

def lines(d, t, items, y0, f, fill, t0, gap, step=0.35, dy=40, lh=100, anchor="ma", x=W // 2):
    for i, s in enumerate(items):
        p = seg(t, t0 + i * step, t0 + i * step + 0.5)
        text(d, (x, y0 + i * lh + (1 - p) * dy), s, f, fill, p, anchor)

def brand(d, y, size, a_txt, b_txt, alpha):
    f = font("Bold", size)
    wa = f.getlength(a_txt); wb = f.getlength(b_txt)
    x = (W - wa - wb) / 2
    text(d, (x, y), a_txt, f, WHITE, alpha, "la")
    text(d, (x + wa, y), b_txt, f, ORANGE, alpha, "la")

TOTAL = 27.0
def frame(t):
    im = bg.copy(); d = ImageDraw.Draw(im)
    # S1 Hook 0-3.3
    if t < 3.5:
        a = 1 - seg(t, 3.0, 3.5)
        p1 = seg(t, 0.1, 0.6); p2 = seg(t, 1.3, 1.8)
        text(d, (W // 2, 640 + (1 - p1) * 40), "Bringt deine", font("Bold", 112), WHITE, p1 * a)
        text(d, (W // 2, 760 + (1 - p1) * 40), "Website Kunden?", font("Bold", 112), WHITE, p1 * a)
        text(d, (W // 2, 960 + (1 - p2) * 40), "Oder kostet sie", font("Bold", 84), GREY, p2 * a)
        text(d, (W // 2, 1060 + (1 - p2) * 40), "nur Geld?", font("Bold", 84), ORANGE, p2 * a)
    # S2 Marke 3.5-7.5
    if 3.5 <= t < 7.8:
        a = seg(t, 3.5, 4.0) * (1 - seg(t, 7.3, 7.8))
        brand(d, 700, 190, "sherka", ".", a)
        p = seg(t, 4.3, 4.9)
        text(d, (W // 2, 1000 + (1 - p) * 30), "Websites für kleine Betriebe", font("Medium", 58), WHITE, p * a)
        p = seg(t, 5.0, 5.6)
        text(d, (W // 2, 1090 + (1 - p) * 30), "in der ganzen Schweiz", font("Medium", 58), GREY, p * a)
    # S3 Beispiel 7.8-14.8
    if 7.8 <= t < 15.0:
        a = seg(t, 7.8, 8.3) * (1 - seg(t, 14.5, 15.0))
        text(d, (W // 2, 200), "Von uns gebaut", font("SemiBold", 64), GREY, a)
        slide = (1 - seg(t, 7.9, 8.8)) * 160
        sc = 1.0 + 0.03 * seg(t, 8.8, 14.8)
        ph = shot.copy(); mk = mask
        pw2, ph2 = int(PW * sc), int(PHONE_H * sc)
        ph = ph.resize((pw2, ph2), Image.LANCZOS); mk2 = mk.resize((pw2, ph2), Image.LANCZOS)
        x0 = (W - pw2) // 2; y0 = int(300 + slide)
        if a > 0:
            frame_img = Image.new("RGB", (pw2 + 24, ph2 + 24), (50, 50, 58))
            fm = Image.new("L", frame_img.size, 0)
            ImageDraw.Draw(fm).rounded_rectangle((0, 0, frame_img.width, frame_img.height), 68, fill=255)
            layer = im.copy(); layer.paste(frame_img, (x0 - 12, y0 - 12), fm); layer.paste(ph, (x0, y0), mk2)
            im = Image.blend(im, layer, a); d = ImageDraw.Draw(im)
        text(d, (W // 2, 1620), "bledi-bienne.ch", font("Bold", 70), WHITE, a)
        text(d, (W // 2, 1710), "Marokkanisches Restaurant, Biel", font("Medium", 44), GREY, a)
    # S4 Vorteile 15.0-21.5
    if 15.0 <= t < 21.8:
        a = seg(t, 15.0, 15.4) * (1 - seg(t, 21.3, 21.8))
        items = [("Du siehst den Entwurf,", "bevor wir starten."),
                 ("Deine Domain", "gehört dir."),
                 ("Um die Technik", "kümmern wir uns.")]
        for i, (l1, l2) in enumerate(items):
            p = seg(t, 15.2 + i * 1.9, 15.8 + i * 1.9)
            y = 520 + i * 360 + (1 - p) * 40
            d.rounded_rectangle((90, y - 6, 100, y + 200), 5, fill=tuple(int(BG[k] + (ORANGE[k] - BG[k]) * p * a) for k in range(3)))
            text(d, (140, y), l1, font("Bold", 74), WHITE, p * a, "la")
            text(d, (140, y + 100), l2, font("Bold", 74), GREY if i != 0 else ORANGE, p * a, "la")
    # S5 CTA 21.8-27
    if t >= 21.8:
        a = seg(t, 21.8, 22.3)
        text(d, (W // 2, 640), "Wir schauen uns", font("Bold", 104), WHITE, a)
        text(d, (W // 2, 760), "deine Seite an.", font("Bold", 104), WHITE, a)
        p = seg(t, 22.6, 23.1)
        text(d, (W // 2, 930 + (1 - p) * 30), "Kostenlos und unverbindlich.", font("Medium", 56), GREY, p)
        p = seg(t, 23.4, 24.0)
        bw, bh = 700, 150; bx, by = (W - bw) // 2, 1100 + (1 - p) * 40
        col = tuple(int(BG[k] + (BLUE[k] - BG[k]) * p) for k in range(3))
        d.rounded_rectangle((bx, by, bx + bw, by + bh), 75, fill=col)
        text(d, (W // 2, by + bh // 2), "Link in der Bio", font("Bold", 62), WHITE, p, "mm")
        p = seg(t, 24.2, 24.8)
        brand(d, 1420, 84, "sherka", ".ch", p)
    return im

cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
       "-i", "-", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p",
       "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "sherka-reel.mp4"]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
n = int(TOTAL * FPS)
for i in range(n):
    p.stdin.write(frame(i / FPS).tobytes())
p.stdin.close(); p.wait()
print("done", n, "frames")
