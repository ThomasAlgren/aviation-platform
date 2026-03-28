# PanPanParts — Status 28. marts 2026

## Hvad er PanPanParts
Aviation platform for piloter og flyejere. Tre dele:
1. Flyregister — søg på tail# fra 526K+ fly globalt
2. Marketplace — dele og fly til salg med AI verificering
3. Pilot/fly cockpit — dokumenthåndtering, logbog, certifikater

## Live
- panpanparts.com — HTTPS ✅
- Railway Hobby ($5/md) — gunicorn, 1 worker
- GitHub: ThomasAlgren/aviation-platform
- Railway URL: aviation-platform-production-cf8f.up.railway.app

## Stack
- Python Flask, PostgreSQL (Railway), Anthropic AI (claude-sonnet-4-20250514)
- Resend email (noreply@panpanparts.com)
- AWS S3 backup (panpanparts-backup, eu-north-1)
- ImprovMX email forwarding (info@, support@, thomas@)
- APScheduler: backup kl 02:00, notifikationer kl 02:30, månedlig opdatering d.1 kl 03:00

## Database tabeller
- aircraft (526K+ fly — US, DK, NO, SE, CH, AU, DE, FR, UK + flere)
- aircraft_type (93K FAA flytyper)
- user (login, profil, medical, licens, certifikater)
- claimed_aircraft (ejerskab, ARC, CoA, forsikring, timer, dokumenter)
- pilot_certificate (EASA/FAA certifikater med AI foto-læsning)
- logbook_entry (pilot logbog med AI scanning)
- aircraft_maintenance_log (teknisk logbog for fly)
- claim_protest (disputed claims)
- aircraft_listing (fly til salg)
- part (reservedele til salg)

## Features (alle virker)
- Tail# søgning — genkender OY/LN/SE/HB/VH/G-/D-/F-/N/C- præfikser
- Flytype søgning → AI beskrivelse + listings + parts
- OpenSky live tracking på fly profil
- Login/Register med email verificering + glemt password
- Claim aircraft — ejer kan rette forkert data
- Protest claim — disputed badge
- ARC upload med AI verificering
- My aircraft cockpit (kritiske datoer, dokumenter, timer)
- Aircraft maintenance log (teknisk logbog, AI læser dokumenter)
- Aircraft for sale listings
- Parts marketplace med AI analyse
- My profile (licens, medical, flyvetimer)
- Pilot certifikater — AI læser foto, udløbsdato automatisk
- Pilot logbog — fuld EASA tabel, desktop/mobil layout
- Logbog linje-for-linje review flow (/logbook-review)
- Email notifikationer ved udløb (ARC, medical, certifikater, forsikring)
- Månedlig auto-opdatering af flyregistre (Sverige fra Transportstyrelsen)
- Datoer gemmes som YYYY-MM-DD internt

## Vigtige tekniske detaljer
- SQLite bruges IKKE — alt er PostgreSQL
- get_pg_conn() bruges til direkte PostgreSQL forbindelser
- app.config SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
- Billeder komprimeres i JavaScript til max 1200-1800px før upload
- APScheduler kører i Flask app (ikke separat Railway service)
- normalize_date() konverterer alle datoformater til YYYY-MM-DD

## Næste skridt (prioriteret)
- Test alle features grundigt (logbog scan, liste dele, liste fly)
- Møde med instruktør — vis cockpit og logbog
- KZ Veteranklub og General Aviation Service outreach
- Community funktion (når 20-30 brugere er inde)
- Holland (PH-register) tilføje
- Stripe betalingssystem
- Fly historik baseret på serienummer

## Railway miljøvariable
- DATABASE_URL, SECRET_KEY, ANTHROPIC_API_KEY
- RESEND_API_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
- AWS_S3_BUCKET=panpanparts-backup, AWS_REGION=eu-north-1

## Database status 28. marts 2026
- US: 100.000/310.985 — mangler resten pga Railway timeout
- DK: kun 2 fly fra danishaircraft.dk — historisk register, ikke aktivt
- Sweden/OpenSky duplikat — 63 ekstra SE-fly fra OpenSky skal renses
- AU: 16.590 fly fra gammel CASA fil — timeout ved download i dag
- Total ca. 380.000 fly i databasen lige nu

## To Do
- US flyregister: Kører lokalt mod Railway timeout efter ~100K fly. Skal køres direkte på Railway-serveren via run_monthly_updates i app.py
- AU flyregister: CASA server timeout — prøv igen næste måned
- DK flyregister: danishaircraft.dk er historisk register, kun 2 aktive fly fundet. Find bedre kilde til aktive OY-fly
- Logbog foto-upload: venstre/højre fotos vises ikke efter de er taget
- Logbog review flow: AI lærer ikke af tidligere godkendte linjer
- Logbog dato-kronologi: datoer rettes ikke baseret på tidligere linjer
- Logbog blocktime: indtast 1440, vis 14:40
- Forside: skift til sælger-fokus — "Earn on your parts", skjul 0-tællere
- Holland (PH-): tilføj til månedlig opdatering
