# PanPanParts — Status 25. marts 2026 (aften)

## Live
- panpanparts.com — Railway Hobby ($5/md)
- HTTPS — venter på Railway certifikat
- UptimeRobot — overvåger siden
- Google Search Console — verificeret, sitemap indsendt

## Database
- 526.081 fly fra USA, Danmark, Norge, Schweiz, Australien, Canada, Østrig, UK, Tyskland, Frankrig + flere
- 93.596 flytyper i aircraft_type tabel (FAA)
- PostgreSQL på Railway (migreret fra SQLite 25/3-2026)
- Daglig backup til AWS S3 (panpanparts-backup, eu-north-1) kl. 00:00

## Features
- Tail# søgning → fly profil
- Flytype søgning → AI beskrivelse + listings + parts
- Login / Register
- Claim aircraft
- ARC upload og AI verificering
- Parts marketplace med AI analyse
- Aircraft for sale listings
- My aircraft / My listings
- Register aircraft manuelt
- Sitemap, About, TOS, robots.txt

## Næste skridt
- HTTPS certifikat (venter)
- Koble part tabel til aircraft_type
- Koble aircraft til aircraft_type via model/manufacturer
- ARC status på My aircraft siden
- Sverige fra officielt register
- Protest claim funktion
- Email notifikationer (ARC udløb)
- Betalingssystem (Stripe)

## Stack
- Python Flask, PostgreSQL, Anthropic AI
- GitHub: ThomasAlgren/aviation-platform
- Railway: aviation-platform-production-cf8f.up.railway.app
- Domain: panpanparts.com (GoDaddy)
- AWS S3: panpanparts-backup (eu-north-1)
