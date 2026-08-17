#!/usr/bin/env python3
"""
artlib2 -- additional instrument builders (specialty trays):
specula, dilators, curettes, endoscopes, bone instruments,
self-retaining retractors, vascular clamps, ENT and ophthalmic items,
plus OR furniture / layout primitives.
"""
import math

from artlib import (Art, BLACK, WHITE, GREY, LGREY, MGREY, DGREY, SS,
                    rot, lerp, dist, ang_of, along, bezier, quad, arc_pts,
                    offset_path, ribbon, ring_handle_instrument,
                    thumb_forceps, scalpel, handheld_retractor, suction_tip,
                    tip_detail, zoom_link)


# ------------------------------------------------------------------ specula
def speculum(a, origin=(0, 0), L=110, kind="graves", ang=0.0):
    """kind: graves | sims | nasal | ear | eyelid"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "graves":
        # duck-bill: two hinged blades, thumb screw, angled handle
        up = quad((ox, oy - 5), (ox + L * 0.55, oy - 15), (ox + L, oy - 9), 30)
        dn = quad((ox, oy + 5), (ox + L * 0.55, oy + 15), (ox + L, oy + 9), 30)
        a.band([R(p) for p in up], 5.0, 3.4, lw=1.5)
        a.band([R(p) for p in dn], 5.0, 3.4, lw=1.5)
        # hinge block + handle going down-left
        a.rect([ox - 9, oy - 6.5, ox + 2, oy + 6.5], w=1.5, r=2)
        h = [(ox - 5, oy + 6), (ox - 16, oy + 34)]
        a.band([R(p) for p in h], 9.0, 11.0, lw=1.5)
        a.knurl([ox - 16, oy + 20, ox - 7, oy + 32], n=5, w=0.7)
        # thumb screw on the arm
        a.seg(R((ox - 4, oy - 6)), R((ox - 4, oy - 17)), w=1.5)
        a.screw(R((ox - 4, oy - 19)), 3.4, w=1.2)
        a.text(R((ox - 4, oy - 25)), "thumb screw", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
    elif kind == "sims":
        # double-ended, opposite curved blades (no hinge)
        p = quad((ox, oy - 22), (ox + L * 0.50, oy), (ox, oy + 22), 46)
        a.band([R(q) for q in p], 16, 16, lw=1.5)
        a.line([R(q) for q in offset_path(p, 0)], w=0.7, fill=LGREY)
        a.text(R((ox + L * 0.30, oy)), "duck-bill\n(both ends)", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "nasal":
        # Thudichum / Killian: two long thin blades + scissor-like handle
        for sgn in (-1, 1):
            blade = [(ox + L * 0.42, oy + sgn * 3.0), (ox + L, oy + sgn * 6.5)]
            a.band([R(p) for p in blade], 7.0, 8.0, lw=1.5)
            sh = quad((ox + 6, oy + sgn * 13), (ox + L * 0.26, oy + sgn * 9),
                      (ox + L * 0.42, oy + sgn * 3.0), 22)
            a.band([R(p) for p in sh], 4.2, 5.0, lw=1.5)
            a.ring(R((ox, oy + sgn * 16)), 6.5, 3.8, w=1.4)
        a.rect([ox + L * 0.38, oy - 3.6, ox + L * 0.46, oy + 3.6], w=1.4, r=1)
        a.screw(R((ox + L * 0.42, oy)), 1.6, w=1.0)
    elif kind == "ear":
        # aural speculum: simple truncated cone (funnel)
        a.poly([R((ox, oy - 13)), R((ox + L * 0.72, oy - 6)),
                R((ox + L, oy - 4.5)), R((ox + L, oy + 4.5)),
                R((ox + L * 0.72, oy + 6)), R((ox, oy + 13))], w=1.6)
        a.ellipse([ox - 3.5, oy - 13, ox + 3.5, oy + 13], w=1.4)
        a.ellipse([ox + L - 2.0, oy - 4.5, ox + L + 2.0, oy + 4.5], w=1.2,
                  outline=DGREY)
        a.text(R((ox + L * 0.45, oy)), "funnel", size=6.5, weight="it",
               anchor="mm", fill=MGREY)
    elif kind == "eyelid":
        # wire lid speculum (Barraquer): springy U with two lid hooks
        c = quad((ox, oy - 20), (ox - 26, oy), (ox, oy + 20), 40)
        a.line([R(p) for p in c], w=2.0)
        for sgn in (-1, 1):
            y = oy + sgn * 20
            a.line([R((ox, y)), R((ox + 16, y)),
                    R((ox + 20, y - sgn * 5))], w=2.0)
            a.arc(R((ox + 20, y - sgn * 9)), 4.5,
                  0 if sgn > 0 else 90, 90 if sgn > 0 else 180, w=2.0)
        a.text(R((ox + 24, oy)), "lid hooks", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    return {"tip": R((ox + L, oy))}


# ---------------------------------------------------------------- dilators
def dilator_set(a, origin=(0, 0), n=6, L=120, kind="hegar", ang=0.0,
                spread=17):
    """Graduated dilator set. kind: hegar | bakes | lacrimal | trousseau"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "hegar":
        for i in range(n):
            y = oy + i * spread
            w = 3.2 + i * 1.15
            # double-ended, gently curved rod
            p = quad((ox, y + 4), (ox + L * 0.5, y - 5), (ox + L, y + 4), 34)
            a.band([R(q) for q in p], w, w, lw=1.4)
            a.circle(R(p[0]), w / 2, w=1.2)
            a.circle(R(p[-1]), w / 2, w=1.2)
            a.text(R((ox + L + 7, y + 2)), f"{5 + i * 2}mm", size=7.5,
                   weight="semi", anchor="lm", fill=DGREY)
    elif kind == "bakes":
        for i in range(n):
            y = oy + i * spread
            p = quad((ox, y), (ox + L * 0.62, y - 2), (ox + L, y - 13), 34)
            a.band([R(q) for q in p], 2.6, 2.2, lw=1.3)
            a.circle(R(p[-1]), 2.0 + i * 0.75, w=1.3)     # olive/bulbous tip
            a.rect([ox - 12, y - 2.6, ox + 1, y + 2.6], w=1.3, r=1.4)
            a.text(R((ox + L + 8, y - 13)), f"{3 + i}mm", size=7.5,
                   weight="semi", anchor="lm", fill=DGREY)
    elif kind == "trousseau":
        # tracheal dilator: 3-blade, opens on squeezing rings
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 13)), 7.0, 4.2, w=1.4)
            sh = quad((ox + 7, oy + sgn * 13), (ox + L * 0.42, oy + sgn * 8),
                      (ox + L * 0.62, oy + sgn * 2.4), 22)
            a.band([R(p) for p in sh], 4.4, 4.0, lw=1.4)
            bl = [(ox + L * 0.62, oy + sgn * 2.4), (ox + L, oy + sgn * 12)]
            a.band([R(p) for p in bl], 5.2, 4.0, lw=1.5)
        a.rect([ox + L * 0.58, oy - 3.4, ox + L * 0.66, oy + 3.4], w=1.4, r=1)
        a.text(R((ox + L, oy)), "opens on\nsqueezing", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "lacrimal":
        for i in range(n):
            y = oy + i * spread
            a.band([R((ox, y)), R((ox + L, y))], 3.0, 1.0, lw=1.3)
            a.knurl([ox + L * 0.30, y - 1.6, ox + L * 0.58, y + 1.6], n=6, w=0.6)
    return {}


# ---------------------------------------------------------------- curettes
def curette(a, origin=(0, 0), L=130, kind="uterine", ang=0.0, loop=7.0):
    """kind: uterine_sharp | uterine_blunt | bone | adenoid | ear"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind.startswith("uterine"):
        sharp = kind.endswith("sharp")
        p = quad((ox, oy), (ox + L * 0.72, oy - 3), (ox + L, oy - 12), 34)
        a.band([R(q) for q in p], 3.4, 2.6, lw=1.4)
        # flat malleable handle
        a.poly([R((ox - 26, oy - 5.0)), R((ox + 1, oy - 2.4)),
                R((ox + 1, oy + 2.4)), R((ox - 26, oy + 5.0))], w=1.5)
        a.knurl([ox - 24, oy - 4.2, ox - 6, oy + 4.2], n=8, w=0.6)
        # open cutting loop at the tip
        t = p[-1]
        a.ellipse([t[0] - loop * 0.55, t[1] - loop, t[0] + loop * 0.55,
                   t[1] + loop * 0.25], w=1.5)
        if sharp:
            a.arc(R((t[0], t[1] - loop * 0.38)), loop * 0.52, 200, 340, w=2.1)
            a.text(R((t[0] + loop + 4, t[1] - loop * 0.4)), "sharp loop",
                   size=6.5, weight="it", anchor="lm", fill=MGREY)
        else:
            a.text(R((t[0] + loop + 4, t[1] - loop * 0.4)), "blunt loop",
                   size=6.5, weight="it", anchor="lm", fill=MGREY)
    elif kind == "bone":
        a.band([R((ox, oy)), R((ox + L * 0.80, oy))], 5.6, 4.0, lw=1.4)
        # bulbous grip
        a.ellipse([ox - 24, oy - 7.0, ox + 2, oy + 7.0], w=1.5)
        a.knurl([ox - 20, oy - 5.5, ox - 2, oy + 5.5], n=7, w=0.6)
        x = ox + L * 0.80
        # cup / spoon tip
        a.band([R((x, oy)), R((x + 10, oy - 1.5))], 4.0, 8.0, lw=1.4)
        a.ellipse([x + 8, oy - 6.5, x + 20, oy + 3.5], w=1.6)
        a.arc(R((x + 14, oy - 1.5)), 4.4, 20, 340, w=1.0, fill=DGREY)
        a.text(R((x + 24, oy - 1.5)), "cup (spoon)", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "adenoid":
        # St Clair Thomson: boxed cage curette on an angled shaft
        p = [(ox, oy), (ox + L * 0.62, oy), (ox + L * 0.78, oy + 16)]
        a.band([R(q) for q in p], 5.0, 4.4, lw=1.5)
        a.poly([R((ox - 26, oy - 5.0)), R((ox + 1, oy - 2.6)),
                R((ox + 1, oy + 2.6)), R((ox - 26, oy + 5.0))], w=1.5)
        a.knurl([ox - 24, oy - 4.2, ox - 6, oy + 4.2], n=8, w=0.6)
        x, y = ox + L * 0.78, oy + 16
        a.rect([x - 13, y, x + 13, y + 13], w=1.6, r=1.5)      # cage/box
        a.seg((x - 13, y + 4.2), (x + 13, y + 4.2), w=2.0)      # cutting edge
        a.text((x + 17, y + 7), "boxed cage", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "ear":
        a.band([R((ox, oy)), R((ox + L, oy - 6))], 3.0, 1.8, lw=1.3)
        a.knurl([ox + L * 0.16, oy - 1.6, ox + L * 0.50, oy + 1.6], n=8, w=0.6)
        a.circle(R((ox + L + 1.5, oy - 6.4)), 2.6, w=1.4)
    return {}


# ---------------------------------------------------------------- endoscopes
def endoscope(a, origin=(0, 0), L=180, kind="sigmoidoscope", ang=0.0):
    """
    kind: sigmoidoscope | proctoscope | laparoscope | arthroscope
          | bronchoscope | mediastinoscope | choledochoscope | cystoscope
    """
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind in ("sigmoidoscope", "proctoscope"):
        rad = 11 if kind == "sigmoidoscope" else 13
        ln = L if kind == "sigmoidoscope" else L * 0.42
        # rigid tube (side view) with obturator
        a.rect([ox, oy - rad, ox + ln, oy + rad], w=1.6, r=2)
        a.ellipse([ox + ln - 4, oy - rad, ox + ln + 4, oy + rad], w=1.3,
                  outline=DGREY)
        # bevelled distal end
        a.seg(R((ox + ln, oy - rad)), R((ox + ln + 7, oy - rad * 0.3)), w=1.6)
        # proximal head: eyepiece + light post + insufflation bulb port
        a.rect([ox - 20, oy - rad - 3, ox + 1, oy + rad + 3], w=1.6, r=3)
        a.circle(R((ox - 9, oy)), 6.0, w=1.4)
        a.band([R((ox - 12, oy - rad - 2)), R((ox - 20, oy - rad - 16))],
               6.0, 6.5, lw=1.4)
        a.text(R((ox - 22, oy - rad - 18)), "light carrier", size=6.5,
               weight="it", anchor="mb", fill=MGREY)
        a.band([R((ox - 12, oy + rad + 2)), R((ox - 24, oy + rad + 12))],
               4.4, 4.4, lw=1.4)
        a.circle(R((ox - 31, oy + rad + 17)), 6.5, w=1.4)     # bulb
        a.text(R((ox - 31, oy + rad + 26)), "insufflator", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
        a.dash_path([R((ox + 4, oy)), R((ox + ln - 4, oy))], w=0.7, fill=LGREY)
        a.text(R((ox + ln * 0.5, oy)), "obturator", size=7, weight="it",
               anchor="mm", fill=MGREY)
    elif kind in ("laparoscope", "arthroscope", "choledochoscope",
                  "cystoscope", "mediastinoscope"):
        if kind == "mediastinoscope":
            # tapered open tube, slightly flattened
            a.poly([R((ox, oy - 13)), R((ox + L, oy - 7)),
                    R((ox + L, oy + 7)), R((ox, oy + 13))], w=1.6)
            a.ellipse([ox - 4, oy - 13, ox + 4, oy + 13], w=1.4)
            a.band([R((ox - 2, oy - 12)), R((ox - 16, oy - 24))], 5.0, 5.0,
                   lw=1.4)
            a.text(R((ox - 18, oy - 26)), "fibre-optic light", size=6.5,
                   weight="it", anchor="mb", fill=MGREY)
            a.text(R((ox + L * 0.55, oy)), "open tube", size=7, weight="it",
                   anchor="mm", fill=MGREY)
        else:
            rad = {"laparoscope": 5.4, "arthroscope": 3.4,
                   "choledochoscope": 3.0, "cystoscope": 4.6}[kind]
            a.rect([ox, oy - rad, ox + L, oy + rad], w=1.5, r=rad)
            a.line([R((ox + L * 0.2, oy)), R((ox + L, oy))], w=0.6, fill=LGREY)
            # angled distal lens face (30 deg)
            a.seg(R((ox + L - 6, oy - rad)), R((ox + L, oy + rad)), w=1.4)
            a.text(R((ox + L - 2, oy + rad + 3)), "30° lens", size=6.5,
                   weight="it", anchor="mt", fill=MGREY)
            # eyepiece + light post
            a.rect([ox - 26, oy - 9, ox + 1, oy + 9], w=1.6, r=3)
            a.ellipse([ox - 34, oy - 9, ox - 24, oy + 9], w=1.5)
            a.circle(R((ox - 29, oy)), 4.6, w=1.2, outline=DGREY)
            a.band([R((ox - 14, oy + 8)), R((ox - 26, oy + 24))], 5.6, 6.2,
                   lw=1.4)
            a.text(R((ox - 28, oy + 26)), "light post", size=6.5, weight="it",
                   anchor="mt", fill=MGREY)
            a.text(R((ox - 29, oy - 12)), "eyepiece", size=6.5, weight="it",
                   anchor="mb", fill=MGREY)
    elif kind == "bronchoscope":
        a.rect([ox, oy - 8, ox + L, oy + 8], w=1.6, r=2)
        for i in range(8):    # side ventilation holes
            a.circle(R((ox + L * 0.55 + i * 8, oy - 4)), 1.5, w=0.9)
        a.rect([ox - 22, oy - 12, ox + 1, oy + 12], w=1.6, r=3)
        a.circle(R((ox - 10, oy)), 7.0, w=1.4)
        a.band([R((ox - 12, oy - 11)), R((ox - 24, oy - 26))], 5.6, 6.0, lw=1.4)
        a.text(R((ox - 26, oy - 28)), "light", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
        a.text(R((ox + L * 0.72, oy + 12)), "side vents", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    return {"tip": R((ox + L, oy))}


def trocar(a, origin=(0, 0), L=140, ang=0.0, kind="trocar"):
    """kind: trocar | veress"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "trocar":
        # cannula/sleeve + pyramidal obturator + gas stopcock
        a.rect([ox, oy - 8, ox + L * 0.86, oy + 8], w=1.6, r=2)
        a.poly([R((ox + L * 0.86, oy - 8)), R((ox + L, oy)),
                R((ox + L * 0.86, oy + 8))], w=1.6, fill=LGREY)   # pyramid tip
        a.rect([ox - 26, oy - 14, ox + 1, oy + 14], w=1.6, r=3)   # valve house
        a.circle(R((ox - 12, oy)), 6.5, w=1.3)
        a.text(R((ox - 12, oy)), "V", size=7, weight="bold", anchor="mm",
               fill=DGREY)
        a.band([R((ox - 20, oy - 13)), R((ox - 30, oy - 27))], 5.6, 6.4, lw=1.4)
        a.circle(R((ox - 33, oy - 30)), 4.0, w=1.3)               # stopcock
        a.text(R((ox - 35, oy - 34)), "CO₂ stopcock", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
        a.text(R((ox + L * 0.42, oy)), "cannula (sleeve)", size=7, weight="it",
               anchor="mm", fill=MGREY)
    else:  # Veress -- spring-loaded blunt-tipped insufflation needle
        a.band([R((ox, oy)), R((ox + L, oy))], 4.0, 4.0, lw=1.5)
        a.poly([R((ox + L, oy - 2.0)), R((ox + L + 8, oy)),
                R((ox + L, oy + 2.0))], w=1.4, fill=LGREY)
        a.line([R((ox + L * 0.2, oy)), R((ox + L + 6, oy))], w=0.7, fill=LGREY)
        a.rect([ox - 24, oy - 6.5, ox + 1, oy + 6.5], w=1.6, r=2.5)
        a.knurl([ox - 22, oy - 5.5, ox - 4, oy + 5.5], n=7, w=0.6)
        a.circle(R((ox - 30, oy)), 5.0, w=1.4)      # luer hub
        a.text(R((ox + L + 10, oy)), "blunt inner\nstylet (spring)", size=6.5,
               weight="it", anchor="lm", fill=MGREY)


# --------------------------------------------------- self-retaining retractors
def self_retaining(a, origin=(0, 0), L=140, kind="weitlaner", ang=0.0):
    """kind: weitlaner | balfour | finochietto | mastoid | cerebellar"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind in ("weitlaner", "mastoid", "cerebellar"):
        # two arms crossing at a hinge, ratchet bar, rake/blade tips
        sharp = kind != "cerebellar"
        hinge = (ox + L * 0.52, oy)
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 15)), 7.5, 4.6, w=1.4)
            sh = quad((ox + 7, oy + sgn * 15), (ox + L * 0.34, oy + sgn * 11),
                      hinge, 24)
            a.band([R(p) for p in sh], 4.6, 4.2, lw=1.4)
            arm = quad(hinge, (ox + L * 0.76, oy - sgn * 6),
                       (ox + L, oy - sgn * 17), 22)
            a.band([R(p) for p in arm], 4.2, 4.6, lw=1.4)
            # tip: rake prongs or blunt blade
            t = arm[-1]
            if sharp:
                for k in (-1, 0, 1):
                    b = (t[0], t[1] + k * 3.4)
                    a.poly([R(b), R((t[0] + 11, t[1] + k * 4.0 - sgn * 5)),
                            R((t[0] + 3, t[1] + k * 3.4))], w=1.1, fill=BLACK)
            else:
                a.poly([R((t[0], t[1] - 4)), R((t[0] + 12, t[1] - 6)),
                        R((t[0] + 12, t[1] + 6)), R((t[0], t[1] + 4))], w=1.4)
        a.screw(R(hinge), 3.4, w=1.3)
        # ratchet bar: rises from the lower shank and locks on the upper one
        rb0 = (ox + 13, oy + 12.0)
        rb1 = (ox + 15, oy - 11.0)
        a.band([R(rb0), R(rb1)], 3.0, 2.6, lw=1.4)
        for i in range(5):
            t = (i + 0.5) / 5
            p = lerp(rb0, rb1, t)
            a.seg(R(p), R((p[0] + 3.2, p[1] + 0.6)), w=1.0)
        a.text(R((ox + 21, oy - 13)), "ratchet lock", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "balfour":
        # abdominal self-retainer: cross-bar + 2 side blades + centre bladder blade
        a.rect([ox, oy - 4, ox + L, oy + 4], w=1.6, r=1.5)
        a.ratchet((ox + L * 0.10, oy - 4), (ox + L * 0.90, oy - 4), n=14,
                  depth=-2.4, w=0.9)
        for x, lab in ((ox + L * 0.14, None), (ox + L * 0.86, None)):
            a.rect([x - 7, oy - 11, x + 7, oy + 5], w=1.5, r=2)   # slide block
            a.screw((x, oy - 3), 3.0, w=1.1)
            # fenestrated lateral blade going down
            a.poly([(x - 8, oy + 5), (x + 8, oy + 5), (x + 10, oy + 34),
                    (x - 10, oy + 34)], w=1.5)
            a.rect([x - 5, oy + 12, x + 5, oy + 29], w=1.0, r=2, outline=DGREY)
        # centre bladder blade on a sliding arm
        a.rect([ox + L * 0.44, oy - 16, ox + L * 0.56, oy - 4], w=1.5, r=2)
        a.band([(ox + L * 0.50, oy - 4), (ox + L * 0.50, oy + 20)], 5.0, 5.0,
               lw=1.5)
        a.poly([(ox + L * 0.50 - 11, oy + 20), (ox + L * 0.50 + 11, oy + 20),
                (ox + L * 0.50 + 9, oy + 40), (ox + L * 0.50 - 9, oy + 40)],
               w=1.5)
        a.text((ox + L * 0.50, oy + 44), "bladder blade", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
        a.text((ox + L * 0.14, oy + 38), "lateral blade", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    elif kind == "finochietto":
        # rib spreader: rack bar, crank handle, two hinged arms with fenestrated blades
        a.rect([ox, oy - 4.0, ox + L, oy + 4.0], w=1.6, r=1.5)
        a.ratchet((ox + L * 0.16, oy + 4.0), (ox + L * 0.94, oy + 4.0), n=16,
                  depth=2.4, w=0.9)
        # fixed arm (left) -- tall arm + deep fenestrated rib blade
        a.band([(ox + 12, oy - 4), (ox + 12, oy - 40)], 7.0, 7.0, lw=1.6)
        a.poly([(ox - 2, oy - 40), (ox + 26, oy - 40), (ox + 26, oy - 74),
                (ox - 2, oy - 74)], w=1.7)
        a.rect([ox + 4, oy - 69, ox + 20, oy - 45], w=1.1, r=2.5, outline=DGREY)
        # sliding arm (right)
        a.rect([ox + L * 0.62, oy - 10, ox + L * 0.80, oy + 5], w=1.6, r=2)
        a.band([(ox + L * 0.71, oy - 10), (ox + L * 0.71, oy - 40)], 7.0, 7.0,
               lw=1.6)
        a.poly([(ox + L * 0.71 - 14, oy - 40), (ox + L * 0.71 + 14, oy - 40),
                (ox + L * 0.71 + 14, oy - 74), (ox + L * 0.71 - 14, oy - 74)],
               w=1.7)
        a.rect([ox + L * 0.71 - 8, oy - 69, ox + L * 0.71 + 8, oy - 45],
               w=1.1, r=2.5, outline=DGREY)
        a.text((ox + 12, oy - 78), "fenestrated rib blades", size=6.5,
               weight="it", anchor="lb", fill=MGREY)
        # crank handle
        a.circle((ox + L + 4, oy), 5.5, w=1.5)
        a.band([(ox + L + 4, oy), (ox + L + 20, oy + 13)], 4.0, 4.0, lw=1.5)
        a.circle((ox + L + 22, oy + 15), 4.6, w=1.5)
        a.text((ox + L + 12, oy + 24), "crank", size=6.5, weight="it",
               anchor="mt", fill=MGREY)
    return {}


# ------------------------------------------------------------ vascular items
def vascular(a, origin=(0, 0), L=120, kind="bulldog", ang=0.0):
    """kind: bulldog | satinsky | aortic_punch | tunneler"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "bulldog":
        # small spring clip, atraumatic jaws
        for sgn in (-1, 1):
            p = quad((ox, oy + sgn * 2), (ox + L * 0.42, oy + sgn * 10),
                     (ox + L, oy + sgn * 2.4), 30)
            a.band([R(q) for q in p], 3.0, 3.6, lw=1.5)
            if sgn == 1:
                a.cross_serrate(R(p[-9]), R(p[-1]), n=7, depth=1.4, w=0.7,
                                fill=MGREY)
        a.arc(R((ox + 2, oy)), 4.2, 90, 270, w=2.0)
        a.text(R((ox + L * 0.42, oy)), "spring", size=6.5, weight="it",
               anchor="mm", fill=MGREY)
    elif kind == "satinsky":
        # long angled 'S'-curved atraumatic side-biting clamp
        res = ring_handle_instrument(a, origin=(ox, oy), L=L, jaw="atraumatic",
                                     jaw_len=L * 0.42, curve=0.0, ring_r=10,
                                     jaw_w=5.0, ang=ang, open_deg=4)
        # extra: mark the characteristic S curve
        a.text(R((ox + L * 0.86, oy - 16)), "S-shaped\natraumatic jaw",
               size=6.5, weight="it", anchor="mm", fill=MGREY)
        return res
    elif kind == "aortic_punch":
        a.band([R((ox, oy)), R((ox + L * 0.72, oy))], 7.0, 6.0, lw=1.5)
        a.knurl([ox + 4, oy - 3.4, ox + L * 0.40, oy + 3.4], n=10, w=0.6)
        x = ox + L * 0.72
        a.rect([x, oy - 7, x + 16, oy + 7], w=1.5, r=2)
        a.circle(R((x + 24, oy)), 6.0, w=1.6)         # circular cutting head
        a.circle(R((x + 24, oy)), 3.0, w=1.0, outline=DGREY)
        # plunger
        a.band([R((ox - 16, oy)), R((ox - 1, oy))], 5.0, 6.5, lw=1.5)
        a.text(R((x + 24, oy + 10)), "circular punch", size=6.5, weight="it",
               anchor="mt", fill=MGREY)
    return {}


# ------------------------------------------------------------ bone / ortho
def bone_instrument(a, origin=(0, 0), L=150, kind="rongeur", ang=0.0):
    """
    kind: rongeur | kerrison | osteotome | chisel | gouge | mallet | rasp
          | gigli | periosteal | bone_holder | bone_cutter | hudson | reamer
    """
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "rongeur":
        # double-action, spring between handles, cup jaws
        for sgn in (-1, 1):
            h = quad((ox, oy + sgn * 16), (ox + L * 0.34, oy + sgn * 13),
                     (ox + L * 0.60, oy + sgn * 3.2), 26)
            a.band([R(p) for p in h], 6.0, 5.0, lw=1.5)
            a.arc(R((ox - 1, oy + sgn * 16)), 4.0,
                  90 if sgn > 0 else 180, 270 if sgn > 0 else 360, w=1.5)
            jw = [(ox + L * 0.60, oy + sgn * 3.2), (ox + L, oy + sgn * 2.0)]
            a.band([R(p) for p in jw], 5.0, 6.2, lw=1.5)
        # leaf spring
        sp = quad((ox + L * 0.16, oy - 12), (ox + L * 0.34, oy),
                  (ox + L * 0.16, oy + 12), 24)
        a.line([R(p) for p in sp], w=1.6)
        a.rect([ox + L * 0.56, oy - 4.2, ox + L * 0.64, oy + 4.2], w=1.4, r=1)
        a.screw(R((ox + L * 0.60, oy)), 1.6, w=1.0)
        # cup jaw tips
        a.arc(R((ox + L + 1, oy - 2.0)), 3.6, 100, 260, w=1.8)
        a.arc(R((ox + L + 1, oy + 2.0)), 3.6, 280, 440, w=1.8)
        a.text(R((ox + L * 0.30, oy)), "spring", size=6.5, weight="it",
               anchor="mm", fill=MGREY)
        a.text(R((ox + L + 7, oy)), "cup jaws", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "kerrison":
        # up-biting laminectomy rongeur: pistol grip, footplate
        a.band([R((ox, oy)), R((ox + L * 0.88, oy - 2))], 6.4, 5.0, lw=1.5)
        for sgn in (-1, 1):
            h = quad((ox + 2, oy + sgn * 3.0), (ox - 14, oy + sgn * 16),
                     (ox - 8, oy + sgn * 30), 22)
            a.band([R(p) for p in h], 5.4, 6.4, lw=1.5)
        x = ox + L * 0.88
        # foot plate + up-biting cutting head
        a.poly([R((x, oy - 4.6)), R((x + 15, oy - 8.5)), R((x + 15, oy - 2.0)),
                R((x, oy + 2.0))], w=1.5)
        a.seg(R((x + 1, oy - 2.6)), R((x + 15, oy - 6.0)), w=2.0)
        a.text(R((x + 19, oy - 6)), "up-biting\nfootplate", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind in ("osteotome", "chisel", "gouge"):
        a.poly([R((ox, oy - 6.5)), R((ox + L * 0.46, oy - 5.0)),
                R((ox + L, oy - 4.2)), R((ox + L, oy + 4.2)),
                R((ox + L * 0.46, oy + 5.0)), R((ox, oy + 6.5))], w=1.6)
        a.knurl([ox + 4, oy - 5.6, ox + L * 0.36, oy + 5.6], n=11, w=0.7)
        if kind == "osteotome":     # bevel on BOTH faces
            a.seg(R((ox + L, oy - 4.2)), R((ox + L + 10, oy)), w=1.6)
            a.seg(R((ox + L, oy + 4.2)), R((ox + L + 10, oy)), w=1.6)
            note = "bevel both sides"
        elif kind == "chisel":      # bevel on ONE face
            a.seg(R((ox + L, oy - 4.2)), R((ox + L + 10, oy + 4.2)), w=1.6)
            a.seg(R((ox + L, oy + 4.2)), R((ox + L + 10, oy + 4.2)), w=1.6)
            note = "bevel one side"
        else:                        # gouge -- U-shaped trough
            a.arc(R((ox + L + 5, oy)), 4.4, 270, 450, w=1.6)
            a.seg(R((ox + L, oy - 4.2)), R((ox + L + 9, oy - 4.2)), w=1.6)
            note = "U-shaped trough"
        a.text(R((ox + L + 14, oy)), note, size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "mallet":
        a.band([R((ox, oy + 44)), R((ox, oy + 12))], 8.0, 9.0, lw=1.6)
        a.knurl([ox - 4.2, oy + 20, ox + 4.2, oy + 42], n=8, w=0.6)
        a.rect([ox - 22, oy - 4, ox + 22, oy + 12], w=1.7, r=2.5)
        a.rect([ox - 22, oy - 4, ox - 12, oy + 12], w=1.2, r=2.0, outline=DGREY)
        a.rect([ox + 12, oy - 4, ox + 22, oy + 12], w=1.2, r=2.0, outline=DGREY)
        a.text((ox + 27, oy + 4), "nylon/lead\nfaces", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "rasp":
        a.band([R((ox, oy)), R((ox + L, oy))], 5.0, 9.0, lw=1.5)
        a.knurl([ox + 3, oy - 2.6, ox + L * 0.32, oy + 2.6], n=9, w=0.6)
        # cross-hatched abrasive face
        a.hatch([ox + L * 0.40, oy - 4.2, ox + L - 2, oy + 4.2], step=3.0,
                w=0.6, fill=DGREY, ang=45)
        a.hatch([ox + L * 0.40, oy - 4.2, ox + L - 2, oy + 4.2], step=3.0,
                w=0.6, fill=DGREY, ang=135)
        a.text(R((ox + L * 0.70, oy + 8)), "abrasive file surface", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    elif kind == "gigli":
        # flexible twisted saw wire with two removable T-handles
        w = quad((ox + 22, oy), (ox + L * 0.5, oy - 12), (ox + L - 22, oy), 60)
        a.line([R(p) for p in w], w=1.6)
        for i in range(0, len(w) - 2, 3):     # serration ticks
            a.seg(R(w[i]), R((w[i][0] + 1.4, w[i][1] + 3.0)), w=0.8, fill=DGREY)
        for x in (ox + 22, ox + L - 22):
            d = -1 if x < ox + L / 2 else 1
            a.circle(R((x, oy)), 4.0, w=1.5)                # eyelet
            a.rect([x + d * 6 - 3, oy - 13, x + d * 6 + 3, oy + 13], w=1.6, r=2)
            a.knurl([x + d * 6 - 2.4, oy - 11, x + d * 6 + 2.4, oy + 11],
                    n=6, w=0.6)
        a.text(R((ox + L * 0.5, oy + 12)), "flexible twisted saw wire",
               size=6.5, weight="it", anchor="mt", fill=MGREY)
    elif kind == "periosteal":
        a.band([R((ox, oy)), R((ox + L, oy))], 5.6, 7.0, lw=1.5)
        a.knurl([ox + 4, oy - 3.0, ox + L * 0.42, oy + 3.0], n=11, w=0.6)
        # broad, slightly curved, blunt lifting edge
        t = ox + L
        a.poly([R((t, oy - 3.5)), R((t + 12, oy - 6.0)), R((t + 14, oy)),
                R((t + 12, oy + 6.0)), R((t, oy + 3.5))], w=1.5, fill=LGREY)
        a.text(R((t + 18, oy)), "blunt elevating\nedge", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "bone_holder":
        # heavy ratcheted bone-holding clamp with jaw teeth
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 15)), 7.5, 4.6, w=1.5)
            sh = quad((ox + 7, oy + sgn * 15), (ox + L * 0.36, oy + sgn * 12),
                      (ox + L * 0.56, oy + sgn * 3.4), 24)
            a.band([R(p) for p in sh], 5.6, 5.0, lw=1.5)
            jw = quad((ox + L * 0.56, oy + sgn * 3.4),
                      (ox + L * 0.84, oy + sgn * 12),
                      (ox + L, oy + sgn * 6.0), 24)
            a.band([R(p) for p in jw], 5.0, 5.6, lw=1.5)
            a.teeth(R(jw[-6]), R(jw[-1]), n=3, depth=-sgn * 4.0, w=1.1)
        a.rect([ox + L * 0.52, oy - 4.4, ox + L * 0.60, oy + 4.4], w=1.4, r=1)
        a.ratchet(R((ox + 9, oy - 12)), R((ox + 26, oy - 16)), n=5, depth=-2.4,
                  w=1.0)
        a.text(R((ox + L, oy)), "gripping\nteeth", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "bone_cutter":
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 16)), 7.5, 4.6, w=1.5)
            sh = quad((ox + 7, oy + sgn * 16), (ox + L * 0.34, oy + sgn * 13),
                      (ox + L * 0.58, oy + sgn * 3.4), 24)
            a.band([R(p) for p in sh], 6.0, 5.2, lw=1.5)
            jw = [(ox + L * 0.58, oy + sgn * 3.4), (ox + L, oy + sgn * 1.6)]
            a.band([R(p) for p in jw], 5.2, 4.0, lw=1.5)
        a.rect([ox + L * 0.54, oy - 4.4, ox + L * 0.62, oy + 4.4], w=1.4, r=1)
        a.seg(R((ox + L - 1, oy - 2.4)), R((ox + L + 3, oy)), w=1.8)
        a.seg(R((ox + L - 1, oy + 2.4)), R((ox + L + 3, oy)), w=1.8)
        a.text(R((ox + L + 7, oy)), "bevelled\ncutting edges", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "hudson":
        # hand brace: crank frame + chuck + perforator bit
        a.line([R((ox, oy)), R((ox + 26, oy))], w=2.0)
        a.line([R((ox + 26, oy)), R((ox + 26, oy - 26)),
                R((ox + 56, oy - 26)), R((ox + 56, oy)),
                R((ox + 82, oy))], w=2.0)
        a.rect([ox + 34, oy - 33, ox + 48, oy - 19], w=1.5, r=2)   # grip
        a.knurl([ox + 36, oy - 31, ox + 46, oy - 21], n=5, w=0.6)
        a.rect([ox + 82, oy - 7, ox + 98, oy + 7], w=1.6, r=2)     # chuck
        a.knurl([ox + 84, oy - 6, ox + 96, oy + 6], n=6, w=0.6)
        a.band([R((ox + 98, oy)), R((ox + L, oy))], 5.0, 2.0, lw=1.5)
        a.poly([R((ox + L, oy - 2)), R((ox + L + 9, oy)),
                R((ox + L, oy + 2))], w=1.3, fill=LGREY)
        a.text(R((ox + L + 13, oy)), "perforator /\nburr", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
        a.text(R((ox + 41, oy - 37)), "crank", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
    return {}


# ------------------------------------------------------------- misc / ENT / eye
def misc_instrument(a, origin=(0, 0), L=130, kind="towel_clip", ang=0.0):
    """
    kind: towel_clip | sponge_stick | tenaculum | snare | trach_tube
          | myringotomy | chalazion | strabismus_hook | lacrimal_probe
          | trephine | phaco | stapler | pacemaker | probe | grooved_director
          | tongue_depressor | mouth_gag | bard_parker | ligature_carrier
    """
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "towel_clip":
        # Backhaus: ring handles, ratchet, crossed sharp curved points
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 13)), 7.5, 4.6, w=1.5)
            sh = quad((ox + 7, oy + sgn * 13), (ox + L * 0.36, oy + sgn * 10),
                      (ox + L * 0.56, oy + sgn * 2.4), 24)
            a.band([R(p) for p in sh], 4.6, 4.2, lw=1.5)
            # jaws curve ACROSS each other and end in sharp points
            jw = quad((ox + L * 0.56, oy + sgn * 2.4),
                      (ox + L * 0.84, oy + sgn * 13),
                      (ox + L, oy - sgn * 3.0), 26)
            a.band([R(p) for p in jw], 4.2, 1.2, lw=1.4)
        a.rect([ox + L * 0.52, oy - 3.6, ox + L * 0.60, oy + 3.6], w=1.4, r=1)
        a.ratchet(R((ox + 9, oy - 10)), R((ox + 25, oy - 14)), n=4, depth=-2.2,
                  w=1.0)
        a.text(R((ox + L + 5, oy)), "sharp crossed\npoints", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "sponge_stick":
        res = ring_handle_instrument(a, origin=(ox, oy), L=L, jaw="serrated",
                                     jaw_len=L * 0.30, curve=0.0, ring_r=10,
                                     jaw_w=7.0, ang=ang, open_deg=3)
        # fenestrated (ring) jaws
        t = res["tip"]
        a.ellipse([t[0] - L * 0.26, oy - 5.0, t[0] - 3, oy - 0.6], w=1.0,
                  outline=WHITE)
        a.text(R((t[0] + 6, oy)), "fenestrated jaws\n(holds gauze ball)",
               size=6.5, weight="it", anchor="lm", fill=MGREY)
        return res
    elif kind == "tenaculum":
        # Schroeder single-tooth uterine tenaculum
        for sgn in (-1, 1):
            a.ring(R((ox, oy + sgn * 13)), 7.5, 4.6, w=1.5)
            sh = quad((ox + 7, oy + sgn * 13), (ox + L * 0.38, oy + sgn * 10),
                      (ox + L * 0.58, oy + sgn * 2.4), 24)
            a.band([R(p) for p in sh], 4.6, 4.2, lw=1.5)
            jw = quad((ox + L * 0.58, oy + sgn * 2.4),
                      (ox + L * 0.82, oy + sgn * 7), (ox + L, oy + sgn * 2), 22)
            a.band([R(p) for p in jw], 4.2, 1.6, lw=1.4)
            # single sharp hook per jaw, curving in
            a.line([R(jw[-1]), R((jw[-1][0] + 8, jw[-1][1] - sgn * 1.0)),
                    R((jw[-1][0] + 11, jw[-1][1] + sgn * 5.0))], w=1.6)
        a.rect([ox + L * 0.54, oy - 3.6, ox + L * 0.62, oy + 3.6], w=1.4, r=1)
        a.ratchet(R((ox + 9, oy - 10)), R((ox + 25, oy - 14)), n=4, depth=-2.2,
                  w=1.0)
        a.text(R((ox + L + 14, oy)), "single sharp\nhooks", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "snare":
        # Eves tonsil snare: cannula + wire loop + sliding thumb ring
        a.band([R((ox, oy)), R((ox + L * 0.74, oy))], 6.0, 5.0, lw=1.5)
        a.rect([ox - 20, oy - 6.5, ox + 1, oy + 6.5], w=1.5, r=2.5)
        a.ring(R((ox - 30, oy)), 8.0, 5.0, w=1.5)         # thumb ring
        a.knurl([ox - 18, oy - 5.4, ox - 4, oy + 5.4], n=6, w=0.6)
        x = ox + L * 0.74
        lp = arc_pts(x + 16, oy, 15, 120, 400, 50)
        a.line([R(p) for p in lp], w=1.5)
        a.text(R((x + 34, oy)), "wire loop\n(snares tonsil)", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "trach_tube":
        # curved outer cannula + inner tube + flange with tape eyelets
        p = quad((ox, oy), (ox + L * 0.46, oy + 4), (ox + L * 0.52, oy + 34), 34)
        a.band([R(q) for q in p], 12, 10, lw=1.6)
        a.line([R(q) for q in offset_path(p, 0)], w=0.7, fill=LGREY)
        # neck flange
        a.rect([ox - 6, oy - 16, ox + 6, oy + 16], w=1.6, r=2.5)
        a.circle(R((ox, oy - 11)), 2.6, w=1.2)
        a.circle(R((ox, oy + 11)), 2.6, w=1.2)
        a.ellipse([ox - 8, oy - 6.5, ox + 4, oy + 6.5], w=1.4)
        a.text(R((ox - 10, oy - 20)), "flange +\ntape eyelets", size=6.5,
               weight="it", anchor="mb", fill=MGREY)
        a.text(R((ox + L * 0.60, oy + 38)), "distal opening", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    elif kind == "myringotomy":
        # fine angled lance-shaped knife
        a.band([R((ox, oy)), R((ox + L * 0.80, oy))], 6.0, 3.4, lw=1.5)
        a.knurl([ox + 4, oy - 3.0, ox + L * 0.44, oy + 3.0], n=11, w=0.6)
        x = ox + L * 0.80
        a.band([R((x, oy)), R((x + 14, oy - 9))], 3.0, 2.0, lw=1.4)
        a.poly([R((x + 13, oy - 8.4)), R((x + 26, oy - 15.5)),
                R((x + 16, oy - 5.6))], w=1.3, fill=LGREY)
        a.text(R((x + 29, oy - 15)), "lance tip", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "chalazion":
        # ring-shaped plate + solid plate, thumb screw
        a.band([R((ox, oy - 11)), R((ox + L * 0.66, oy - 4))], 3.6, 3.6, lw=1.5)
        a.band([R((ox, oy + 11)), R((ox + L * 0.66, oy + 4))], 3.6, 3.6, lw=1.5)
        a.circle(R((ox - 8, oy - 13)), 8.5, w=1.6)
        a.circle(R((ox - 8, oy - 13)), 5.0, w=1.2, outline=DGREY)  # open ring
        a.circle(R((ox - 8, oy + 13)), 8.5, w=1.6, fill=LGREY)     # solid plate
        x = ox + L * 0.66
        a.rect([x, oy - 5, x + 10, oy + 5], w=1.5, r=1.5)
        a.seg(R((x + 5, oy - 5)), R((x + 5, oy - 17)), w=1.5)
        a.screw(R((x + 5, oy - 20)), 3.6, w=1.2)
        a.text(R((ox - 8, oy - 24)), "open ring", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
        a.text(R((ox - 8, oy + 24)), "solid plate", size=6.5, weight="it",
               anchor="mt", fill=MGREY)
    elif kind == "strabismus_hook":
        a.band([R((ox, oy)), R((ox + L * 0.76, oy))], 4.6, 3.0, lw=1.5)
        a.knurl([ox + 3, oy - 2.4, ox + L * 0.42, oy + 2.4], n=10, w=0.6)
        x = ox + L * 0.76
        h = arc_pts(x + 8, oy + 7, 8.5, 250, 430, 34)
        a.line([R(p) for p in h], w=1.7)
        a.circle(R(h[-1]), 1.6, w=1.3, fill=LGREY)      # bulbous safety tip
        a.text(R((x + 20, oy + 12)), "blunt hook\n(lifts muscle)", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "lacrimal_probe":
        a.band([R((ox, oy)), R((ox + L, oy))], 2.4, 2.4, lw=1.4)
        a.knurl([ox + L * 0.34, oy - 2.0, ox + L * 0.66, oy + 2.0], n=9, w=0.6)
        a.circle(R((ox, oy)), 1.7, w=1.2)
        a.circle(R((ox + L, oy)), 1.7, w=1.2)
        a.text(R((ox + L * 0.5, oy + 5)), "double-ended, graduated sizes",
               size=6.5, weight="it", anchor="mt", fill=MGREY)
    elif kind == "trephine":
        a.band([R((ox, oy + 30)), R((ox, oy + 10))], 9.0, 8.0, lw=1.6)
        a.knurl([ox - 4.6, oy + 14, ox + 4.6, oy + 29], n=7, w=0.6)
        a.rect([ox - 13, oy - 2, ox + 13, oy + 11], w=1.6, r=2)
        a.knurl([ox - 11, oy, ox + 11, oy + 9], n=9, w=0.6)
        a.circle(R((ox, oy - 9)), 10.5, w=1.7)
        a.circle(R((ox, oy - 9)), 7.5, w=1.1, outline=DGREY)
        a.text((ox + 15, oy - 9), "circular\ncutting crown", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "phaco":
        a.rect([ox, oy - 9, ox + L * 0.66, oy + 9], w=1.6, r=6)
        a.knurl([ox + 6, oy - 7.6, ox + L * 0.52, oy + 7.6], n=13, w=0.6)
        a.band([R((ox + L * 0.66, oy)), R((ox + L, oy - 5))], 5.0, 2.2, lw=1.5)
        a.circle(R((ox + L + 1, oy - 5.4)), 1.8, w=1.3)
        # irrigation / aspiration lines
        for sgn in (-1, 1):
            a.band([R((ox, oy + sgn * 4)), R((ox - 20, oy + sgn * 13))],
                   3.4, 3.4, lw=1.3)
        a.text(R((ox - 24, oy - 14)), "irrigation /\naspiration", size=6.5,
               weight="it", anchor="rm", fill=MGREY)
        a.text(R((ox + L * 0.33, oy)), "ultrasonic", size=6.5, weight="it",
               anchor="mm", fill=DGREY)
        a.text(R((ox + L + 5, oy - 6)), "titanium tip", size=6.5, weight="it",
               anchor="lm", fill=MGREY)
    elif kind == "stapler":
        # linear cutter / GIA-type stapler
        a.rect([ox, oy - 8, ox + L * 0.52, oy + 8], w=1.6, r=3)
        a.knurl([ox + 5, oy - 6.4, ox + L * 0.34, oy + 6.4], n=10, w=0.6)
        a.band([R((ox, oy + 8)), R((ox - 6, oy + 30))], 7.0, 7.0, lw=1.6)
        a.band([R((ox + L * 0.30, oy + 8)), R((ox + L * 0.34, oy + 28))],
               6.0, 6.0, lw=1.6)      # trigger
        for sgn in (-1, 1):
            a.rect([ox + L * 0.52, oy + sgn * 3 - 3.2, ox + L,
                    oy + sgn * 3 + 3.2], w=1.5, r=1.5)
        for i in range(11):           # staple rows
            xx = ox + L * 0.58 + i * (L * 0.036)
            a.seg(R((xx, oy - 5.0)), R((xx, oy - 1.6)), w=0.9, fill=DGREY)
            a.seg(R((xx, oy + 1.6)), R((xx, oy + 5.0)), w=0.9, fill=DGREY)
        a.text(R((ox + L * 0.78, oy - 9)), "double staple rows", size=6.5,
               weight="it", anchor="mb", fill=MGREY)
        a.text(R((ox + L * 0.78, oy + 9)), "knife track", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    elif kind == "pacemaker":
        a.rect([ox, oy - 20, ox + 44, oy + 20], w=1.7, r=9)
        a.rect([ox + 5, oy - 15, ox + 39, oy + 15], w=0.9, r=6, outline=LGREY)
        a.text((ox + 22, oy), "PULSE\nGEN", size=7, weight="bold",
               anchor="mm", fill=DGREY)
        a.rect([ox + 44, oy - 12, ox + 56, oy + 12], w=1.5, r=3)  # header
        for sgn in (-1, 1):
            lead = quad((ox + 56, oy + sgn * 6), (ox + 100, oy + sgn * 22),
                        (ox + L, oy + sgn * 8), 40)
            a.line([R(p) for p in lead], w=1.8)
            a.circle(R(lead[-1]), 2.6, w=1.3, fill=LGREY)
        a.text((ox + 22, oy - 24), "generator", size=6.5, weight="it",
               anchor="mb", fill=MGREY)
        a.text(R((ox + L + 5, oy)), "endocardial\nleads", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "probe":
        a.band([R((ox, oy)), R((ox + L, oy))], 2.8, 2.8, lw=1.4)
        a.circle(R((ox, oy)), 2.4, w=1.2)
        a.circle(R((ox + L, oy)), 2.4, w=1.2)
        a.text(R((ox + L * 0.5, oy + 5)), "malleable, blunt both ends",
               size=6.5, weight="it", anchor="mt", fill=MGREY)
    elif kind == "grooved_director":
        a.band([R((ox, oy)), R((ox + L, oy))], 4.4, 4.4, lw=1.4)
        a.line([R((ox + 6, oy)), R((ox + L - 4, oy))], w=0.9, fill=DGREY)
        a.circle(R((ox + L, oy)), 3.2, w=1.3)
        a.text(R((ox + L * 0.5, oy + 6)), "central groove guides the knife",
               size=6.5, weight="it", anchor="mt", fill=MGREY)
    elif kind == "tongue_depressor":
        a.poly([R((ox, oy - 7)), R((ox + L * 0.62, oy - 10)),
                R((ox + L, oy - 8)), R((ox + L, oy + 8)),
                R((ox + L * 0.62, oy + 10)), R((ox, oy + 7))], w=1.6)
        for i in range(5):
            a.seg(R((ox + L * 0.70 + i * 7, oy - 7)),
                  R((ox + L * 0.70 + i * 7, oy + 7)), w=0.8, fill=MGREY)
    elif kind == "mouth_gag":
        # Boyle-Davis style: tongue plate + frame
        a.poly([R((ox, oy - 9)), R((ox + L * 0.70, oy - 12)),
                R((ox + L, oy - 7)), R((ox + L, oy + 7)),
                R((ox + L * 0.70, oy + 12)), R((ox, oy + 9))], w=1.6)
        a.line([R((ox + L * 0.16, oy)), R((ox + L - 6, oy))], w=0.9, fill=DGREY)
        a.band([R((ox, oy - 8)), R((ox - 24, oy - 26))], 5.6, 5.6, lw=1.6)
        a.band([R((ox, oy + 8)), R((ox - 24, oy + 26))], 5.6, 5.6, lw=1.6)
        a.text(R((ox + L * 0.55, oy + 15)), "grooved tongue plate", size=6.5,
               weight="it", anchor="mt", fill=MGREY)
    elif kind == "ligature_carrier":
        p = quad((ox, oy), (ox + L * 0.72, oy - 4), (ox + L, oy - 20), 34)
        a.band([R(q) for q in p], 4.6, 3.0, lw=1.5)
        a.knurl([ox + 4, oy - 2.4, ox + L * 0.34, oy + 2.4], n=9, w=0.6)
        a.circle(R(p[-1]), 2.6, w=1.4)
        a.seg(R((p[-1][0] - 1.2, p[-1][1] + 1.0)),
              R((p[-1][0] + 1.2, p[-1][1] - 1.0)), w=1.0, fill=WHITE)
        a.text(R((p[-1][0] + 6, p[-1][1])), "eye carries\nthe ligature",
               size=6.5, weight="it", anchor="lm", fill=MGREY)
    return {}



def thoracic_instrument(a, origin=(0, 0), L=150, kind="rib_shears", ang=0.0):
    """kind: rib_shears | rib_raspatory | rib_approximator | sternal_saw"""
    ox, oy = origin

    def R(p):
        return rot(p, ang, (ox, oy))

    if kind == "rib_shears":
        # heavy guillotine-type shears with offset handles
        for sgn in (-1, 1):
            h = quad((ox, oy + sgn * 18), (ox + L * 0.30, oy + sgn * 15),
                     (ox + L * 0.56, oy + sgn * 3.6), 26)
            a.band([R(p) for p in h], 7.0, 5.6, lw=1.6)
            a.arc(R((ox - 1, oy + sgn * 18)), 5.0,
                  90 if sgn > 0 else 180, 270 if sgn > 0 else 360, w=1.6)
        a.rect([ox + L * 0.52, oy - 5.0, ox + L * 0.62, oy + 5.0], w=1.5, r=1)
        a.screw(R((ox + L * 0.57, oy)), 2.0, w=1.1)
        # short stout angled blades
        a.poly([R((ox + L * 0.62, oy - 4.4)), R((ox + L, oy - 12)),
                R((ox + L + 5, oy - 7)), R((ox + L * 0.66, oy + 1.0))],
               w=1.6, fill=LGREY)
        a.poly([R((ox + L * 0.62, oy + 4.4)), R((ox + L, oy + 12)),
                R((ox + L + 5, oy + 7)), R((ox + L * 0.66, oy - 1.0))],
               w=1.6)
        a.text(R((ox + L + 9, oy)), "stout angled\ncutting jaws", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    elif kind == "rib_raspatory":
        # Doyen periosteal elevator -- curved hook that rides the rib
        a.band([R((ox, oy)), R((ox + L * 0.62, oy))], 6.4, 5.6, lw=1.5)
        a.knurl([ox + 4, oy - 3.2, ox + L * 0.40, oy + 3.2], n=11, w=0.6)
        x = ox + L * 0.62
        hook = arc_pts(x + 14, oy - 2, 15, 150, 400, 44)
        a.band([R(p) for p in hook], 6.0, 5.0, lw=1.6)
        a.text(R((x + 32, oy + 12)), "semicircular hook\nstrips periosteum",
               size=6.5, weight="it", anchor="lm", fill=MGREY)
    elif kind == "rib_approximator":
        a.rect([ox, oy - 4.0, ox + L, oy + 4.0], w=1.6, r=1.5)
        a.ratchet((ox + L * 0.14, oy + 4.0), (ox + L * 0.86, oy + 4.0), n=13,
                  depth=2.2, w=0.9)
        for fx in (0.16, 0.72):
            x = ox + L * fx
            a.rect([x - 7, oy - 10, x + 7, oy + 5], w=1.5, r=2)
            a.line([R((x, oy - 10)), R((x, oy - 26)),
                    R((x + 11, oy - 30))], w=1.8)
            a.arc(R((x + 13, oy - 25)), 5.5, 200, 360, w=1.8)
        a.text((ox + L * 0.44, oy - 34), "hooks engage adjacent ribs",
               size=6.5, weight="it", anchor="mb", fill=MGREY)
    elif kind == "sternal_saw":
        a.rect([ox, oy - 12, ox + L * 0.52, oy + 12], w=1.6, r=5)
        a.knurl([ox + 6, oy - 10, ox + L * 0.38, oy + 10], n=12, w=0.6)
        a.text(R((ox + L * 0.26, oy)), "power unit", size=6.8, weight="semi",
               anchor="mm", fill=DGREY)
        a.band([R((ox + L * 0.52, oy)), R((ox + L * 0.80, oy))], 8.0, 6.0,
               lw=1.5)
        # oscillating blade with a foot/guard
        a.poly([R((ox + L * 0.80, oy - 4)), R((ox + L, oy - 6)),
                R((ox + L, oy + 6)), R((ox + L * 0.80, oy + 4))], w=1.5,
               fill=LGREY)
        for i in range(9):
            a.seg(R((ox + L * 0.83 + i * (L * 0.019), oy + 6)),
                  R((ox + L * 0.83 + i * (L * 0.019), oy + 9)), w=0.9)
        a.line([R((ox + L * 0.80, oy + 7)), R((ox + L + 3, oy + 9))], w=1.5)
        a.text(R((ox + L + 6, oy)), "guarded\noscillating blade", size=6.5,
               weight="it", anchor="lm", fill=MGREY)
    return {}
