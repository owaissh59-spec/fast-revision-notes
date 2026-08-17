#!/usr/bin/env python3
"""
diagrams.py -- conceptual figures for the foundation chapters:
labelled instrument anatomy, classification charts, back-table and
Mayo-stand layouts, the sterilisation workflow and the count sequence.
"""
import math

from artlib import (Art, BLACK, WHITE, GREY, LGREY, MGREY, DGREY,
                    ring_handle_instrument, thumb_forceps, quad, arc_pts,
                    lerp, along, offset_path, ribbon)


# ------------------------------------------------------- labelled anatomy
def hemostat_anatomy(width=470):
    """Ring-handled instrument with every named part called out."""
    a = Art(width, 250)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 6), "Parts of a ring-handled instrument",
           size=11.5, weight="bold", anchor="mt")
    a.seg((width * 0.10, 24), (width * 0.90, 24), w=0.9, fill=MGREY)

    L = 300
    ox, oy = 70, 140
    res = ring_handle_instrument(a, (ox, oy), L=L, jaw="cross",
                                 jaw_len=L * 0.24, curve=0.0, ring_r=15,
                                 jaw_w=6.0, open_deg=0)
    box_x = ox + L - L * 0.24 - 4.2

    # --- callouts
    a.label((ox + 15, oy - 19), "Ring / bow", side="u", lead=26, size=9,
            elbow=(ox + 15, oy - 30))
    a.label((ox + 15, oy + 19), "Finger ring", side="d", lead=24, size=9)
    a.label((ox + 34, oy - 14), "Shank", side="u", lead=52, size=9,
            elbow=(ox + 44, oy - 40))
    a.label((ox + 30, oy + 13), "Ratchet (lock)", side="d", lead=44, size=9,
            elbow=(ox + 44, oy + 40))
    a.label((box_x + 1, oy - 6), "Box lock (joint)", side="u", lead=62,
            size=9, elbow=(box_x + 6, oy - 52))
    a.label((box_x + 30, oy + 4), "Jaw / blade", side="d", lead=52, size=9,
            elbow=(box_x + 36, oy + 42))
    a.label((ox + L - 4, oy - 3), "Tip", side="r", lead=28, size=9)

    # serration zoom
    a.text((width / 2, 232), "Jaw serrations run transversely in a haemostat",
           size=8.2, weight="it", anchor="ms", fill=DGREY)
    return a


def scissors_family(width=470):
    """Mayo vs Metzenbaum vs iris -- proportion comparison."""
    a = Art(width, 250)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 6), "Scissors: matching the instrument to the tissue",
           size=11.0, weight="bold", anchor="mt")
    a.seg((width * 0.10, 24), (width * 0.90, 24), w=0.9, fill=MGREY)

    rows = [
        (0.26, 6.0, "Mayo — short, heavy blades", "fascia, muscle, sutures"),
        (0.20, 4.0, "Metzenbaum — long shank, short fine blades",
         "delicate tissue, dissection"),
        (0.16, 2.8, "Iris / tenotomy — very small", "ophthalmic, fine work"),
    ]
    y = 52
    for frac, jw, name, use in rows:
        ring_handle_instrument(a, (34, y), L=270, jaw="scissor",
                               jaw_len=270 * frac, curve=0.45, ring_r=12,
                               jaw_w=jw)
        a.text((26, y + 26), name, size=9.2, weight="semi", anchor="lt")
        a.text((26, y + 38), "→ " + use, size=8.4, weight="it", anchor="lt",
               fill=DGREY)
        y += 68
    return a


