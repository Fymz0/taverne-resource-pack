#!/usr/bin/env python3
"""Build v11: compact profile label with an explicit hover description."""
import copy
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Taverne_Ranks_MCModels_32_Badges_v10_OPAC_BACAP_FR.zip"
OUTPUT = ROOT / "Taverne_Ranks_MCModels_32_Badges_v11_OPAC_BACAP_FR.zip"
REPORT = ROOT / "opac-fr-0.31.6" / "validation-v11.json"
BASE_SHA1 = "20b7f9ac0184f729574e3ab6b533d40621d3e385"
CHANGES = {
    "gui.xaero_pac_ui_sub_config_create_widget": (
        "Nouveau", "Profil +"),
    "gui.xaero_pac_ui_sub_config_create_widget_tooltip": (
        "Saisis l'identifiant du sous-profil à créer.\n%1$s",
        "Créer un nouveau sous-profil. Saisis son identifiant dans la case.\n%1$s"),
}
LANG_FILES = {
    "assets/openpartiesandclaims/lang/fr_fr.json",
    "assets/openpartiesandclaims/lang/en_us.json",
}


def revise(data):
    original = json.loads(data)
    expected = dict(original)
    for key, (before, after) in CHANGES.items():
        assert original[key] == before
        expected[key] = after
        old = (json.dumps(key) + ": " + json.dumps(before, ensure_ascii=False)).encode()
        new = (json.dumps(key) + ": " + json.dumps(after, ensure_ascii=False)).encode()
        assert data.count(old) == 1
        data = data.replace(old, new, 1)
    assert json.loads(data) == expected
    assert {k for k in original if original[k] != expected[k]} == set(CHANGES)
    assert expected["gui.xaero_pac_ui_sub_config_create_widget_tooltip"].count("%1$s") == 1
    return data


def main():
    assert hashlib.sha1(BASE.read_bytes()).hexdigest() == BASE_SHA1
    # OPAC uses width 200, input width 112, input x+w-112-42, label x+2.
    available = 200 - 112 - 42 - 2
    # Vanilla font: Profil = P(6)+r(6)+o(6)+f(5)+i(2)+l(3); space(4), +(6).
    label_width = 6 + 6 + 6 + 5 + 2 + 3 + 4 + 6
    assert label_width < available
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
                assert all(lang[k] == new for k, (_, new) in CHANGES.items())
            report = {
                "filename": OUTPUT.name,
                "base_sha1": BASE_SHA1,
                "sha1": hashlib.sha1(OUTPUT.read_bytes()).hexdigest(),
                "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                "bytes": OUTPUT.stat().st_size,
                "labels": {k: {"before": old, "after": new}
                           for k, (old, new) in CHANGES.items()},
                "layout": {"available_gui_pixels": available,
                           "label_width_gui_pixels": label_width},
                "changed_entries": changed,
                "unchanged_entries": len(after.namelist()) - len(changed),
                "changed_language_keys_per_file": len(CHANGES),
                "checks": ["base checksum", "ZIP CRC", "all JSON valid",
                           "the one tooltip placeholder is retained",
                           "all non-OPAC-language resources byte-identical"],
                "client_visual_validation": "pending after server distributes v11",
            }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
