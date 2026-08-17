#!/usr/bin/env python3
"""
registry.py -- a named catalogue of every instrument drawing, plus a generic
"plate" renderer that stacks labelled instruments into a single figure.

Each registry entry is:  key -> (draw_fn(art, origin, L), height, default_L)
where draw_fn draws the instrument with its *left-centre* at `origin`.
`height` is the vertical band the drawing needs (used for auto-layout).
"""
import math

from artlib import (Art, BLACK, WHITE, GREY, LGREY, MGREY, DGREY, SS as SS_,
                    ring_handle_instrument, thumb_forceps, scalpel,
                    handheld_retractor, suction_tip, tip_detail, zoom_link,
                    quad, arc_pts, rot)
from artlib2 import (speculum, dilator_set, curette, endoscope, trocar,
                     self_retaining, vascular, bone_instrument,
                     misc_instrument, thoracic_instrument)

R = {}


def reg(key, h=44, L=170):
    def deco(fn):
        R[key] = (fn, h, L)
        return fn
    return deco


# ============================================================ cutting/dissect
@reg("scalpel_10", h=34)
def _(a, o, L): scalpel(a, o, L=L, blade="10", handle_no="4")


@reg("scalpel_11", h=34)
def _(a, o, L): scalpel(a, o, L=L, blade="11", handle_no="3")


@reg("scalpel_15", h=34)
def _(a, o, L): scalpel(a, o, L=L, blade="15", handle_no="3")


@reg("scalpel_20", h=36)
def _(a, o, L): scalpel(a, o, L=L, blade="20", handle_no="4")


@reg("scalpel_12", h=34)
def _(a, o, L): scalpel(a, o, L=L, blade="12", handle_no="3")


@reg("mayo_straight", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.26,
                           curve=0.0, ring_r=11, jaw_w=5.4, open_deg=9)


@reg("mayo_curved", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.26,
                           curve=0.55, ring_r=11, jaw_w=5.4)


@reg("metzenbaum", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.20,
                           curve=0.45, ring_r=11, jaw_w=3.8)


@reg("iris_scissors", h=38)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.16,
                           curve=0.0, ring_r=8.5, jaw_w=2.8, open_deg=7)


@reg("tenotomy_scissors", h=38)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.15,
                           curve=0.35, ring_r=8.5, jaw_w=2.4)


@reg("suture_scissors", h=42)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.22,
                           curve=0.0, ring_r=10.5, jaw_w=4.6, open_deg=8)


@reg("potts_scissors", h=42)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.14,
                           curve=1.05, ring_r=10, jaw_w=3.0)


@reg("wire_scissors", h=42)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="scissor", jaw_len=L * 0.18,
                           curve=0.0, ring_r=10.5, jaw_w=5.6, open_deg=6)


# ================================================================== grasping
@reg("adson", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="adson", w_top=13)


@reg("adson_brown", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="toothed", w_top=13, teeth_n=3)


@reg("tissue_forceps", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="toothed", w_top=15)


@reg("dressing_forceps", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="serrated", w_top=15)


@reg("debakey_forceps", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="debakey", w_top=13)


@reg("fine_forceps", h=30)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="fine", w_top=9)


@reg("russian_forceps", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="serrated", w_top=16)


@reg("bonney_forceps", h=34)
def _(a, o, L): thumb_forceps(a, o, L=L, tip="toothed", w_top=16, teeth_n=3)


# ================================================================== clamping
@reg("mosquito", h=40)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="cross", jaw_len=L * 0.16,
                           curve=0.45, ring_r=9, jaw_w=3.4)


@reg("crile", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="cross", jaw_len=L * 0.22,
                           curve=0.0, ring_r=11, jaw_w=4.6)


@reg("kelly", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="cross", jaw_len=L * 0.22,
                           curve=0.5, ring_r=11, jaw_w=4.8)