def grip_diagram(width=470):
    """How to hold instruments -- three standard grips."""
    a = Art(width, 190)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 6), "Standard grips", size=11.0, weight="bold",
           anchor="mt")
    a.seg((width * 0.10, 24), (width * 0.90, 24), w=0.9, fill=MGREY)

    cw = width / 3
    labels = [("Pencil grip", "fine, controlled cuts;\nNo.15 / No.11 blade"),
              ("Palmar grip", "long skin incisions;\nNo.20 / No.10 blade"),
              ("Tripod (ring) grip", "thumb + ring finger in bows,\nindex "
               "along shank")]
    for i, (t, sub) in enumerate(labels):
        cx = cw * i + cw / 2
        # stylised hand: palm block + fingers
        a.rect([cx - 26, 62, cx + 26, 96], w=1.4, r=6, fill=LGREY)
        for k in range(4):
            a.rect([cx - 22 + k * 12, 46, cx - 14 + k * 12, 64], w=1.1, r=3)
        if i == 0:
            a.band([(cx - 34, 108), (cx + 30, 84)], 5.0, 2.0, lw=1.5)
            a.poly([(cx + 28, 85), (cx + 44, 78), (cx + 30, 90)], w=1.2,
                   fill=LGREY)
        elif i == 1:
            a.band([(cx - 36, 92), (cx + 34, 92)], 6.0, 2.4, lw=1.5)
            a.poly([(cx + 32, 90), (cx + 50, 92), (cx + 32, 96)], w=1.2,
                   fill=LGREY)
        else:
            a.circle((cx - 20, 104), 8.0, w=1.4)
            a.circle((cx - 20, 122), 8.0, w=1.4)
            a.band([(cx - 12, 106), (cx + 40, 100)], 4.0, 3.0, lw=1.4)
            a.band([(cx - 12, 120), (cx + 40, 108)], 4.0, 3.0, lw=1.4)
        a.text((cx, 140), t, size=9.2, weight="bold", anchor="mt")
        a.text((cx, 154), sub, size=8.0, weight="it", anchor="mt", fill=DGREY)
        if i < 2:
            a.seg((cw * (i + 1), 40), (cw * (i + 1), 176), w=0.8, fill=LGREY)
    return a


# ------------------------------------------------------------ chart figures
def classification_chart(width=470):
    """The six functional groups -- the spine of the whole subject."""
    a = Art(width, 330)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Functional classification of surgical instruments",
           size=11.0, weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    # root
    a.rect([width / 2 - 78, 38, width / 2 + 78, 62], w=1.7, r=3, fill=LGREY)
    a.text((width / 2, 50), "SURGICAL INSTRUMENTS", size=9.0, weight="bold",
           anchor="mm")

    groups = [
        ("1. CUTTING &\nDISSECTING", "scalpel, scissors,\nosteotome, curette"),
        ("2. GRASPING &\nHOLDING", "forceps, Allis,\nBabcock, tenaculum"),
        ("3. CLAMPING &\nOCCLUDING", "haemostats, Kocher,\nbulldog, Satinsky"),
        ("4. EXPOSING &\nRETRACTING", "Army-Navy, Deaver,\nBalfour, Weitlaner"),
        ("5. SUTURING &\nSTAPLING", "needle holders,\nstaplers, clip appliers"),
        ("6. SUCTIONING &\nACCESSORY", "Yankauer, Poole,\nsponge stick, probe"),
    ]
    bw, bh = width / 3 - 16, 46
    for i, (name, eg) in enumerate(groups):
        col, row = i % 3, i // 3
        cx = (width / 3) * col + width / 6
        cy = 96 + row * 108
        a.rect([cx - bw / 2, cy, cx + bw / 2, cy + bh], w=1.5, r=3)
        a.text((cx, cy + bh / 2), name, size=8.2, weight="bold", anchor="mm")
        a.text((cx, cy + bh + 5), eg, size=7.6, weight="it", anchor="mt",
               fill=DGREY)
        # connector from the root
        a.line([(width / 2, 62), (width / 2, 78), (cx, 78), (cx, cy)],
               w=0.9, fill=GREY)
    a.text((width / 2, 314),
           "Every tray must satisfy all six groups before it is complete",
           size=8.4, weight="it", anchor="ms", fill=DGREY)
    return a


