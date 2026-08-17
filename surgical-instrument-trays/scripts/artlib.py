#!/usr/bin/env python3
"""
artlib -- a tiny 2D line-art engine on top of PIL, tuned for producing
crisp black-and-white surgical instrument diagrams for print.

Everything is drawn on a supersampled canvas (SS x) then downscaled with
LANCZOS, which gives clean anti-aliased strokes without needing a real
vector backend.

Coordinate system: logical pixels, origin top-left, y grows downward.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SS = 4  # supersample factor

FONT_DIR = "/usr/share/fonts/google-noto"
_F_REG = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
_F_BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
_F_SEMI = os.path.join(FONT_DIR, "NotoSans-SemiBold.ttf")
_F_IT = os.path.join(FONT_DIR, "NotoSans-Italic.ttf")
_F_COND = os.path.join(FONT_DIR, "NotoSans-CondensedSemiBold.ttf")

BLACK = 0
WHITE = 255
GREY = 128
LGREY = 205
MGREY = 165
DGREY = 75

_font_cache = {}


def font(size, weight="reg"):
    path = {"reg": _F_REG, "bold": _F_BOLD, "semi": _F_SEMI,
            "it": _F_IT, "cond": _F_COND}[weight]
    key = (path, int(size * SS))
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, int(size * SS))
    return _font_cache[key]


# ----------------------------------------------------------------- geometry
def rot(pt, ang, about=(0, 0)):
    """Rotate pt by ang degrees about a point."""
    a = math.radians(ang)
    x, y = pt[0] - about[0], pt[1] - about[1]
    return (about[0] + x * math.cos(a) - y * math.sin(a),
            about[1] + x * math.sin(a) + y * math.cos(a))


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def dist(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def ang_of(a, b):
    return math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))


def along(a, b, t, off=0.0):
    """Point at fraction t from a->b, offset perpendicular by off."""
    p = lerp(a, b, t)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    return (p[0] - math.sin(ang) * off, p[1] + math.cos(ang) * off)


def bezier(p0, p1, p2, p3, n=48):
    """Cubic bezier -> point list."""
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = (mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0]
             + 3 * mt * t * t * p2[0] + t ** 3 * p3[0])
        y = (mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1]
             + 3 * mt * t * t * p2[1] + t ** 3 * p3[1])
        out.append((x, y))
    return out


def quad(p0, p1, p2, n=36):
    """Quadratic bezier -> point list."""
    out = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        out.append((mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0],
                    mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]))
    return out


def arc_pts(cx, cy, r, a0, a1, n=64):
    """Points along a circular arc, angles in degrees."""
    out = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        out.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return out


def offset_path(pts, d):
    """Crude parallel offset of a polyline by distance d (left of travel)."""
    out = []
    n = len(pts)
    for i, p in enumerate(pts):
        if i == 0:
            a, b = pts[0], pts[1]
        elif i == n - 1:
            a, b = pts[-2], pts[-1]
        else:
            a, b = pts[i - 1], pts[i + 1]
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        out.append((p[0] - math.sin(ang) * d, p[1] + math.cos(ang) * d))
    return out


def ribbon(pts, w0, w1=None):
    """Closed outline of a tapering band centred on polyline pts."""
    if w1 is None:
        w1 = w0
    n = len(pts)
    up, dn = [], []
    for i, p in enumerate(pts):
        t = i / max(1, n - 1)
        h = (w0 + (w1 - w0) * t) / 2.0
        if i == 0:
            a, b = pts[0], pts[1]
        elif i == n - 1:
            a, b = pts[-2], pts[-1]
        else:
            a, b = pts[i - 1], pts[i + 1]
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        nx, ny = -math.sin(ang), math.cos(ang)
        up.append((p[0] + nx * h, p[1] + ny * h))
        dn.append((p[0] - nx * h, p[1] - ny * h))
    return up + dn[::-1]


# -------------------------------------------------------------------- canvas
class Art:
    def __init__(self, w, h, bg=WHITE):
        self.w, self.h = w, h
        self.im = Image.new("L", (int(w * SS), int(h * SS)), bg)
        self.d = ImageDraw.Draw(self.im)

    # ---- scaling helpers
    def _p(self, pt):
        return (pt[0] * SS, pt[1] * SS)

    def _pl(self, pts):
        return [(p[0] * SS, p[1] * SS) for p in pts]

    def _bbox(self, box):
        return [box[0] * SS, box[1] * SS, box[2] * SS, box[3] * SS]

    # ---- strokes
    def line(self, pts, w=1.4, fill=BLACK, joint="curve"):
        if len(pts) < 2:
            return
        self.d.line(self._pl(pts), fill=fill, width=max(1, int(w * SS)),
                    joint=joint)

    def seg(self, a, b, w=1.4, fill=BLACK):
        self.d.line([self._p(a), self._p(b)], fill=fill,
                    width=max(1, int(w * SS)))

    def poly(self, pts, w=1.4, fill=None, outline=BLACK):
        pp = self._pl(pts)
        if fill is not None:
            self.d.polygon(pp, fill=fill)
        if outline is not None:
            self.d.line(pp + [pp[0]], fill=outline,
                        width=max(1, int(w * SS)), joint="curve")

    def circle(self, c, r, w=1.4, fill=None, outline=BLACK):
        box = [c[0] - r, c[1] - r, c[0] + r, c[1] + r]
        if fill is not None:
            self.d.ellipse(self._bbox(box), fill=fill)
        if outline is not None:
            self.d.ellipse(self._bbox(box), outline=outline,
                           width=max(1, int(w * SS)))

    def ellipse(self, box, w=1.4, fill=None, outline=BLACK):
        if fill is not None:
            self.d.ellipse(self._bbox(box), fill=fill)
        if outline is not None:
            self.d.ellipse(self._bbox(box), outline=outline,
                           width=max(1, int(w * SS)))

    def rect(self, box, w=1.4, fill=None, outline=BLACK, r=0):
        if r > 0:
            if fill is not None:
                self.d.rounded_rectangle(self._bbox(box), radius=r * SS, fill=fill)
            if outline is not None:
                self.d.rounded_rectangle(self._bbox(box), radius=r * SS,
                                         outline=outline, width=max(1, int(w * SS)))
        else:
            if fill is not None:
                self.d.rectangle(self._bbox(box), fill=fill)
            if outline is not None:
                self.d.rectangle(self._bbox(box), outline=outline,
                                 width=max(1, int(w * SS)))

    def arc(self, c, r, a0, a1, w=1.4, fill=BLACK):
        self.line(arc_pts(c[0], c[1], r, a0, a1), w=w, fill=fill)

    def ring(self, c, ro, ri, w=1.4, fill=None):
        """Annulus: outer + inner circle, optional grey fill between."""
        if fill is not None:
            self.circle(c, ro, fill=fill, outline=None)
            self.circle(c, ri, fill=WHITE, outline=None)
        self.circle(c, ro, w=w)
        self.circle(c, ri, w=w)

    def band(self, pts, w0, w1=None, lw=1.4, fill=None):
        self.poly(ribbon(pts, w0, w1), w=lw, fill=fill)

    def dash(self, a, b, w=1.0, fill=BLACK, on=3.0, off=2.5):
        L = dist(a, b)
        if L <= 0:
            return
        t = 0.0
        while t < L:
            t2 = min(L, t + on)
            self.seg(lerp(a, b, t / L), lerp(a, b, t2 / L), w=w, fill=fill)
            t = t2 + off

    def dash_path(self, pts, w=1.0, fill=BLACK, on=3.0, off=2.5):
        for i in range(len(pts) - 1):
            self.dash(pts[i], pts[i + 1], w=w, fill=fill, on=on, off=off)

    # ---- textures
    def hatch(self, box, step=3.0, w=0.7, fill=MGREY, ang=45):
        """Diagonal hatch clipped to a rectangle (approximate)."""
        x0, y0, x1, y1 = box
        n = int((abs(x1 - x0) + abs(y1 - y0)) / step) + 2
        for i in range(-n, n):
            if ang == 45:
                a = (x0 + i * step, y0)
                b = (x0 + i * step + (y1 - y0), y1)
            else:
                a = (x0 + i * step, y1)
                b = (x0 + i * step + (y1 - y0), y0)
            # clip crudely
            self._clipseg(a, b, box, w, fill)

    def _clipseg(self, a, b, box, w, fill):
        x0, y0, x1, y1 = box
        pts = []
        for t in [i / 60 for i in range(61)]:
            p = lerp(a, b, t)
            if x0 <= p[0] <= x1 and y0 <= p[1] <= y1:
                pts.append(p)
        if len(pts) >= 2:
            self.seg(pts[0], pts[-1], w=w, fill=fill)

    def serrate(self, a, b, n=9, depth=1.5, w=0.9, fill=BLACK):
        """Zig-zag teeth along segment a->b (jaw serrations)."""
        pts = []
        for i in range(n * 2 + 1):
            t = i / (n * 2)
            pts.append(along(a, b, t, depth if i % 2 else 0))
        self.line(pts, w=w, fill=fill)

    def cross_serrate(self, a, b, n=12, depth=1.6, w=0.8, fill=DGREY):
        """Short transverse strokes -- the usual 'serrated jaw' look."""
        for i in range(n + 1):
            t = i / n
            p1 = along(a, b, t, -depth)
            p2 = along(a, b, t, depth)
            self.seg(p1, p2, w=w, fill=fill)

    def teeth(self, a, b, n=4, depth=2.6, w=1.1, fill=BLACK):
        """Sharp triangular teeth pointing perpendicular (tissue forceps)."""
        for i in range(n):
            t0 = (i + 0.15) / n
            t1 = (i + 0.85) / n
            tm = (t0 + t1) / 2
            self.poly([along(a, b, t0, 0), along(a, b, tm, depth),
                       along(a, b, t1, 0)], w=w, fill=BLACK)

    def ratchet(self, a, b, n=4, depth=1.8, w=1.0):
        """Ratchet / lock teeth bar."""
        self.seg(a, b, w=w)
        for i in range(n):
            t = (i + 0.5) / n
            self.seg(along(a, b, t, 0), along(a, b, t, depth), w=w)

    def screw(self, c, r, w=1.0):
        self.circle(c, r, w=w)
        self.seg((c[0] - r * 0.62, c[1]), (c[0] + r * 0.62, c[1]), w=w)

    def knurl(self, box, n=10, w=0.8, fill=DGREY):
        x0, y0, x1, y1 = box
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n
            self.seg((x, y0), (x, y1), w=w, fill=fill)

    # ---- text
    def text(self, pt, s, size=11, weight="reg", fill=BLACK,
             anchor="lt", angle=0, leading=1.22):
        f = font(size, weight)
        # PIL cannot anchor multiline text -- lay the lines out ourselves.
        if "\n" in s and not angle:
            lines = s.split("\n")
            lh = size * leading
            n = len(lines)
            v = anchor[1] if len(anchor) > 1 else "t"
            if v == "t" or v == "a":
                y0 = pt[1]
            elif v == "m":
                y0 = pt[1] - (n - 1) * lh / 2.0
            else:                      # b, s, d -> block sits above the point
                y0 = pt[1] - (n - 1) * lh
            va = "t" if v in ("t", "a") else ("m" if v == "m" else v)
            for i, ln in enumerate(lines):
                if not ln:
                    continue
                self.d.text(self._p((pt[0], y0 + i * lh)), ln, font=f,
                            fill=fill, anchor=anchor[0] + va)
            return
        if angle:
            tmp = Image.new("L", (int(size * SS * len(s) * 1.2) + 20,
                                  int(size * SS * 2) + 20), WHITE)
            td = ImageDraw.Draw(tmp)
            td.text((5, 5), s, font=f, fill=fill)
            tmp = tmp.rotate(angle, expand=True, fillcolor=WHITE)
            self.im.paste(tmp, (int(pt[0] * SS), int(pt[1] * SS)), )
            return
        self.d.text(self._p(pt), s, font=f, fill=fill, anchor=anchor)

    def tsize(self, s, size=11, weight="reg"):
        f = font(size, weight)
        bb = self.d.textbbox((0, 0), s, font=f)
        return ((bb[2] - bb[0]) / SS, (bb[3] - bb[1]) / SS)

    def label(self, tip, txt, side="r", size=10.5, weight="semi",
              lead=14, dotr=1.5, w=0.9, fill=BLACK, gap=2.5, elbow=None):
        """Leader-line label: dot at `tip`, line out, text at the end."""
        if side == "r":
            end = (tip[0] + lead, tip[1])
            anchor, tx = "lm", (end[0] + gap, end[1])
        elif side == "l":
            end = (tip[0] - lead, tip[1])
            anchor, tx = "rm", (end[0] - gap, end[1])
        elif side == "u":
            end = (tip[0], tip[1] - lead)
            anchor, tx = "mb", (end[0], end[1] - gap)
        else:
            end = (tip[0], tip[1] + lead)
            anchor, tx = "mt", (end[0], end[1] + gap)
        if elbow is not None:
            self.line([tip, elbow, end], w=w, fill=fill)
        else:
            self.seg(tip, end, w=w, fill=fill)
        if dotr:
            self.circle(tip, dotr, fill=fill, outline=None)
        self.text(tx, txt, size=size, weight=weight, fill=fill, anchor=anchor)

    def caption(self, txt, size=11.5, weight="bold", pad=3):
        """Centred caption at the bottom of the canvas."""
        self.text((self.w / 2, self.h - pad), txt, size=size, weight=weight,
                  anchor="ms")

    def frame(self, w=1.0, fill=LGREY, inset=0.5):
        self.rect([inset, inset, self.w - inset, self.h - inset],
                  w=w, outline=fill)

    def scalebar(self, x, y, length, txt, size=8.5):
        self.seg((x, y), (x + length, y), w=1.0)
        self.seg((x, y - 2), (x, y + 2), w=1.0)
        self.seg((x + length, y - 2), (x + length, y + 2), w=1.0)
        self.text((x + length / 2, y + 3), txt, size=size, weight="reg",
                  anchor="mt", fill=DGREY)

    # ---- output
    def save(self, path, trim=False, pad=6, scale=1.0, colors=8):
        """
        Write the figure as a PNG.

        scale  -- output pixels per logical unit. 1.0 keeps the logical
                  size; raise it for figures printed large, so they stay
                  crisp on paper (line art wants >=200 dpi at final size).
        colors -- quantise to this many grey levels. Line art needs very
                  few, and doing so cuts the file size by more than half
                  with no visible difference. Pass None to keep 8-bit grey.
        """
        im = self.im
        if trim:
            bb = Image.eval(im, lambda v: 255 - v).getbbox()
            if bb:
                bb = (max(0, bb[0] - pad * SS), max(0, bb[1] - pad * SS),
                      min(im.width, bb[2] + pad * SS),
                      min(im.height, bb[3] + pad * SS))
                im = im.crop(bb)
        tw = max(1, int(round(im.width / SS * scale)))
        th = max(1, int(round(im.height / SS * scale)))
        im = im.resize((tw, th), Image.LANCZOS)
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        if colors:
            q = im.quantize(colors=colors, method=Image.MEDIANCUT)
            bits = max(1, (colors - 1).bit_length())
            q.save(path, "PNG", optimize=True, bits=bits)
        else:
            im.save(path, "PNG", optimize=True)
        return im.size


# ==================================================================
#  Re-usable instrument builders
# ==================================================================
def ring_handle_instrument(a, origin=(0, 0), L=150, jaw="serrated",
                           jaw_len=34, curve=0.0, ring_r=11.0, shank_w=4.2,
                           lock=True, jaw_w=5.0, teeth_n=4, ang=0.0,
                           open_deg=7.0, tip="blunt"):
    """
    Draw a classic ring-handled instrument (hemostat / clamp / scissors /
    needle holder) pointing to the RIGHT from `origin`.

    jaw: serrated | cross | teeth | scissor | needle | tapered | atraumatic | babcock | allis
    """
    ox, oy = origin
    # `L` is the TRUE overall length: handle section + jaws.
    box_x = ox + max(L * 0.30, L - jaw_len - 4.2)   # box-lock position
    handle_end = ox
    jaw_start = box_x

    def R(p):
        return rot(p, ang, (ox, oy))

    # ---------------- handles (two rings + shanks) ----------------
    for sgn in (-1, 1):
        ry = oy + sgn * (ring_r + 2.0)
        ring_c = (handle_end + ring_r, ry)
        # ring
        a.ring(R(ring_c), ring_r, ring_r * 0.58, w=1.5)
        # shank from ring to box lock
        p0 = (handle_end + ring_r * 1.85, ry + sgn * -1.0)
        p1 = (box_x - (box_x - p0[0]) * 0.42, ry * 0.55 + oy * 0.45)
        p2 = (box_x, oy + sgn * shank_w * 0.42)
        pts = [R(p) for p in quad(p0, p1, p2, 28)]
        a.band(pts, shank_w, shank_w * 0.92, lw=1.4)
        # ratchet lock arm
        if lock and sgn == 1:
            lx0 = handle_end + ring_r * 2.15
            a.ratchet(R((lx0, ry - ring_r * 0.15)),
                      R((lx0 + 13, ry - ring_r * 0.15 - 4)), n=4, depth=-2.0, w=1.0)

    # box lock
    a.rect([box_x - 3.4, oy - shank_w * 0.95, box_x + 4.6, oy + shank_w * 0.95],
           w=1.5, r=1.2)
    a.screw((box_x + 0.6, oy), 1.5, w=1.0)

    # ---------------- jaws ----------------
    jx0 = jaw_start + 4.2
    jx1 = jx0 + jaw_len
    for sgn in (-1, 1):
        spread = open_deg * sgn
        if abs(curve) > 0.01:
            # curved jaw: arc bending "up"
            base = (jx0, oy + sgn * jaw_w * 0.30)
            ctrl = (jx0 + jaw_len * 0.55, oy - jaw_len * curve * 0.35
                    + sgn * jaw_w * 0.30)
            tipp = (jx1 - jaw_len * 0.06, oy - jaw_len * curve * 0.72)
            path = quad(base, ctrl, tipp, 26)
        else:
            base = (jx0, oy + sgn * jaw_w * 0.30)
            tipp = (jx1, oy + sgn * spread * 0.35)
            path = [lerp(base, tipp, i / 20) for i in range(21)]

        pth = [R(p) for p in path]

        if jaw == "scissor":
            a.band(pth, jaw_w * 1.12, 1.1, lw=1.4)
            if sgn == 1:  # cutting edge highlight
                e = offset_path(pth, -jaw_w * 0.22)
                a.line(e, w=0.8, fill=DGREY)
        elif jaw == "needle":
            a.band(pth, jaw_w * 1.15, jaw_w * 0.72, lw=1.4)
            if sgn == 1:
                a.cross_serrate(pth[2], pth[-3], n=10, depth=jaw_w * 0.30, w=0.8)
        elif jaw == "teeth":
            a.band(pth, jaw_w, 1.6, lw=1.4)
            if sgn == 1:
                a.teeth(pth[3], pth[-2], n=teeth_n,
                        depth=-2.4, w=1.0)
        elif jaw == "allis":
            a.band(pth, jaw_w * 0.95, 2.2, lw=1.4)
            # interlocking sharp teeth face each other
            a.teeth(pth[-6], pth[-1], n=3, depth=-sgn * 3.0, w=1.0)
        elif jaw == "babcock":
            # fenestrated triangular loop tip
            a.band(pth[:-8], jaw_w * 0.95, jaw_w * 0.75, lw=1.4)
            lp = pth[-9:]
            outer = ribbon(lp, jaw_w * 1.5, jaw_w * 1.15)
            a.poly(outer, w=1.4)
            inner = ribbon(lp[1:-1], jaw_w * 0.55, jaw_w * 0.35)
            a.poly(inner, w=1.0, outline=DGREY)
        elif jaw == "atraumatic":
            a.band(pth, jaw_w, jaw_w * 0.55, lw=1.4)
            if sgn == 1:
                a.line(offset_path(pth, -jaw_w * 0.2), w=0.7, fill=MGREY)
                a.line(offset_path(pth, -jaw_w * 0.05), w=0.7, fill=MGREY)
        elif jaw == "tapered":
            a.band(pth, jaw_w, 1.3, lw=1.4)
            if sgn == 1:
                a.cross_serrate(pth[1], pth[-4], n=11, depth=jaw_w * 0.26, w=0.75)
        elif jaw == "cross":
            a.band(pth, jaw_w, jaw_w * 0.68, lw=1.4)
            if sgn == 1:
                a.cross_serrate(pth[1], pth[-2], n=13, depth=jaw_w * 0.30, w=0.8)
        else:  # serrated (longitudinal)
            a.band(pth, jaw_w, jaw_w * 0.66, lw=1.4)
            if sgn == 1:
                a.line(offset_path(pth, 0), w=0.7, fill=MGREY)
                a.serrate(pth[1], pth[-2], n=8, depth=-jaw_w * 0.22, w=0.7,
                          fill=DGREY)
    return {"box": R((box_x, oy)), "tip": R((jx1, oy)),
            "rings": (R((ox + ring_r, oy - ring_r - 2)),
                      R((ox + ring_r, oy + ring_r + 2)))}


def thumb_forceps(a, origin=(0, 0), L=110, tip="toothed", ang=0.0,
                  w_top=7.0, open_deg=9.0, teeth_n=2, serr=True,
                  platform=False):
    """
    Spring (thumb / dressing / tissue) forceps pointing RIGHT.
    tip: toothed | serrated | smooth | adson | debakey | fine | dissect
    """
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    hinge = (ox, oy)
    tipx = ox + L
    for sgn in (-1, 1):
        # arm: wide at hinge -> narrow shoulder -> tip
        p0 = (ox + 1.0, oy + sgn * 0.6)
        p1 = (ox + L * 0.34, oy + sgn * (w_top * 0.92))
        p2 = (ox + L * 0.74, oy + sgn * (w_top * 0.52))
        p3 = (tipx, oy + sgn * (open_deg * 0.30 + 0.5))
        path = bezier(p0, p1, p2, p3, 40)
        pth = [R(p) for p in path]
        wid = 3.0 if tip in ("adson", "fine", "debakey") else 3.5
        a.band(pth, 2.0, wid * 0.55, lw=1.4)

        # finger platform (knurled grip zone)
        if platform or tip in ("adson", "debakey", "serrated", "toothed"):
            i0, i1 = int(len(pth) * 0.30), int(len(pth) * 0.50)
            a.cross_serrate(pth[i0], pth[i1], n=5,
                            depth=wid * 0.30, w=0.6, fill=MGREY)

        # tips
        t0, t1 = pth[-7], pth[-1]
        if tip == "toothed":
            if sgn == 1:
                a.teeth(t0, t1, n=teeth_n, depth=-2.4, w=1.0)
        elif tip == "adson":
            if sgn == 1:
                a.teeth(t0, t1, n=2, depth=-1.9, w=0.9)
        elif tip == "debakey":
            a.line(offset_path(pth[-12:], -sgn * 0.5), w=0.7, fill=MGREY)
            if sgn == 1:
                a.cross_serrate(pth[-13], pth[-1], n=8, depth=1.0, w=0.6,
                                fill=MGREY)
        elif tip in ("serrated", "dissect"):
            if sgn == 1:
                a.cross_serrate(t0, t1, n=5, depth=1.2, w=0.7)

    # hinge / spring joint
    a.poly([R((ox - 5.5, oy - 3.2)), R((ox + 2.0, oy - 1.4)),
            R((ox + 2.0, oy + 1.4)), R((ox - 5.5, oy + 3.2))], w=1.4)
    a.arc(R((ox - 4.0, oy)), 3.2, 90, 270, w=1.4)
    return {"tip": R((tipx, oy)), "hinge": R(hinge)}


def scalpel(a, origin=(0, 0), L=120, blade="10", ang=0.0, handle_no="4"):
    """Scalpel handle with a mounted blade, pointing RIGHT."""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    hl = L * 0.74
    # handle: flat, slightly tapered, knurled mid-section
    body = [(ox, oy - 3.4), (ox + hl * 0.86, oy - 4.2),
            (ox + hl, oy - 3.0), (ox + hl, oy + 3.0),
            (ox + hl * 0.86, oy + 4.2), (ox, oy + 3.4)]
    a.poly([R(p) for p in body], w=1.5)
    a.arc(R((ox + 1.2, oy)), 3.4, 90, 270, w=1.5)
    a.knurl([ox + hl * 0.14, oy - 3.2, ox + hl * 0.55, oy + 3.2], n=13, w=0.7)
    # scale markings
    a.text(R((ox + hl * 0.70, oy + 0.2)), f"No.{handle_no}", size=6.5,
           weight="semi", anchor="mm", fill=DGREY)

    # blade-mounting shank on the handle (blade slides onto this)
    a.poly([R((ox + hl - 2, oy - 2.4)), R((ox + hl + 9, oy - 1.9)),
            R((ox + hl + 9, oy + 1.9)), R((ox + hl - 2, oy + 2.4))],
           w=1.2, fill=LGREY)

    bx = ox + hl - 1          # overlap so blade sits ON the shank
    bl = L - hl + 1
    H = max(4.4, bl * 0.17)   # half-height of blade body (~3:1 aspect)
    if blade == "10":
        # straight back on top, convex cutting belly below, rounded tip
        back = [(bx, oy - 2.2), (bx + bl * 0.22, oy - H),
                (bx + bl * 0.72, oy - H - 0.6)]
        nose = quad((bx + bl * 0.72, oy - H - 0.6),
                    (bx + bl * 1.00, oy - H + 0.8), (bx + bl, oy + 0.4), 22)
        belly = quad((bx + bl, oy + 0.4), (bx + bl * 0.46, oy + H + 1.4),
                     (bx, oy + 2.2), 26)
        outline = back + nose + belly
        edge = belly
    elif blade == "11":   # straight, sharp stab point
        outline = [(bx, oy - 2.2), (bx + bl * 0.16, oy - H),
                   (bx + bl, oy + 1.6), (bx + bl * 0.20, oy + H - 0.4),
                   (bx, oy + 2.2)]
        edge = [(bx + bl, oy + 1.6), (bx + bl * 0.20, oy + H - 0.4)]
    elif blade == "12":   # crescent / sickle hook
        outline = (quad((bx, oy - 2.2), (bx + bl * 0.62, oy - H - 2.4),
                        (bx + bl, oy - 0.4), 24)
                   + quad((bx + bl, oy - 0.4), (bx + bl * 0.55, oy + 1.0),
                          (bx, oy + 2.2), 20))
        edge = quad((bx + bl, oy - 0.4), (bx + bl * 0.55, oy + 1.0),
                    (bx, oy + 2.2), 20)
    elif blade == "15":   # short, small curved belly
        back = [(bx, oy - 2.2), (bx + bl * 0.34, oy - H + 0.6),
                (bx + bl * 0.70, oy - H + 0.2)]
        nose = quad((bx + bl * 0.70, oy - H + 0.2),
                    (bx + bl, oy - H + 2.0), (bx + bl, oy + 1.0), 20)
        belly = quad((bx + bl, oy + 1.0), (bx + bl * 0.42, oy + H),
                     (bx, oy + 2.2), 22)
        outline = back + nose + belly
        edge = belly
    elif blade == "20":   # large #10 pattern
        H2 = H + 2.2
        back = [(bx, oy - 2.6), (bx + bl * 0.20, oy - H2),
                (bx + bl * 0.74, oy - H2 - 0.8)]
        nose = quad((bx + bl * 0.74, oy - H2 - 0.8),
                    (bx + bl * 1.02, oy - H2 + 1.0), (bx + bl, oy + 0.6), 22)
        belly = quad((bx + bl, oy + 0.6), (bx + bl * 0.46, oy + H2 + 1.6),
                     (bx, oy + 2.6), 26)
        outline = back + nose + belly
        edge = belly
    else:
        outline = [(bx, oy - 2.2), (bx + bl, oy - 1.0), (bx + bl, oy + 3.0)]
        edge = None

    a.poly([R(p) for p in outline], w=1.4, fill=LGREY)
    a.poly([R(p) for p in outline], w=1.4, fill=None)
    # highlight the cutting edge with a second inboard line
    if edge:
        a.line([R(p) for p in offset_path(edge, 1.1)], w=0.8, fill=DGREY)
    # blade slot (the keyhole that grips the handle shank)
    a.poly([R((bx + 2.5, oy - 1.0)), R((bx + 10, oy - 1.0)),
            R((bx + 10, oy + 1.4)), R((bx + 2.5, oy + 1.4))],
           w=1.0, fill=WHITE)
    return {"tip": R((bx + bl, oy)), "handle": R((ox + hl * 0.4, oy))}


def handheld_retractor(a, origin=(0, 0), L=130, kind="army", ang=0.0):
    """
    Hand-held retractor pointing RIGHT; blade at the right end.
    kind: army | richardson | deaver | malleable | senn | rake | ribbon
    """
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "army":
        # PROFILE view: flat shaft, a 90-degree blade at each end pointing
        # in opposite directions (shallow one end, deep the other).
        th = 3.0                      # shaft thickness in profile
        d1, d2 = 13.0, 20.0           # blade depths
        bw = 4.0                      # blade thickness
        outline = [
            (ox, oy - th), (ox + L, oy - th),
            (ox + L, oy - th - d2), (ox + L - bw, oy - th - d2),
            (ox + L - bw, oy + th), (ox + bw, oy + th),
            (ox + bw, oy + th + d1), (ox, oy + th + d1),
        ]
        a.poly([R(p) for p in outline], w=1.5)
        # lip at each blade end
        a.seg(R((ox, oy + th + d1)), R((ox - 3.5, oy + th + d1 - 3.0)), w=1.5)
        a.seg(R((ox + L, oy - th - d2)), R((ox + L + 3.5, oy - th - d2 + 3.0)),
              w=1.5)
        a.knurl([ox + L * 0.34, oy - th + 0.4, ox + L * 0.66, oy + th - 0.4],
                n=11, w=0.7)
    elif kind == "richardson":
        # PROFILE: hollow grip handle -> shaft -> deep right-angle blade
        th = 3.2
        d = 22.0
        bw = 4.2
        sx = ox + L * 0.78
        outline = [
            (ox, oy - th - 1.6), (sx, oy - th),
            (sx + bw + 6, oy - th),
            (sx + bw + 6, oy + th + d - 5),           # blade back
            (sx + bw + 1, oy + th + d),               # curved lip
            (sx - 1.5, oy + th + d),
            (sx - 1.5, oy + th), (ox, oy + th + 1.6),
        ]
        a.poly([R(p) for p in outline], w=1.5)
        # rolled lip on blade
        a.line([R((sx - 1.5, oy + th + d)), R((sx - 5.0, oy + th + d - 2.5)),
                R((sx - 3.0, oy + th + d - 6.0))], w=1.4)
        # hollow finger-grip fenestration in handle
        a.rect([ox + 4, oy - 2.0, ox + L * 0.30, oy + 2.0], w=1.1, r=2.0,
               outline=DGREY)
        a.knurl([ox + L * 0.38, oy - 2.4, ox + L * 0.66, oy + 2.4], n=9, w=0.6)
    elif kind == "deaver":
        # PROFILE: long slender shaft with a gently curved shallow blade
        th = 2.6
        sx = ox + L * 0.55
        spine = quad((sx, oy), (sx + L * 0.30, oy + 6), (sx + L * 0.40, oy + 30), 34)
        a.poly([R(p) for p in
                [(ox, oy - th - 1.2), (sx, oy - th)]
                + offset_path(spine, -th)
                + [(spine[-1][0] + 1.0, spine[-1][1] + 2.0)]
                + offset_path(spine, th)[::-1]
                + [(sx, oy + th), (ox, oy + th + 1.2)]], w=1.5)
        a.rect([ox + 3, oy - 1.6, ox + L * 0.26, oy + 1.6], w=1.0, r=1.6,
               outline=DGREY)
        a.text(R((sx + L * 0.16, oy + 16)), "narrow", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind in ("malleable", "ribbon"):
        pts = quad((ox, oy + 6), (ox + L * 0.55, oy - 14), (ox + L, oy + 6), 40)
        a.band([R(p) for p in pts], 17, 17, lw=1.5)
        a.line([R(p) for p in offset_path(pts, 0)], w=0.7, fill=LGREY)
        a.text(R((ox + L * 0.5, oy - 2)), "malleable", size=6.5, weight="it",
               anchor="mm", fill=MGREY)
    elif kind == "senn":
        a.band([R((ox, oy)), R((ox + L * 0.78, oy))], 5.0, 5.6, lw=1.5)
        a.knurl([ox + L * 0.14, oy - 2.6, ox + L * 0.46, oy + 2.6], n=10, w=0.6)
        # flat blade one end
        a.poly([R((ox, oy - 2.6)), R((ox - 10, oy - 5.5)),
                R((ox - 10, oy + 5.5)), R((ox, oy + 2.6))], w=1.5)
        # 3 sharp prongs other end
        x = ox + L * 0.78
        a.band([R((x, oy)), R((x + 7, oy))], 5.6, 5.6, lw=1.4)
        for k in (-1, 0, 1):
            base = (x + 7, oy + k * 3.0)
            a.poly([R(base), R((x + 14, oy + k * 3.6 + 6)),
                    R((x + 9, oy + k * 3.0 + 1.6))], w=1.2, fill=BLACK)
    elif kind == "rake":
        a.band([R((ox, oy)), R((ox + L * 0.72, oy))], 6.0, 6.6, lw=1.5)
        a.ellipse([ox + 2, oy - 2.4, ox + L * 0.20, oy + 2.4], w=1.0,
                  outline=DGREY)
        x = ox + L * 0.72
        a.poly([R((x, oy - 3.3)), R((x + 8, oy - 12)), R((x + 8, oy + 12)),
                R((x, oy + 3.3))], w=1.5)
        for k in range(6):
            yy = oy - 10 + k * 4
            a.poly([R((x + 8, yy - 1.2)), R((x + 20, yy + 2.0)),
                    R((x + 8, yy + 1.6))], w=1.1, fill=BLACK)
    return {"blade": R((ox + L, oy))}


def suction_tip(a, origin=(0, 0), L=130, kind="yankauer", ang=0.0):
    """kind: yankauer | poole | frazier"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "yankauer":
        shaft = quad((ox, oy), (ox + L * 0.55, oy - 2), (ox + L * 0.80, oy - 16), 34)
        a.band([R(p) for p in shaft], 8.0, 6.4, lw=1.5)
        a.line([R(p) for p in offset_path(shaft, 0)], w=0.7, fill=LGREY)
        # bulbous fenestrated tip
        t = shaft[-1]
        a.circle(R((t[0] + 1.5, t[1] - 4.0)), 6.2, w=1.5)
        for dx, dy in ((-2.2, -1.0), (2.2, -1.0), (0, -4.2), (0, 2.0)):
            a.circle(R((t[0] + 1.5 + dx, t[1] - 4.0 + dy)), 1.15, w=0.9,
                     fill=WHITE)
        # thumb port + connector
        a.rect([ox - 12, oy - 5.5, ox + 3, oy + 5.5], w=1.5, r=2.5)
        a.circle(R((ox - 4.5, oy)), 2.6, w=1.2)
        a.band([R((ox - 24, oy)), R((ox - 11, oy))], 9.0, 7.5, lw=1.5)
    elif kind == "poole":
        a.band([R((ox, oy)), R((ox + L * 0.60, oy))], 8.5, 8.5, lw=1.5)
        # outer perforated sheath
        x0 = ox + L * 0.60
        a.rect([x0, oy - 8.5, x0 + L * 0.40, oy + 8.5], w=1.5, r=8.0)
        for i in range(7):
            for j in (-1, 1):
                a.circle(R((x0 + 7 + i * 6.2, oy + j * 3.6)), 1.5, w=0.9)
        a.dash_path([R((x0, oy)), R((x0 + L * 0.40, oy))], w=0.7, fill=MGREY)
        a.band([R((ox - 20, oy)), R((ox - 1, oy))], 9.5, 8.5, lw=1.5)
        a.text(R((x0 + L * 0.20, oy + 12)), "perforated shield", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    else:  # frazier -- fine, angled, with thumb vent
        p = quad((ox, oy), (ox + L * 0.62, oy + 1), (ox + L * 0.86, oy - 22), 34)
        a.band([R(q) for q in p], 5.4, 3.2, lw=1.5)
        a.rect([ox - 10, oy - 4.2, ox + 2, oy + 4.2], w=1.5, r=2.0)
        a.circle(R((ox - 4.0, oy - 0.2)), 2.2, w=1.2)   # thumb vent
        a.band([R((ox - 22, oy)), R((ox - 9, oy))], 6.8, 5.6, lw=1.5)
        a.text(R((ox - 4.0, oy - 7.5)), "vent", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
    return {"tip": R((ox + L, oy))}



def tip_detail(a, c, r=26, kind="1x2", label=None, size=8.5):
    """
    A magnified circular 'tip detail' inset -- the convention used in
    instrument catalogue plates. Draws the jaw tips greatly enlarged
    inside a circle at centre c.

    kind: 1x2 | ratteeth | serrated | smooth | debakey | allis | babcock
          | kocher | scissor | needle
    """
    cx, cy = c
    a.circle(c, r, w=1.6)
    # clip guide: everything is drawn well inside the circle
    g = r * 0.72

    if kind in ("1x2", "ratteeth"):
        n_up, n_dn = (1, 2) if kind == "1x2" else (2, 3)
        for sgn, n in ((-1, n_up), (1, n_dn)):
            y = cy + sgn * g * 0.34
            a.poly([(cx - g, y - sgn * g * 0.30), (cx + g * 0.55, y),
                    (cx - g, y + sgn * g * 0.06)], w=1.4, fill=LGREY)
            for i in range(n):
                xx = cx + g * 0.10 - i * g * 0.30
                a.poly([(xx, y), (xx + g * 0.10, y - sgn * g * 0.30),
                        (xx + g * 0.20, y)], w=1.2, fill=BLACK)
    elif kind == "serrated":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.30
            a.poly([(cx - g, y - sgn * g * 0.26), (cx + g * 0.62, y),
                    (cx - g, y + sgn * g * 0.04)], w=1.4, fill=LGREY)
            a.cross_serrate((cx - g * 0.75, y), (cx + g * 0.45, y),
                            n=7, depth=g * 0.10, w=0.9)
    elif kind == "smooth":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.26
            a.poly([(cx - g, y - sgn * g * 0.26), (cx + g * 0.66, y),
                    (cx - g, y + sgn * g * 0.02)], w=1.4, fill=LGREY)
    elif kind == "debakey":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.30
            a.poly([(cx - g, y - sgn * g * 0.28), (cx + g * 0.68, y),
                    (cx - g, y + sgn * g * 0.04)], w=1.4, fill=LGREY)
            # fine longitudinal rows -- the DeBakey 'atraumatic' pattern
            for k in (0.30, 0.62):
                a.line([(cx - g * 0.80, y - sgn * g * k * 0.30),
                        (cx + g * 0.40, y - sgn * g * k * 0.10)],
                       w=0.8, fill=DGREY)
            a.cross_serrate((cx - g * 0.78, y), (cx + g * 0.42, y),
                            n=10, depth=g * 0.07, w=0.6, fill=MGREY)
    elif kind == "kocher":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.30
            a.poly([(cx - g, y - sgn * g * 0.28), (cx + g * 0.50, y),
                    (cx - g, y + sgn * g * 0.04)], w=1.4, fill=LGREY)
            a.cross_serrate((cx - g * 0.80, y), (cx + g * 0.30, y),
                            n=7, depth=g * 0.09, w=0.8)
        # single interlocking tooth at the very tip
        a.poly([(cx + g * 0.40, cy - g * 0.30), (cx + g * 0.72, cy),
                (cx + g * 0.40, cy + g * 0.02)], w=1.3, fill=BLACK)
        a.poly([(cx + g * 0.40, cy + g * 0.30), (cx + g * 0.72, cy),
                (cx + g * 0.40, cy - g * 0.02)], w=1.3, fill=BLACK)
    elif kind == "allis":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.42
            a.poly([(cx - g, y - sgn * g * 0.24), (cx + g * 0.55, y),
                    (cx - g, y + sgn * g * 0.06)], w=1.4, fill=LGREY)
            for i in range(4):
                xx = cx - g * 0.30 + i * g * 0.22
                a.poly([(xx, y), (xx + g * 0.08, y - sgn * g * 0.26),
                        (xx + g * 0.16, y)], w=1.1, fill=BLACK)
    elif kind == "babcock":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.40
            band = [(cx - g, y), (cx - g * 0.2, y - sgn * g * 0.10),
                    (cx + g * 0.60, y - sgn * g * 0.04)]
            a.band(band, g * 0.26, g * 0.34, lw=1.4)
            a.ellipse([cx - g * 0.10, y - sgn * g * 0.10 - g * 0.09,
                       cx + g * 0.50, y - sgn * g * 0.10 + g * 0.09],
                      w=1.0, outline=DGREY)
    elif kind == "scissor":
        a.poly([(cx - g, cy - g * 0.46), (cx + g * 0.70, cy - g * 0.04),
                (cx - g, cy - g * 0.16)], w=1.4, fill=LGREY)
        a.poly([(cx - g, cy + g * 0.46), (cx + g * 0.70, cy + g * 0.04),
                (cx - g, cy + g * 0.16)], w=1.4, fill=LGREY)
        a.seg((cx - g * 0.9, cy - g * 0.30), (cx + g * 0.62, cy - g * 0.04),
              w=0.8, fill=DGREY)
    elif kind == "needle":
        for sgn in (-1, 1):
            y = cy + sgn * g * 0.28
            a.poly([(cx - g, y - sgn * g * 0.30), (cx + g * 0.62, y),
                    (cx - g, y + sgn * g * 0.02)], w=1.4, fill=LGREY)
        # cross-hatched carbide insert
        a.rect([cx - g * 0.55, cy - g * 0.24, cx + g * 0.45, cy + g * 0.24],
               w=1.0, outline=DGREY)
        a.hatch([cx - g * 0.55, cy - g * 0.24, cx + g * 0.45, cy + g * 0.24],
                step=g * 0.13, w=0.6, fill=MGREY, ang=45)
        a.hatch([cx - g * 0.55, cy - g * 0.24, cx + g * 0.45, cy + g * 0.24],
                step=g * 0.13, w=0.6, fill=MGREY, ang=135)

    if label:
        a.text((cx, cy + r + 3), label, size=size, weight="semi", anchor="mt")


def zoom_link(a, tip, inset_c, inset_r, w=0.8, fill=GREY):
    """Dashed 'magnifier' leader from an instrument tip to its detail inset."""
    ang = ang_of(tip, inset_c)
    edge = (inset_c[0] - inset_r * math.cos(math.radians(ang)),
            inset_c[1] - inset_r * math.sin(math.radians(ang)))
    a.circle(tip, 5.0, w=w, outline=fill)
    a.dash(tip, edge, w=w, fill=fill, on=3.0, off=2.5)