@reg("rochester_pean", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="cross", jaw_len=L * 0.26,
                           curve=0.5, ring_r=11.5, jaw_w=5.6)


@reg("kocher", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="teeth", jaw_len=L * 0.24,
                           curve=0.0, ring_r=11.5, jaw_w=5.2, teeth_n=1)


@reg("allis", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="allis", jaw_len=L * 0.24,
                           curve=0.0, ring_r=11, jaw_w=4.6)


@reg("babcock", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="babcock", jaw_len=L * 0.26,
                           curve=0.0, ring_r=11, jaw_w=4.4)


@reg("right_angle", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="serrated", jaw_len=L * 0.20,
                           curve=1.25, ring_r=11, jaw_w=4.4)


@reg("tonsil_clamp", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="serrated", jaw_len=L * 0.22,
                           curve=0.85, ring_r=11, jaw_w=4.2)


@reg("intestinal_clamp", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="atraumatic", jaw_len=L * 0.40,
                           curve=0.0, ring_r=10.5, jaw_w=4.4, open_deg=3)


@reg("kidney_clamp", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="atraumatic", jaw_len=L * 0.34,
                           curve=0.55, ring_r=11, jaw_w=5.0, open_deg=3)


@reg("stone_forceps", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="babcock", jaw_len=L * 0.24,
                           curve=1.05, ring_r=11, jaw_w=4.4)


@reg("lahey_clamp", h=46)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="teeth", jaw_len=L * 0.20,
                           curve=0.75, ring_r=11, jaw_w=4.2, teeth_n=1)


@reg("towel_clip", h=44)
def _(a, o, L): misc_instrument(a, o, L=L, kind="towel_clip")


@reg("sponge_stick", h=44)
def _(a, o, L): misc_instrument(a, o, L=L, kind="sponge_stick")


@reg("tenaculum", h=46)
def _(a, o, L): misc_instrument(a, o, L=L, kind="tenaculum")


# ================================================================== suturing
@reg("needle_holder", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="needle", jaw_len=L * 0.18,
                           curve=0.0, ring_r=11, jaw_w=5.2, open_deg=5)


@reg("needle_holder_long", h=44)
def _(a, o, L):
    ring_handle_instrument(a, o, L=L, jaw="needle", jaw_len=L * 0.13,
                           curve=0.0, ring_r=10.5, jaw_w=4.6, open_deg=4)


@reg("castroviejo_nh", h=34)
def _(a, o, L):
    thumb_forceps(a, o, L=L, tip="serrated", w_top=10, platform=True)


@reg("ligature_carrier", h=44)
def _(a, o, L): misc_instrument(a, o, L=L, kind="ligature_carrier")


# ================================================================ retracting
@reg("army_navy", h=56)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="army")


@reg("richardson", h=56)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="richardson")


@reg("deaver", h=60)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="deaver")


@reg("malleable", h=46)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="malleable")


@reg("senn", h=40)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="senn")


@reg("rake_retractor", h=52)
def _(a, o, L): handheld_retractor(a, o, L=L, kind="rake")


@reg("weitlaner", h=72)
def _(a, o, L): self_retaining(a, o, L=L, kind="weitlaner")


@reg("cerebellar", h=72)
def _(a, o, L): self_retaining(a, o, L=L, kind="cerebellar")


@reg("mastoid_retractor", h=72)
def _(a, o, L): self_retaining(a, o, L=L, kind="mastoid")


@reg("balfour", h=104)
def _(a, o, L): self_retaining(a, o, L=L, kind="balfour")


@reg("finochietto", h=104)
def _(a, o, L): self_retaining(a, o, L=L, kind="finochietto")


# ================================================================= suctioning
@reg("yankauer", h=50)
def _(a, o, L): suction_tip(a, o, L=L, kind="yankauer")


@reg("poole", h=52)
def _(a, o, L): suction_tip(a, o, L=L, kind="poole")


@reg("frazier", h=58)
def _(a, o, L): suction_tip(a, o, L=L, kind="frazier")