def sterilization_flow(width=470):
    """Point-of-use → decontamination → assembly → sterilisation → storage."""
    a = Art(width, 430)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Instrument reprocessing cycle", size=11.0,
           weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    steps = [
        ("POINT OF USE", "wipe blood, keep moist,\nremove gross soil"),
        ("TRANSPORT", "closed, leak-proof,\nbiohazard-labelled"),
        ("DECONTAMINATION", "sort → rinse cool water →\nenzymatic soak → "
         "ultrasonic → rinse → dry"),
        ("INSPECTION & TESTING", "cleanliness, alignment, sharpness,\n"
         "ratchet & box-lock action"),
        ("ASSEMBLY / TRAY SET-UP", "count sheet, jaws OPEN or on a\n"
         "stringer, heaviest at the bottom"),
        ("PACKAGING", "wrap / rigid container +\ninternal & external "
         "indicators"),
        ("STERILISATION", "steam 121 °C/15 min or 134 °C/3 min;\n"
         "EO or plasma for heat-sensitive"),
        ("STORAGE & ISSUE", "cool, dry, dust-free;\nevent-related shelf life"),
    ]
    y = 40
    bw = width - 90
    for i, (t, sub) in enumerate(steps):
        h = 38
        x0 = 45
        a.rect([x0, y, x0 + bw, y + h], w=1.5, r=3,
               fill=LGREY if i % 2 == 0 else None)
        a.text((x0 + 10, y + 9), f"{i+1}.  {t}", size=8.8, weight="bold",
               anchor="lt")
        a.text((x0 + 10, y + 21), sub, size=7.6, weight="it", anchor="lt",
               fill=DGREY)
        if i < len(steps) - 1:
            ax = x0 + bw / 2
            a.seg((ax, y + h), (ax, y + h + 9), w=1.3)
            a.poly([(ax - 4, y + h + 8), (ax + 4, y + h + 8),
                    (ax, y + h + 14)], w=1.0, fill=BLACK)
        y += h + 14
    return a


def backtable_layout(width=470):
    """Top view of a correctly set back table."""
    a = Art(width, 300)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Back table — standard arrangement (top view)",
           size=11.0, weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    x0, y0, x1, y1 = 26, 44, width - 26, 252
    a.rect([x0, y0, x1, y1], w=1.8, r=4)
    a.text((width / 2, y1 + 8), "sterile drape edge — never reach across",
           size=8.0, weight="it", anchor="mt", fill=DGREY)

    W = x1 - x0
    zones = [
        (0.00, 0.30, "SHARPS &\nSUTURE", "blades in a magnet/needle\nbook; "
         "needle holders"),
        (0.30, 0.58, "INSTRUMENTS", "grouped by function,\ntips pointing "
         "one way"),
        (0.58, 0.78, "SPONGES &\nDRESSINGS", "counted, kept away\nfrom "
         "sharps"),
        (0.78, 1.00, "BASINS,\nDRAPES,\nGOWNS", "heaviest and least\nused, "
         "far end"),
    ]
    for f0, f1, name, sub in zones:
        a.seg((x0 + W * f1, y0), (x0 + W * f1, y1), w=1.1, fill=GREY)
        cx = x0 + W * (f0 + f1) / 2
        a.text((cx, y0 + 12), name, size=8.4, weight="bold", anchor="mt")
        a.text((cx, y0 + 48), sub, size=7.4, weight="it", anchor="mt",
               fill=DGREY)

    # instrument silhouettes in the instrument zone
    ix = x0 + W * 0.32
    for k in range(4):
        ring_handle_instrument(a, (ix, y0 + 100 + k * 26), L=W * 0.24,
                               jaw="cross", jaw_len=W * 0.055, curve=0.0,
                               ring_r=6.5, jaw_w=2.6, open_deg=0)
    # sponge stack
    sx = x0 + W * 0.62
    for k in range(4):
        a.rect([sx, y0 + 100 + k * 22, sx + W * 0.13, y0 + 116 + k * 22],
               w=1.1, r=1.5, fill=LGREY)
    # basin
    a.ellipse([x0 + W * 0.80, y0 + 104, x0 + W * 0.96, y0 + 150], w=1.5)
    a.ellipse([x0 + W * 0.83, y0 + 112, x0 + W * 0.93, y0 + 142], w=0.9,
              outline=GREY)
    # drape stack
    a.rect([x0 + W * 0.80, y0 + 164, x0 + W * 0.96, y0 + 196], w=1.4, r=2,
           fill=LGREY)

    a.text((width / 2, 274),
           "Rule: sharps segregated · tips aligned · heaviest items furthest "
           "from the edge", size=8.2, weight="it", anchor="ms", fill=DGREY)
    return a


