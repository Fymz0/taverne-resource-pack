#!/usr/bin/env python3
"""Build v10 from v9: fit the new-profile label into OPAC's 44px space."""
import copy
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Taverne_Ranks_MCModels_32_Badges_v9_OPAC_BACAP_FR.zip"
OUTPUT = ROOT / "Taverne_Ranks_MCModels_32_Badges_v10_OPAC_BACAP_FR.zip"
REPORT = ROOT / "opac-fr-0.31.6" / "validation-v10.json"
BASE_SHA1 = "cabf64a53afc9652a8c3df51405d4c42b1409650"
KEY = "gui.xaero_pac_ui_sub_config_create_widget"
OLD, NEW = "Nouveau profil", "Nouveau"
LANG_FILES = {
    "assets/openpartiesandclaims/lang/fr_fr.json",
    "assets/openpartiesandclaims/lang/en_us.json",
}


def revise(data):
    original = json.loads(data)
    assert original[KEY] == OLD
    expected = dict(original, **{KEY: NEW})
    old = (json.dumps(KEY) + ": " + json.dumps(OLD, ensure_ascii=False)).encode()
    new = (json.dumps(KEY) + ": " + json.dumps(NEW, ensure_ascii=False)).encode()
    assert data.count(old) == 1
    data = data.replace(old, new, 1)
    assert json.loads(data) == expected
    assert [k for k in original if original[k] != expected[k]] == [KEY]
    return data


def main():
    assert hashlib.sha1(BASE.read_bytes()).hexdigest() == BASE_SHA1
    # OPAC PlayerConfigScreen: w=200, boxWidth=112.
    # TextWidgetListElement: label x+2; edit box x+w-boxWidth-42.
    available = 200 - 112 - 42 - 2
    # Conservative vanilla ASCII advance bound, 6 GUI pixels per letter.
    width_bound = len(NEW) * 6
    assert width_bound + 2 <= available
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
                assert json.loads(after.read(name))[KEY] == NEW
            report = {
                "filename": OUTPUT.name,
                "base_sha1": BASE_SHA1,
                "sha1": hashlib.sha1(OUTPUT.read_bytes()).hexdigest(),
                "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                "bytes": OUTPUT.stat().st_size,
                "label": {"key": KEY, "before": OLD, "after": NEW},
                "layout": {"available_gui_pixels": available,
                           "new_label_width_upper_bound": width_bound,
                           "minimum_gap_gui_pixels": available - width_bound,
                           "font_assumption": "vanilla ASCII advance at most 6 pixels; custom wider fonts not verified"},
                "changed_entries": changed,
                "unchanged_entries": len(after.namelist()) - len(changed),
                "changed_language_keys_per_file": 1,
                "checks": ["base checksum", "ZIP CRC", "all JSON valid",
                           "only creation label changed in each OPAC language file",
                           "all other resources byte-identical",
                           "label fits OPAC geometry with vanilla ASCII font"],
                "client_visual_validation": "pending after server distributes v10",
            }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
