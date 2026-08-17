#!/usr/bin/env python3
"""Check every plate row in every content module against the registry."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from registry import R
from diagrams import DIAGRAMS

MODULES = [
    ("content_foundations", "FOUNDATIONS"),
    ("content_general", "GENERAL"),
    ("content_gyn", "GYN"),
    ("content_gu", "GU"),
    ("content_thoracic", "THORACIC"),
    ("content_cardio", "CARDIO"),
    ("content_ortho", "ORTHO"),
    ("content_neuro", "NEURO"),
    ("content_ent", "ENT"),
    ("content_eye", "EYE"),
    ("content_peds", "PEDS"),
]

DETAIL_KINDS = {"1x2", "ratteeth", "serrated", "smooth", "debakey", "allis",
                "babcock", "kocher", "scissor", "needle"}


def main():
    bad = []
    n_plates = n_rows = n_trays = 0
    used = set()

    for modname, attr in MODULES:
        try:
            mod = __import__(modname)
            part = getattr(mod, attr)
        except (ImportError, AttributeError):
            continue
        for tray in part["trays"]:
            n_trays += 1
            specs = []
            if tray.get("plate"):
                specs.append(tray["plate"])
            specs.extend(tray.get("figs", []))
            for s in specs:
                if s.get("kind") == "plate":
                    n_plates += 1
                    for row in s["rows"]:
                        n_rows += 1
                        key = row[0]
                        used.add(key)
                        if key not in R:
                            bad.append((modname, tray["no"], "registry", key))
                elif s.get("kind") == "detail":
                    n_plates += 1
                    for kind, _lab in s["items"]:
                        n_rows += 1
                        if kind not in DETAIL_KINDS:
                            bad.append((modname, tray["no"], "detail", kind))
                elif s.get("kind") == "diagram":
                    if s["name"] not in DIAGRAMS:
                        bad.append((modname, tray["no"], "diagram",
                                    s["name"]))

    print(f"chapters={n_trays}  figures={n_plates}  rows={n_rows}")
    print(f"registry entries={len(R)}  used={len(used)}  "
          f"unused={len(set(R) - used)}")
    if bad:
        print(f"\n{len(bad)} BAD REFERENCES:")
        for m, no, kind, key in bad:
            print(f"  {m} {no}: unknown {kind} key '{key}'")
        return 1
    print("\nAll figure references resolve.")
    unused = sorted(set(R) - used)
    if unused:
        print(f"\n(unused registry entries: {', '.join(unused)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
