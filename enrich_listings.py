import os
import json
import time
import psycopg2
import psycopg2.extras
import anthropic

# Hent database connection
DATABASE_URL = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# Hent alle listings der mangler AI-behandling
cur.execute("""
    SELECT id, manufacturer, model, year, description, hours_total
    FROM aircraft_listing 
    WHERE ai_description IS NULL AND status = 'active'
    ORDER BY id
""")
listings = cur.fetchall()
print(f"Fundet {len(listings)} listings der skal beriges")

client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

for i, listing in enumerate(listings):
    try:
        print(f"[{i+1}/{len(listings)}] Beriger {listing['manufacturer']} {listing['model']} (id={listing['id']})")
        
        prompt = f"""Extract structured data from this aircraft listing. Return ONLY JSON, no markdown.

Aircraft: {listing['manufacturer']} {listing['model']} {listing['year']}
Description: {listing['description'] or ''}

Return exactly this JSON structure:
{{
  "ai_description": "2-3 sentence professional summary of the aircraft",
  "ai_highlights": ["highlight 1", "highlight 2", "highlight 3"],
  "ai_specs": {{
    "engine": "engine name or null",
    "avionics": "main avionics or null",
    "seats": number or null,
    "cruise_kt": number or null,
    "range_nm": number or null,
    "useful_load_kg": number or null
  }},
  "has_autopilot": true or false,
  "has_adsb": true or false,
  "is_hangared": true or false
}}"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}]
        )
        
        text = response.content[0].text.replace("```json","").replace("```","").strip()
        data = json.loads(text)
        
        # Opdater database
        update_cur = conn.cursor()
        update_cur.execute("""
            UPDATE aircraft_listing SET
                ai_description = %s,
                ai_highlights = %s,
                ai_specs = %s,
                has_autopilot = %s,
                has_adsb = %s,
                is_hangared = %s
            WHERE id = %s
        """, (
            data.get('ai_description'),
            json.dumps(data.get('ai_highlights', [])),
            json.dumps(data.get('ai_specs', {})),
            data.get('has_autopilot', False),
            data.get('has_adsb', False),
            data.get('is_hangared', False),
            listing['id']
        ))
        conn.commit()
        
        # Kort pause så vi ikke overbelaster API
        time.sleep(0.3)
        
    except Exception as e:
        print(f"  ❌ Fejl på id={listing['id']}: {e}")
        conn.rollback()
        continue

conn.close()
print("✅ Færdig!")
