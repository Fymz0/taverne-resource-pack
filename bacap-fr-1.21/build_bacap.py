"""Build server resource pack v8 from v7 and the supplied official BACAP 1.21 language ZIP."""
import argparse, collections, copy, hashlib, json, re, zipfile
from pathlib import Path

V7_SHA256 = '2c38d489cc87f3e25d7e6121600c1b1d63025f6143b480184d141d584e125d78'
SOURCE_SHA256 = '63b82a4251cac526f9677480f3ba14a1f93fab89206c29004fe63adfb44ca864'
NAME = 'Taverne_Ranks_MCModels_32_Badges_v8_OPAC_BACAP_FR.zip'
EXAMPLE = "For example, if Alex and Steve are on Blue team and Steve gets 'Monster Hunter', Steve will have this score increase by 1, but when Alex gets it they won't. If Bob is on Red team and gets 'Monster Hunter' after Steve did, they will have this score increase by 1"
FIXES = {
    'Ahoy!': 'Ohé, du bateau !',
    EXAMPLE: "Par exemple, si Alex et Steve sont dans l’équipe bleue et que Steve obtient le progrès « Chasseur de monstres », ce score augmente de 1. Si Alex l’obtient ensuite, il n’augmente pas. Si Bob, dans l’équipe rouge, obtient ce progrès après Steve, le score de son équipe augmente de 1.",
    'Item Rewards:': 'Objets en récompense :',
    'Potions Milestone': 'Alchimiste accompli',
    'The Stink Bomb': 'La bombe puante',
}
CREDITS = '''BACAP — traduction française pour Le Comptoir des Artisans

Datapack : BlazeandCave's Advancements Pack 1.21, par Cavinator1.
https://modrinth.com/datapack/blazeandcaves-advancements-pack
Source linguistique : BACAP Language Pack 1.21, fourni par l’utilisateur.
https://modrinth.com/resourcepack/bacap-language-pack
Traduction française : Personnedu59, avec les contributions de Zangdarss,
Chucky2401 et TaeliaDideaux, selon l’en-tête du fichier fourni.

Adaptations du Comptoir : quatre clés complétées ou corrigées et une valeur
vide traduite ; commentaires retirés et JSON normalisé. La dernière valeur
des clés dupliquées est conservée, conformément au chargement habituel.
Les noms propres et références culturelles de la traduction sont conservés.
La traduction française est également placée dans en_us comme langue de repli,
selon la convention du pack serveur. Les identifiants de progrès sont inchangés.

Les droits et attributions des ressources d’origine restent applicables.
Cette adaptation n’est pas une nouvelle version officielle de BACAP.
Les crédits et licences du pack serveur v7 sont conservés dans cette archive.
'''

def parse_language(z, name):
    raw = z.read('assets/minecraft/lang/' + name + '.json').decode('utf-8-sig')
    # The supplied files use full-line # comments. No removal within strings.
    clean = '\n'.join(line for line in raw.splitlines() if not line.lstrip().startswith('#'))
    pairs = json.loads(clean, object_pairs_hook=lambda items: items)
    assert all(isinstance(k, str) and isinstance(v, str) for k,v in pairs)
    count = collections.Counter(k for k,v in pairs)
    return dict(pairs), {k:n for k,n in count.items() if n>1}

def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('v7',type=Path);ap.add_argument('source',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    assert hashlib.sha256(a.v7.read_bytes()).hexdigest() == V7_SHA256
    assert hashlib.sha256(a.source.read_bytes()).hexdigest() == SOURCE_SHA256
    a.out.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(a.source) as source, zipfile.ZipFile(a.v7) as old:
        assert source.testzip() is None and old.testzip() is None
        fr,duplicates=parse_language(source,'fr_fr');base,_=parse_language(source,'base_language_file')
        missing=sorted(set(base)-set(fr));empty=[k for k,v in fr.items() if not v]
        assert set(missing) == set(FIXES)-{'The Stink Bomb'} and empty == ['The Stink Bomb']
        fr.update(FIXES);fr.pop('__END OF FILE__',None)
        expected=set(base)-{'__END OF FILE__'}
        assert expected<=set(fr) and all(fr.values())
        params=re.compile(r'%(?:\d+\$)?[sd]')
        assert all(params.findall(k)==params.findall(v) for k,v in fr.items())
        modifications={}
        for lang in ['fr_fr','en_us']:
            path='assets/minecraft/lang/'+lang+'.json';previous=json.loads(old.read(path))
            assert not (set(previous)&set(fr)), 'Existing translation collision'
            modifications[path]=encoded({**previous,**fr})
        metadata=json.loads(old.read('pack.mcmeta'))
        metadata['pack']['description']='Le Comptoir des Artisans — Grades, badges, OPAC et BACAP en français'
        modifications['pack.mcmeta']=encoded(metadata)
        output=a.out/NAME
        with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as new:
            for entry in old.infolist():
                payload=modifications.get(entry.filename,old.read(entry.filename))
                new.writestr(copy.copy(entry),payload)
            info=zipfile.ZipInfo('BACAP-CREDITS-FR.txt',(2026,9,14,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            new.writestr(info,CREDITS.encode('utf-8'))
        with zipfile.ZipFile(output) as new:
            assert new.testzip() is None
            assert len(new.namelist())==len(set(new.namelist()))
            preserved=[n for n in old.namelist() if n not in modifications]
            assert all(new.read(n)==old.read(n) for n in preserved)
            for lang in ['fr_fr','en_us']:
                n='assets/minecraft/lang/'+lang+'.json';before=json.loads(old.read(n));after=json.loads(new.read(n))
                assert all(after[k]==v for k,v in before.items())
                assert all(after[k]==v for k,v in fr.items())
            # Validate every actual JSON asset and metadata using strict JSON.
            for n in new.namelist():
                if n.endswith('.json') or n=='pack.mcmeta': json.loads(new.read(n))
            assert json.loads(new.read('pack.mcmeta'))['pack']['min_format']==88
            assert json.loads(new.read('pack.mcmeta'))['pack']['max_format']==88
        validation={'filename':NAME,'bytes':output.stat().st_size,'sha1':hashlib.sha1(output.read_bytes()).hexdigest(),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'source_sha256':SOURCE_SHA256,'v7_sha256':V7_SHA256,'french_entries_added_per_language':len(fr),'template_keys_covered':len(expected),'missing_template_keys':[],'empty_translations':[],'format_parameters_preserved':True,'duplicate_source_keys_normalized':duplicates,'source_missing_keys_completed':missing,'source_empty_keys_completed':empty,'old_entries_preserved_byte_for_byte':len(preserved),'existing_minecraft_translations_preserved':True,'opac_language_files_unchanged':True,'json_strict_valid':True,'zip_crc_valid':True,'minecraft_resource_format':88,'runtime_load_verified':False,'visual_verified':False,'notes':'Coverage checked against supplied BACAP 1.21 translation template; game references and rendered text not yet verified.'}
        (a.out/'fr_fr.json').write_bytes(encoded(fr));(a.out/'validation.json').write_bytes(encoded(validation));(a.out/'credits.txt').write_text(CREDITS,encoding='utf-8')
        print(json.dumps(validation,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
