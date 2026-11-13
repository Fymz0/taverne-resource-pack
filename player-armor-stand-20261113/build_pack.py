#!/usr/bin/env python3
"""Merge the active Comptoir pack with ShorkBee's original Player Armor Stand 1.4."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
BASE_SHA1 = "3b33bb903020d18f119573d96efbae01ab35a0a1"
SOURCE_SHA1 = "7e19ed33849c4b01b77fb29147dc086673e68000"
SOURCE_URL = "https://cdn.modrinth.com/data/sLB2cYpz/versions/qheFIWLC/Player%20Armor%20Stand%201.4.zip"
OUTPUT = ROOT / "Le_Comptoir_v18_Player_Armor_Stand.zip"


def digest(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()
    source = args.source or Path(__file__).with_name("Player_Armor_Stand_1.4.zip")
    if not source.exists():
        request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "LeComptoir-ResourcePack/1.0"})
        source.write_bytes(urllib.request.urlopen(request, timeout=60).read())
    baseline = ROOT / "Le_Comptoir_v16_Chat_Emojis.zip"
    assert digest(baseline) == BASE_SHA1, "Unexpected baseline archive"
    assert digest(source) == SOURCE_SHA1, "Unexpected original archive"

    with ZipFile(baseline) as base, ZipFile(source) as armor:
        assert base.testzip() is None and armor.testzip() is None
        base_data = {n: base.read(n) for n in base.namelist() if not n.endswith("/")}
        armor_data = {n: armor.read(n) for n in armor.namelist() if not n.endswith("/")}
    assert set(base_data) & set(armor_data) == {"pack.mcmeta"}
    merged = {**base_data, **{n: b for n, b in armor_data.items() if n != "pack.mcmeta"}}
    metadata = json.loads(base_data["pack.mcmeta"])
    metadata["pack"].update({
        "description": "Le Comptoir des Artisans — icônes, émojis, traductions et Player Armor Stand 1.4 par ShorkBee",
        "pack_format": 88,
        "supported_formats": [88, 99],
        "min_format": 88,
        "max_format": 99,
    })
    merged["pack.mcmeta"] = (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode()
    merged["CREDITS_Player_Armor_Stand.txt"] = (
        "Player Armor Stand 1.4 — ShorkBee\n"
        "Original source: https://modrinth.com/resourcepack/player-armor-stand\n"
        "Original files retained unchanged, except the combined pack metadata.\n"
        "Requires Entity Model Features (EMF) and Entity Texture Features (ETF) on each client.\n"
        "Rename an armor stand: Male1, Female1, Male Sit1, Female Sit1, etc. (1–50).\n"
    ).encode()
    json_files = [n for n in merged if n.endswith((".json", ".jem", ".mcmeta"))]
    for name in json_files:
        json.loads(merged[name])
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED, compresslevel=9) as target:
        for name, data in sorted(merged.items()):
            info = ZipInfo(name, (2026, 11, 13, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            target.writestr(info, data, compresslevel=9)
    with ZipFile(OUTPUT) as target:
        assert target.testzip() is None
        assert len(target.namelist()) == len(set(target.namelist()))
        assert all(target.read(n) == b for n, b in base_data.items() if n != "pack.mcmeta")
        assert all(target.read(n) == b for n, b in armor_data.items() if n != "pack.mcmeta")
    result = {
        "file": OUTPUT.name,
        "bytes": OUTPUT.stat().st_size,
        "sha1": digest(OUTPUT),
        "baseline_sha1": BASE_SHA1,
        "source_sha1": SOURCE_SHA1,
        "unchanged_baseline_files": len(base_data) - 1,
        "unchanged_armor_files": len(armor_data) - 1,
        "total_files": len(merged),
        "valid_json_files": len(json_files),
        "zip_crc": "ok",
    }
    Path(__file__).with_name("validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
