from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
repls = {
    "style=\"height:'+remPendPct+'%\"": "style=\"height:'+remPendPct.replace(',','.')+'%\"",
    "style=\"height:'+remDonePct+'%\"": "style=\"height:'+remDonePct.replace(',','.')+'%\"",
    "style=\"height:'+manPendPct+'%\"": "style=\"height:'+manPendPct.replace(',','.')+'%\"",
    "style=\"height:'+manDonePct+'%\"": "style=\"height:'+manDonePct.replace(',','.')+'%\"",
}
for old, new in repls.items():
    if old not in text:
        raise SystemExit(f'Missing target: {old}')
    text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
print('Thermometer heights fixed')
