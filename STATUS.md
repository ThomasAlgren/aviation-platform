# PanPanParts — Status 28. marts 2026

## Live
- panpanparts.com — HTTPS ✅
- Railway Hobby ($5/md)
- UptimeRobot, Google Search Console

## Database (PostgreSQL)
- 526.081 fly
- 93.596 flytyper
- pilot_certificate, logbook_entry, claim_protest tabeller
- aircraft_maintenance_log tabel
- Daglig S3 backup

## Features
- ✅ Tail# søgning → fly profil
- ✅ Flytype søgning → AI beskrivelse
- ✅ Live tracking via OpenSky API
- ✅ Login/Register med email verificering
- ✅ Glemt password
- ✅ Claim aircraft + protest claim
- ✅ Ejer kan rette flydata
- ✅ ARC upload med AI verificering
- ✅ Parts marketplace med AI
- ✅ Aircraft for sale listings
- ✅ My aircraft cockpit
- ✅ Aircraft maintenance log — AI læser dokumenter
- ✅ My profile (licens, medical, flyvetimer)
- ✅ Pilot certifikater — AI læser foto automatisk
- ✅ Pilot logbog — fuld EASA tabel desktop/mobil
- ✅ Logbog: linje-for-linje review flow
- ✅ Logbog: total timer, validering mod sidetotaler
- ✅ Email: info@, support@, thomas@panpanparts.com

## Næste skridt
- 🔲 Email notifikationer (ARC/medical/certifikat udløb)
- 🔲 Sverige register
- 🔲 Stripe betalingssystem
- 🔲 Logbog: aircraft logbog forbedringer

## Stack
- Python Flask, PostgreSQL, Anthropic AI, Resend
- GitHub: ThomasAlgren/aviation-platform
- Railway: aviation-platform-production-cf8f.up.railway.app
- Domain: panpanparts.com (GoDaddy)
- AWS S3: panpanparts-backup (eu-north-1)
