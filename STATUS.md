# PanPanParts — Status 26. marts 2026 (aften)

## Live
- panpanparts.com — HTTPS ✅ Let's Encrypt certifikat
- Railway Hobby ($5/md)
- UptimeRobot — overvåger siden
- Google Search Console — verificeret, sitemap indsendt

## Database (PostgreSQL)
- 526.081 fly fra USA, Danmark, Norge, Schweiz, Australien, Canada, Østrig, UK, Tyskland, Frankrig + flere
- 93.596 flytyper i aircraft_type tabel (FAA)
- Daglig backup til AWS S3 (panpanparts-backup, eu-north-1) kl. 02:00

## Features
- ✅ Hurtig opstart
- ✅ Tail# søgning → fly profil
- ✅ Flytype søgning → AI beskrivelse + listings + parts
- ✅ Søgebar på alle sider
- ✅ Login / Register
- ✅ Email verificering ved oprettelse
- ✅ Glemt password → reset via email
- ✅ Claim aircraft
- ✅ ARC upload og AI verificering
- ✅ Parts marketplace med AI analyse
- ✅ Aircraft for sale listings
- ✅ My aircraft cockpit (ARC, CoA, forsikring, timer, dokumenter)
- ✅ My profile (licens, medical, flyvetimer)
- ✅ Sitemap, About, TOS, robots.txt

## Email
- Resend.com — noreply@panpanparts.com
- Verificerings-email ved registrering
- Password reset email

## Næste skridt
- Email notifikationer (ARC/medical udløb)
- ARC status på My aircraft siden
- Sverige fra officielt register
- Protest claim funktion
- Betalingssystem (Stripe)
- Manufacturer normalisering (Textron→Cessna etc.)

## Stack
- Python Flask, PostgreSQL, Anthropic AI, Resend
- GitHub: ThomasAlgren/aviation-platform
- Railway: aviation-platform-production-cf8f.up.railway.app
- Domain: panpanparts.com (GoDaddy)
- AWS S3: panpanparts-backup (eu-north-1)