def mayo_stand_layout(width=470):
    """Top view of the Mayo stand -- only what is needed next."""
    a = Art(width, 250)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Mayo stand — the working surface (top view)",
           size=11.0, weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    x0, y0, x1, y1 = 60, 44, width - 60, 200
    a.rect([x0, y0, x1, y1], w=1.8, r=5)
    W, H = x1 - x0, y1 - y0

    # four quadrants of use
    a.seg((x0, y0 + H * 0.5), (x1, y0 + H * 0.5), w=1.0, fill=GREY)
    a.seg((x0 + W * 0.5, y0), (x0 + W * 0.5, y1), w=1.0, fill=GREY)
    quads = [("Knife &\nscissors", 0.25, 0.25), ("Haemostats\n& clamps", 0.75, 0.25),
             ("Forceps &\nretractors", 0.25, 0.75), ("Needle holders\n& suture", 0.75, 0.75)]
    for name, fx, fy in quads:
        a.text((x0 + W * fx, y0 + H * fy), name, size=8.4, weight="semi",
               anchor="mm")

    a.text((width / 2, y1 + 10),
           "Carries only the instruments needed for the //current// step",
           size=8.2, weight="it", anchor="mt", fill=DGREY)
    a.text((width / 2, 228),
           "Never place the Mayo stand over the patient before draping is "
           "complete", size=8.2, weight="it", anchor="ms", fill=DGREY)
    return a


