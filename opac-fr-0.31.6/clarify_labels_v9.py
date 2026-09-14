#!/usr/bin/env python3
"""Build v9 from published v8 with clearer French OPAC labels."""
import copy
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Taverne_Ranks_MCModels_32_Badges_v8_OPAC_BACAP_FR.zip"
OUTPUT = ROOT / "Taverne_Ranks_MCModels_32_Badges_v9_OPAC_BACAP_FR.zip"
REPORT = ROOT / "opac-fr-0.31.6" / "validation-v9.json"
CHANGES = {
    "gui.xaero_pac_ui_my_player_config": ("Mes réglages", "Mes claims"),
    "gui.xaero_pac_config_option_sub_inherited": ("Hérité", "Par défaut"),
}
TOOLTIP_OLD = "Hérité : valeur du profil parent."
TOOLTIP_NEW = "Par défaut : reprend le réglage du profil parent (par exemple, main pour base)."
LANG_FILES = {
    "assets/openpartiesandclaims/lang/fr_fr.json",
    "assets/openpartiesandclaims/lang/en_us.json",
}
BASE_SHA1 = "c2520ca7994cd30be1be83ca50b0f3f77f5b7d6f"

def revise(data):
    original = json.loads(data)
    expected = dict(original)
    for key, (old, new) in CHANGES.items():
        assert original[key] == old
        expected[key] = new
    tooltips = [k for k, v in original.items() if TOOLTIP_OLD in v]
    assert len(tooltips) == 93
    for key in tooltips:
        assert "tooltip" in key
        expected[key] = expected[key].replace(TOOLTIP_OLD, TOOLTIP_NEW)
    for key in list(CHANGES) + tooltips:
        old = json.dumps(key) + ": " + json.dumps(original[key], ensure_ascii=False)
        new = json.dumps(key) + ": " + json.dumps(expected[key], ensure_ascii=False)
        assert data.count(old.encode()) == 1
        data = data.replace(old.encode(), new.encode(), 1)
    assert json.loads(data) == expected
    assert sum(original[k] != expected[k] for k in original) == 95
    assert not any("Hérité" in v for v in expected.values())
    return data

def main():
    assert hashlib.sha1(BASE.read_bytes()).hexdigest() == BASE_SHA1
    with zipfile.ZipFile(BASE) as before:
        assert before.testzip() is None
        assert len(before.namelist()) == len(set(before.namelist()))
        assert LANG_FILES <= set(before.namelist())
        with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as out:
            for info in before.infolist():
                data = before.read(info.filename)
                if info.filename in LANG_FILES:
                    data = revise(data)
                out.writestr(copy.copy(info), data)
        with zipfile.ZipFile(OUTPUT) as after:
            assert after.testzip() is None
            assert before.namelist() == after.namelist()
            changed = [n for n in before.namelist() if before.read(n) != after.read(n)]
            assert set(changed) == LANG_FILES
            for name in after.namelist():
                if name.endswith((".json", ".mcmeta")):
                    json.loads(after.read(name))
            for name in LANG_FILES:
                lang = json.loads(after.read(name))
                assert all(lang[k] == pair[1] for k, pair in CHANGES.items())
            report = {
                "filename": OUTPUT.name, "base_sha1": BASE_SHA1,
                "sha1": hashlib.sha1(OUTPUT.read_bytes()).hexdigest(),
                "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                "bytes": OUTPUT.stat().st_size,
                "labels": {k: {"before": old, "after": new} for k, (old, new) in CHANGES.items()},
                "tooltip_explanation": TOOLTIP_NEW,
                "updated_tooltips": 93,
                "changed_entries": changed,
                "unchanged_entries": len(after.namelist()) - len(changed),
                "checks": ["base checksum", "ZIP CRC", "all JSON valid",
                           "only two labels and their inheritance explanations changed",
                           "all other resources byte-identical"],
                "client_visual_validation": "pending",
            }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
