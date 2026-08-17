#!/usr/bin/env python3
"""schema.py -- tiny constructors for the note content."""


def T(no, title, aka=None, lead="", uses=None, plate=None, groups=None,
      side_box=None, points=None, figs=None, compare=None, extras=None,
      draping=None, mnemonic=None, pitfalls=None, qa=None, newpage=True,
      groups_title=None):
    """One tray chapter."""
    return {
        "no": no, "title": title, "aka": aka, "lead": lead,
        "uses": uses or [], "plate": plate, "groups": groups or [],
        "side_box": side_box, "points": points or [], "figs": figs or [],
        "compare": compare, "extras": extras or [], "draping": draping,
        "mnemonic": mnemonic, "pitfalls": pitfalls or [], "qa": qa or [],
        "newpage": newpage, "groups_title": groups_title,
    }


def P(number, title, subtitle=None, intro=None, trays=None, chapters=None):
    """One part (a group of chapters)."""
    return {"number": number, "title": title, "subtitle": subtitle,
            "intro": intro, "trays": trays or [], "chapters": chapters or []}


def PL(title, rows, cap=None, width=470, L=None, foot=None):
    """A side-column instrument plate spec."""
    return {"kind": "plate", "title": title, "rows": rows, "cap": cap,
            "width": width, "L": L, "foot": foot}


def DP(title, items, cap=None, cols=3, r=30, width=470):
    """A magnified jaw/tip detail-grid spec."""
    return {"kind": "detail", "title": title, "items": items, "cap": cap,
            "cols": cols, "r": r, "width": width}


def FIG(name, cap=None, w=None, side=False):
    """Reference to a pre-rendered conceptual diagram from diagrams.py."""
    return {"kind": "diagram", "name": name, "cap": cap, "w": w, "side": side}


def G(group, items):
    return {"group": group, "items": items}


def CMP(head, rows, widths=None, cap=None, font_size=9.2):
    return {"head": head, "rows": rows, "widths": widths, "cap": cap,
            "font_size": font_size}
