# PanPanParts — Status 26. marts 2026 (sen eftermiddag)

## Live
- panpanparts.com — HTTPS ✅ Let's Encrypt certifikat
- Railway Hobby ($5/md)
- UptimeRobot — overvåger siden
- Google Search Console — verificeret, sitemap indsendt

## Database (PostgreSQL)
- 526.081 fly fra USA, Danmark, Norge, Schweiz, Australien, Canada, Østrig, UK, Tyskland, Frankrig + flere
- 93.596 flytyper i aircraft_type tabel (FAA)
- Alle tabeller i PostgreSQL — SQLite ikke længere i brug
- Daglig backup til AWS S3 (panpanparts-backup, eu-north-1) kl. 02:00

## Features
- ✅ Hurtig opstart — ingen loading ventetid
- ✅ Tail# søgning → fly profil
- ✅ Flytype søgning → AI beskrivelse + listings + parts
- ✅ Søgebar på alle sider
- ✅ Login / Register
- ✅ Claim aircraft
- ✅ ARC upload og AI verificering
- ✅ Parts marketplace med AI analyse
- ✅ fits_manufacturer + fits_model på parts
- ✅ Aircraft for sale listings
- ✅ My aircraft cockpit (ARC, CoA, forsikring, timer, dokumenter)
- ✅ My profile (licens, medical, flyvetimer)
- ✅ My listings
- ✅ Register aircraft manuelt
- ✅ Sitemap, About, TOS, robots.txt

## Næste skridt
- Email notifikationer (ARC/medical udløb)
- ARC status på My aircraft siden
- Sverige fra officielt register
- Protest claim funktion
- Betalingssystem (Stripe)
- Slet cron job service på Railway
- Manufacturer normalisering (Textron→Cessna etc.)

## Stack
- Python Flask, PostgreSQL, Anthropic AI
- GitHub: ThomasAlgren/aviation-platform
- Railway: aviation-platform-production-cf8f.up.railway.app
- Domain: panpanparts.com (GoDaddy)
- AWS S3: panpanparts-backup (eu-north-1)
- Anthropic API: aktiv
