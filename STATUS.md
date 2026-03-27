# PanPanParts — Status 27. marts 2026 (aften)

## Live
- panpanparts.com — HTTPS ✅
- Railway Hobby ($5/md)
- UptimeRobot, Google Search Console

## Database (PostgreSQL)
- 526.081 fly
- 93.596 flytyper
- pilot_certificate, logbook_entry, claim_protest tabeller
- Daglig S3 backup

## Features
- ✅ Tail# søgning → fly profil
- ✅ Flytype søgning → AI beskrivelse
- ✅ Login/Register med email verificering
- ✅ Glemt password
- ✅ Claim aircraft + protest claim
- ✅ Ejer kan rette flydata
- ✅ ARC upload med AI verificering
- ✅ Parts marketplace med AI
- ✅ Aircraft for sale listings
- ✅ My aircraft cockpit
- ✅ My profile (licens, medical, flyvetimer)
- ✅ Pilot certifikater — AI læser foto automatisk
- ✅ Pilot logbog — AI scanner sider
- ✅ Logbog: desktop fuld EASA tabel / mobil kompakt
- ✅ Logbog: total timer, validering mod sidetotaler
- ✅ Logbog: edit entries, bevar rækkefølge
- ✅ Email: info@, support@, thomas@panpanparts.com

## Næste skridt (prioriteret)
- 🔲 Logbog: linje-for-linje review flow med AI læringsloop
- 🔲 Logbog: aircraft logbog (teknisk/vedligehold)
- 🔲 OpenSky live tracking på fly profil
- 🔲 Email notifikationer (ARC/medical/certifikat udløb)
- 🔲 Sverige register
- 🔲 Stripe betalingssystem

## Stack
- Python Flask, PostgreSQL, Anthropic AI, Resend
- GitHub: ThomasAlgren/aviation-platform
- Railway: aviation-platform-production-cf8f.up.railway.app
- Domain: panpanparts.com (GoDaddy)
- AWS S3: panpanparts-backup (eu-north-1)

## Logbog review flow — plan
Bygge linje-for-linje review flow:
1. Bruger uploader logbogsside foto
2. AI læser ALLE rækker på én gang men præsenterer dem én ad gangen
3. Bruger ser linje 1 → godkender eller retter felter
4. Godkendt linje gemmes i DB + sendes til AI som kontekst
5. AI bruger godkendte linjer som reference til næste linje
6. Gentages til alle linjer er godkendt

Teknisk:
- Ny route: /logbook-review
- Session storage til midlertidige rækker
- Step-by-step UI med Approve/Edit knapper
- AI kontekst bygges op linje for linje
