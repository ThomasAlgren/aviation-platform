# PanPanParts — Aviation Parts & Aircraft Registry

## Vision
VINTED for aviation parts med AI verifikation og Digital Hangar for ejere.

## Database
- USA N- : 305.378 fly
- Danmark OY- : 7.115 fly  
- Norge LN- : 1.038 fly
- Schweiz HB- : 16.686 fly
- Australien VH- : 16.590 fly
- TOTAL: 346.807 fly i SQLite

## Stack
- Python Flask, SQLite, Anthropic AI
- GitHub: ThomasAlgren/aviation-platform
- Render: aviation-platform.onrender.com (deploy fejler - ANTHROPIC_API_KEY mangler?)

## Næste skridt
1. Fix Render deploy (eller skift til Railway)
2. Koble panpanparts.com domæne
3. SEO meta tags og sitemap
4. Parts søgning med AI
5. Sverige SE- register

## Lokalt
cd aviation-platform && source venv/bin/activate
python3 -m flask --app app run --host=0.0.0.0 --port=8888

## Datakilder
- USA: registry.faa.gov (faa_small.csv + faa_ref_small.csv)
- Danmark: oy-reg.dk + danishaircraft.dk (denmark.csv)
- Norge: data.caa.no/nlr/norgesluftfartoyregister.json (ln_register.csv)
- Schweiz: BAZL CSV download (hb_register.csv)
- Australien: CASA acrftreg.csv (vh_register.csv)