def count_sequence(width=470):
    """When and what to count."""
    a = Art(width, 290)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Surgical count — when and what", size=11.0,
           weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    when = [("1st", "Before the incision", "baseline count"),
            ("2nd", "Before closing a cavity", "e.g. peritoneum"),
            ("3rd", "Before closing the wound", "fascia / muscle layer"),
            ("4th", "At skin closure", "final reconciliation")]
    y = 40
    for tag, t, sub in when:
        a.circle((48, y + 14), 13, w=1.5, fill=LGREY)
        a.text((48, y + 14), tag, size=8.6, weight="bold", anchor="mm")
        a.text((70, y + 5), t, size=9.2, weight="bold", anchor="lt")
        a.text((70, y + 18), sub, size=7.8, weight="it", anchor="lt",
               fill=DGREY)
        if tag != "4th":
            a.dash((48, y + 28), (48, y + 44), w=1.0, fill=GREY, on=3, off=3)
        y += 46

    a.seg((30, y + 6), (width - 30, y + 6), w=1.0, fill=MGREY)
    a.text((width / 2, y + 14), "COUNTED ITEMS", size=8.6, weight="bold",
           anchor="mt")
    items = ["Sponges & gauze", "Sharps (blades, needles)",
             "Instruments", "Miscellaneous (tapes, clips)"]
    yy = y + 32
    for i, it in enumerate(items):
        cx = 40 + (i % 2) * (width / 2 - 20)
        cy = yy + (i // 2) * 20
        a.rect([cx, cy, cx + 12, cy + 12], w=1.2)
        a.seg((cx + 2.5, cy + 6), (cx + 5, cy + 9), w=1.4)
        a.seg((cx + 5, cy + 9), (cx + 9.5, cy + 3), w=1.4)
        a.text((cx + 18, cy + 6), it, size=8.4, weight="semi", anchor="lm")
    a.text((width / 2, 280),
           "Counted aloud and concurrently by scrub + circulating nurse",
           size=8.2, weight="it", anchor="ms", fill=DGREY)
    return a


def tray_assembly(width=470):
    """How instruments are laid into the tray for sterilisation."""
    a = Art(width, 260)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "Laying up the tray for sterilisation",
           size=11.0, weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    # perforated tray, side view, showing layering
    x0, y0, x1, y1 = 40, 60, width - 40, 190
    a.rect([x0, y0, x1, y1], w=1.8, r=3)
    for i in range(14):     # perforated base
        a.circle((x0 + 18 + i * ((x1 - x0 - 36) / 13), y1), 2.2, w=1.0,
                 fill=WHITE)
    a.text((width / 2, y1 + 6), "perforated / mesh base — lets steam and "
           "condensate through", size=7.8, weight="it", anchor="mt",
           fill=DGREY)

    layers = [(y1 - 26, "Heaviest instruments at the bottom", LGREY),
              (y1 - 52, "Ring-handled instruments on a stringer, jaws OPEN",
               None),
              (y1 - 78, "Delicate & sharp tips protected with tip guards",
               LGREY),
              (y1 - 104, "Concave items on edge / inverted — no water pooling",
               None)]
    for yy, txt, fill in layers:
        a.rect([x0 + 8, yy, x1 - 8, yy + 22], w=1.2, r=2, fill=fill)
        a.text((x0 + 16, yy + 11), txt, size=8.0, weight="semi", anchor="lm")

    a.text((width / 2, 234),
           "A chemical indicator goes INSIDE the pack; an indicator tape "
           "goes OUTSIDE", size=8.2, weight="it", anchor="ms", fill=DGREY)
    a.text((width / 2, 248),
           "Total mass of a wrapped instrument set should not exceed ≈ 11 kg",
           size=8.2, weight="it", anchor="ms", fill=DGREY)
    return a


def tray_size_ladder(width=470):
    """Limited → basic/minor → major: how the trays nest."""
    a = Art(width, 240)
    a.frame(w=1.0, fill=LGREY)
    a.text((width / 2, 8), "The general-surgery tray ladder", size=11.0,
           weight="bold", anchor="mt")
    a.seg((width * 0.08, 27), (width * 0.92, 27), w=0.9, fill=MGREY)

    rows = [("LIMITED PROCEDURES", 0.34, "smallest — very superficial, brief\n"
             "procedures (skin lesion, biopsy)"),
            ("BASIC / MINOR PROCEDURES", 0.62, "small clean cases; the "
             "reference\nset most others are built on"),
            ("MAJOR PROCEDURES", 1.00, "full laparotomy capability; deep\n"
             "cavity exposure and long instruments")]
    y = 44
    for name, frac, sub in rows:
        w = (width - 80) * frac
        a.rect([40, y, 40 + w, y + 34], w=1.6, r=3,
               fill=LGREY if frac < 1.0 else None)
        a.text((48, y + 17), name, size=8.8, weight="bold", anchor="lm")
        a.text((48, y + 40), sub, size=7.6, weight="it", anchor="lt",
               fill=DGREY)
        y += 66
    a.text((width / 2, 226),
           "Each larger tray contains everything in the smaller one, plus "
           "greater depth and length", size=8.2, weight="it", anchor="ms",
           fill=DGREY)
    return a


DIAGRAMS = {
    "fig_hemostat_anatomy": hemostat_anatomy,
    "fig_scissors_family": scissors_family,
    "fig_grip": grip_diagram,
    "fig_classification": classification_chart,
    "fig_steril_flow": sterilization_flow,
    "fig_backtable": backtable_layout,
    "fig_mayo_stand": mayo_stand_layout,
    "fig_count": count_sequence,
    "fig_tray_assembly": tray_assembly,
    "fig_tray_ladder": tray_size_ladder,
}