# ==================================================================== viewing
@reg("sigmoidoscope", h=80)
def _(a, o, L): endoscope(a, o, L=L, kind="sigmoidoscope")


@reg("proctoscope", h=80)
def _(a, o, L): endoscope(a, o, L=L, kind="proctoscope")


@reg("laparoscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="laparoscope")


@reg("arthroscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="arthroscope")


@reg("choledochoscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="choledochoscope")


@reg("cystoscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="cystoscope")


@reg("bronchoscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="bronchoscope")


@reg("mediastinoscope", h=62)
def _(a, o, L): endoscope(a, o, L=L, kind="mediastinoscope")


@reg("trocar", h=64)
def _(a, o, L): trocar(a, o, L=L, kind="trocar")


@reg("veress", h=44)
def _(a, o, L): trocar(a, o, L=L, kind="veress")


# ==================================================================== specula
@reg("graves_speculum", h=80)
def _(a, o, L): speculum(a, o, L=L, kind="graves")


@reg("sims_speculum", h=62)
def _(a, o, L): speculum(a, o, L=L, kind="sims")


@reg("nasal_speculum", h=56)
def _(a, o, L): speculum(a, o, L=L, kind="nasal")


@reg("ear_speculum", h=42)
def _(a, o, L): speculum(a, o, L=L, kind="ear")


@reg("lid_speculum", h=56)
def _(a, o, L): speculum(a, o, L=L, kind="eyelid")


# =================================================== dilators / sounds / curettes
@reg("hegar_set", h=120, L=120)
def _(a, o, L): dilator_set(a, o, n=6, L=L, kind="hegar", spread=17)


@reg("bakes_set", h=110, L=130)
def _(a, o, L): dilator_set(a, o, n=5, L=L, kind="bakes", spread=20)


@reg("trousseau", h=56)
def _(a, o, L): dilator_set(a, o, L=L, kind="trousseau")


@reg("uterine_curette_sharp", h=48)
def _(a, o, L): curette(a, o, L=L, kind="uterine_sharp")


@reg("uterine_curette_blunt", h=48)
def _(a, o, L): curette(a, o, L=L, kind="uterine_blunt")


@reg("bone_curette", h=44)
def _(a, o, L): curette(a, o, L=L, kind="bone")


@reg("adenoid_curette", h=64)
def _(a, o, L): curette(a, o, L=L, kind="adenoid")


@reg("ear_curette", h=36)
def _(a, o, L): curette(a, o, L=L, kind="ear")


@reg("uterine_sound", h=34)
def _(a, o, L): misc_instrument(a, o, L=L, kind="probe")


@reg("probe", h=34)
def _(a, o, L): misc_instrument(a, o, L=L, kind="probe")


@reg("grooved_director", h=34)
def _(a, o, L): misc_instrument(a, o, L=L, kind="grooved_director")


@reg("lacrimal_probe", h=32)
def _(a, o, L): misc_instrument(a, o, L=L, kind="lacrimal_probe")


# =============================================================== bone / ortho
@reg("rongeur", h=64)
def _(a, o, L): bone_instrument(a, o, L=L, kind="rongeur")


@reg("kerrison", h=76)
def _(a, o, L): bone_instrument(a, o, L=L, kind="kerrison")


@reg("osteotome", h=38)
def _(a, o, L): bone_instrument(a, o, L=L, kind="osteotome")


@reg("chisel", h=38)
def _(a, o, L): bone_instrument(a, o, L=L, kind="chisel")


@reg("gouge", h=38)
def _(a, o, L): bone_instrument(a, o, L=L, kind="gouge")


@reg("mallet", h=68, L=60)
def _(a, o, L): bone_instrument(a, o, L=L, kind="mallet")


@reg("bone_rasp", h=40)
def _(a, o, L): bone_instrument(a, o, L=L, kind="rasp")


@reg("gigli_saw", h=52)
def _(a, o, L): bone_instrument(a, o, L=L, kind="gigli")


@reg("periosteal", h=40)
def _(a, o, L): bone_instrument(a, o, L=L, kind="periosteal")


@reg("bone_holder", h=56)
def _(a, o, L): bone_instrument(a, o, L=L, kind="bone_holder")


@reg("bone_cutter", h=56)
def _(a, o, L): bone_instrument(a, o, L=L, kind="bone_cutter")


@reg("hudson_brace", h=60)
def _(a, o, L): bone_instrument(a, o, L=L, kind="hudson")


# ================================================================= vascular
@reg("bulldog", h=40, L=110)
def _(a, o, L): vascular(a, o, L=L, kind="bulldog")


@reg("satinsky", h=48)
def _(a, o, L): vascular(a, o, L=L, kind="satinsky")


@reg("aortic_punch", h=44)
def _(a, o, L): vascular(a, o, L=L, kind="aortic_punch")


# ================================================================ ENT / eye
@reg("tonsil_snare", h=54)
def _(a, o, L): misc_instrument(a, o, L=L, kind="snare")


@reg("trach_tube", h=76)
def _(a, o, L): misc_instrument(a, o, L=L, kind="trach_tube")


@reg("myringotomy_knife", h=48)
def _(a, o, L): misc_instrument(a, o, L=L, kind="myringotomy")


@reg("mouth_gag", h=64)
def _(a, o, L): misc_instrument(a, o, L=L, kind="mouth_gag")


@reg("tongue_depressor", h=38)
def _(a, o, L): misc_instrument(a, o, L=L, kind="tongue_depressor")


@reg("chalazion_clamp", h=64)
def _(a, o, L): misc_instrument(a, o, L=L, kind="chalazion")


@reg("strabismus_hook", h=48)
def _(a, o, L): misc_instrument(a, o, L=L, kind="strabismus_hook")


@reg("trephine", h=70, L=40)
def _(a, o, L): misc_instrument(a, o, L=L, kind="trephine")


@reg("phaco", h=52)
def _(a, o, L): misc_instrument(a, o, L=L, kind="phaco")


# ==================================================================== other
@reg("rib_shears", h=60)
def _(a, o, L): thoracic_instrument(a, o, L=L, kind="rib_shears")


@reg("rib_raspatory", h=56)
def _(a, o, L): thoracic_instrument(a, o, L=L, kind="rib_raspatory")


@reg("rib_approximator", h=76)
def _(a, o, L): thoracic_instrument(a, o, L=L, kind="rib_approximator")


@reg("sternal_saw", h=56)
def _(a, o, L): thoracic_instrument(a, o, L=L, kind="sternal_saw")


@reg("gi_stapler", h=58)
def _(a, o, L): misc_instrument(a, o, L=L, kind="stapler")


@reg("pacemaker", h=64)
def _(a, o, L): misc_instrument(a, o, L=L, kind="pacemaker")


# ==========================================================================
#  Generic plate renderer
# ==========================================================================
PLATE_W = 470          # logical width of a side-column plate
LABEL_GAP = 6

# ---------------------------------------------------------------------------
# Automatic row sizing
# ---------------------------------------------------------------------------
# The `h` declared with @reg is only a hint. Several drawings (multi-row
# dilator sets, self-retaining retractors, mallets) extend well beyond it,
# which used to make them overflow their row and collide with the next
# label. Rather than maintain 100+ hand-tuned numbers, measure the real ink
# extent of each drawing once and cache it.
_measured = {}


def measured_extent(key, L):
    """(ink_above_origin, ink_below_origin) in logical units, cached."""
    ck = (key, round(L, 1))
    if ck in _measured:
        return _measured[ck]
    from PIL import Image
    fn = R[key][0]
    pad = 220
    a = Art(int(L + 2 * pad), 2 * pad)
    try:
        fn(a, (pad, pad), L)
    except Exception:
        _measured[ck] = (R[key][1] / 2.0, R[key][1] / 2.0)
        return _measured[ck]
    bb = Image.eval(a.im, lambda v: 255 - v).getbbox()
    if not bb:
        res = (R[key][1] / 2.0, R[key][1] / 2.0)
    else:
        res = (pad - bb[1] / SS_, bb[3] / SS_ - pad)
    _measured[ck] = res
    return res


def row_height(key, L, declared):
    """Vertical band a centred drawing actually needs."""
    up, down = measured_extent(key, L)
    return max(declared, int(2 * max(up, down)) + 3)


def plate(rows, title=None, width=PLATE_W, L=None, label_size=9.0,
          title_size=11.0, frame=True, pad_top=None, foot=None,
          label_side="below", row_gap=6):
    """
    Build an Art figure stacking labelled instrument drawings.

    rows: list of (registry_key, label) or (registry_key, label, {"L":..})
    label_side: "below"  -> caption under each drawing (default)
                "right"  -> caption to the right of each drawing
    """
    pad_top = pad_top if pad_top is not None else (24 if title else 10)
    lab_h = 15 if label_side == "below" else 0
    row_gap = max(row_gap, 10)

    def sized(dL):
        """Scale up long instruments to fill the plate; leave compact ones."""
        if L is not None:
            return L
        if dL < 140:            # intrinsically compact (mallet, trephine...)
            return dL
        return width * 0.56

    # resolve each row's drawing length and its true vertical band
    plan = []
    for r in rows:
        key = r[0]
        opts = r[2] if len(r) > 2 else {}
        dL = R[key][2]
        draw_L = opts.get("L", sized(dL))
        up, down = measured_extent(key, draw_L)
        ih = int(up + down) + 3          # band = exactly the ink height
        # offset of the drawing origin from the top of its band
        oy_off = up + 1.5
        plan.append((key, r[1], opts, draw_L, ih, oy_off))

    heights = [ih + lab_h + row_gap for *_, ih, _ in plan]
    total = pad_top + sum(heights) + (18 if foot else 8)

    a = Art(width, total)
    if frame:
        a.frame(w=1.0, fill=LGREY)
    if title:
        a.text((width / 2, 5), title, size=title_size, weight="bold",
               anchor="mt")
        a.seg((width * 0.10, pad_top - 7), (width * 0.90, pad_top - 7),
              w=0.9, fill=MGREY)

    y = pad_top
    for (key, label, opts, draw_L, ih, oy_off), h in zip(plan, heights):
        fn = R[key][0]
        ox = opts.get("x", 26)
        fn(a, (ox, y + oy_off), draw_L)
        if label_side == "right":
            a.text((ox + draw_L + 34, y + ih / 2), label, size=label_size,
                   weight="semi", anchor="lm")
        else:
            a.text((ox - 8, y + ih + 2), label, size=label_size,
                   weight="semi", anchor="lt")
        y += h

    if foot:
        a.text((width / 2, total - 4), foot, size=8.0, weight="it",
               anchor="ms", fill=DGREY)
    return a


def detail_plate(items, title=None, width=PLATE_W, cols=3, r=30,
                 label_size=8.5):
    """Grid of magnified jaw/tip detail circles."""
    rows_n = (len(items) + cols - 1) // cols
    cw = width / cols
    ch = r * 2 + 26
    pad_top = 22 if title else 8
    a = Art(width, pad_top + rows_n * ch + 6)
    a.frame(w=1.0, fill=LGREY)
    if title:
        a.text((width / 2, 5), title, size=11.0, weight="bold", anchor="mt")
    for i, (kind, lab) in enumerate(items):
        cx = cw * (i % cols) + cw / 2
        cy = pad_top + ch * (i // cols) + r + 4
        tip_detail(a, (cx, cy), r=r, kind=kind, label=lab, size=label_size)
    return a
