"""Build v19 from v18, replacing only OPAC languages and pack description."""
import copy
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Le_Comptoir_v18_Player_Armor_Stand.zip'
TARGET = ROOT / 'Le_Comptoir_v19_OPAC_FR_26.3.zip'
HERE = Path(__file__).resolve().parent
en = json.loads((HERE / 'en_us.source.json').read_text(encoding='utf-8'))
fr = json.loads((HERE / 'fr_fr.json').read_text(encoding='utf-8'))
assert not (en.keys() - fr.keys()), 'Missing translations'
token = re.compile(r'%(?:\d+\$)?[a-zA-Z%]')
for key, value in en.items():
    assert isinstance(fr[key], str) and fr[key].strip(), key
    assert fr[key] != 'default', key
    if value != 'default':
        assert sorted(token.findall(value)) == sorted(token.findall(fr[key])), key
payload = (json.dumps(fr, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
languages = {'assets/openpartiesandclaims/lang/fr_fr.json',
             'assets/openpartiesandclaims/lang/en_us.json'}
with zipfile.ZipFile(SOURCE) as source:
    old = json.loads(source.read('assets/openpartiesandclaims/lang/fr_fr.json'))
    with zipfile.ZipFile(TARGET, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
        for info in source.infolist():
            data = source.read(info.filename)
            if info.filename in languages:
                data = payload
            elif info.filename == 'pack.mcmeta':
                meta = json.loads(data)
                meta['pack']['description'] = 'Le Comptoir des Artisans — icônes, émojis, traductions OPAC 0.33.0 et Player Armor Stand 1.4 par ShorkBee'
                data = (json.dumps(meta, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
            target.writestr(copy.copy(info), data)
    with zipfile.ZipFile(TARGET) as target:
        assert target.testzip() is None
        assert source.namelist() == target.namelist()
        unchanged = [n for n in source.namelist() if n not in languages | {'pack.mcmeta'}]
        assert all(source.read(n) == target.read(n) for n in unchanged)
        assert all(json.loads(target.read(n)) == fr for n in languages)
report = {
    'minecraft': '26.3', 'opac': '0.33.0', 'source_keys': len(en),
    'translation_keys': len(fr), 'missing_keys': [],
    'keys_added_vs_v18': len(en.keys() - old.keys()),
    'format_tokens_valid': True, 'zip_crc_valid': True,
    'unchanged_other_entries': len(unchanged),
    'output': TARGET.name, 'bytes': TARGET.stat().st_size,
    'sha1': hashlib.sha1(TARGET.read_bytes()).hexdigest(),
    'sha256': hashlib.sha256(TARGET.read_bytes()).hexdigest(),
}
(HERE / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
