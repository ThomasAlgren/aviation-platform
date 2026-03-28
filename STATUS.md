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
- Logbog foto-upload: venstre/højre fotos vises ikke efter de er taget — skal fixes
- Logbog: Manuel entry — ny flyvning direkte uden scanning
- Logbog: Flere logbøger (Logbog 1, 2, 3) — historisk scanning
- Logbog: Preferred aircraft register per pilot
- Forside: skift til sælger-fokus — "Earn on your parts", skjul 0-tællere
- Holland (PH-): tilføj til månedlig opdatering
- Stripe betalingssystem
- Community funktion (når 20-30 brugere)

## Udført 28. marts 2026
- Månedlig opdatering script (update_registries.py) bygget og testet
- SE, NO, CA, CH, AT opdateres automatisk den 1. hver måned
- Logbog review: godkendte linjer sendes som kontekst til AI
- Logbog review: block time max 5 timer advarsel
- Logbog review: dato-kronologi advarsel
- Logbog review: HHMM → HH:MM auto-formatering

## Udført 28. marts 2026 (fortsat)
- Logbog review: tomme linjer filtreres fra
- Logbog review: licens-baserede AI regler (SPL = kun SEP VFR + Dual)
- Logbog review: max 5 timer block time — ryder felter automatisk
- Logbog review: dato-kronologi — ryder dato og blokerer Approve
- User model: preferred_aircraft kolonne tilføjet
- License type opdateret til SPL for Thomas

## To Do (opdateret)
- Preferred aircraft: UI til at vælge/tilføje fly + brug i AI-prompt
- Preferred aircraft: vis fly-historik (unikke tail#, antal flyvninger, seneste dato)
- Logbog foto-upload: venstre/højre fotos vises ikke — skal fixes
- Logbog: Manuel entry — ny flyvning direkte uden scanning
- Logbog: Flere logbøger (Logbog 1, 2, 3) — historisk scanning
- Forside: skift til sælger-fokus — "Earn on your parts", skjul 0-tællere
- US flyregister: køres på Railway-serveren direkte
- AU flyregister: CASA server timeout — prøv igen næste måned
- DK flyregister: find bedre kilde til aktive OY-fly
- Holland (PH-): tilføj til månedlig opdatering
- Stripe betalingssystem
- Community funktion (når 20-30 brugere)

## Strategi — flyejer administration
- Kobl pilot-logbog entries til flyets timer automatisk
- Tacho/Hobbs time felt i logbogen (ejer fakturerer efter dette)
- Flyets totale timer opdateres når en flyvning logges
- Næste service beregnes automatisk baseret på timer
- Ejer ser hvem der har fløjet flyet og hvornår
- IKKE skole-fakturering (myweblog.se's marked) — fokus på privat flyejer

## Udført 28. marts 2026 (eftermiddag)
- Logbog: My flight history sektion med fly-historik og tilføj nyt fly
- Logbog: Flight Currency barometer (grøn/gul/rød) baseret på 6 måneder
- Logbog: +/- knapper til justering af landinger
- Logbog: adjustLandings defineret i head — fix undefined fejl
- Logbog: JS syntaxfejl i editEntry onclick fixet
- Logbog: scan opdateret med licens-regler og preferred aircraft
- Logbog: tomme linjer filtreres fra ved scanning
- US flyregister: genskabt — 310.823 fly importeret fra lokale FAA filer
- US flyregister: sikker import med temp-tabel — gamle data bevares ved fejl
- Forside: "Earn on your parts" som hero-tekst
- Forside: 0-tællere for dele og fly skjult
- Forside: markeder opdateret til USA, EU, UK, Australia, Canada, Switzerland
- Total flyregister: 525.692 fly

## To Do (opdateret)
- Logbog: edit modal Update-knap virker ikke
- Logbog: Flight Currency opdateres ikke live ved landing-ændring
- Logbog: tabel har 19 kolonner — reducer til de vigtigste
- Logbog: Manuel entry — ny flyvning direkte uden scanning
- Logbog: Preferred aircraft — vis og brug i AI-prompt
- Logbog: Tacho/Hobbs time felt
- Logbog: Flere logbøger (Logbog 1, 2, 3) — historisk scanning
- US flyregister: automatiser månedlig opdatering på Railway-siden
- AU flyregister: CASA server timeout — prøv igen
- DK flyregister: find bedre kilde til aktive OY-fly
- Holland (PH-): tilføj til månedlig opdatering
- Stripe betalingssystem
- Community funktion (når 20-30 brugere)
