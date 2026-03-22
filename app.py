from flask import Flask, render_template_string, request
import pandas as pd

app = Flask(__name__)

print("Loader FAA data...")
df = pd.read_pickle("faa_master.pkl")
ref = pd.read_pickle("faa_ref.pkl")
print("Klar!")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SkyReg - Aircraft Search</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; background: #f0f4f8; color: #1a1a2e; }
        .header { background: #1a1a2e; color: white; padding: 20px 40px; display: flex; align-items: center; gap: 16px; }
        .header h1 { font-size: 24px; font-weight: 600; }
        .header span { color: #4a9eff; }
        .search-box { background: white; padding: 40px; margin: 40px auto; max-width: 800px; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
        input, select { padding: 12px 16px; border: 1px solid #ddd; border-radius: 8px; font-size: 15px; width: 100%; }
        input:focus { outline: none; border-color: #4a9eff; }
        button { background: #1a1a2e; color: white; border: none; padding: 12px 32px; border-radius: 8px; font-size: 15px; cursor: pointer; }
        .search-row { display: flex; gap: 12px; margin-bottom: 16px; }
        .results { max-width: 800px; margin: 0 auto 40px; }
        .result-count { color: #666; margin-bottom: 16px; font-size: 14px; }
        .aircraft-card { background: white; border-radius: 12px; padding: 20px 24px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; justify-content: space-between; align-items: center; }
        .aircraft-info h3 { font-size: 16px; margin-bottom: 4px; }
        .aircraft-info p { color: #666; font-size: 14px; }
        .tail { font-size: 22px; font-weight: 700; color: #4a9eff; font-family: monospace; }
        .status-v { background: #e6f4ea; color: #2d7a3a; padding: 4px 10px; border-radius: 20px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Sky<span>Reg</span></h1>
        <p style="color:#aaa; font-size:14px;">Aviation Registry & Marketplace</p>
    </div>
    <div class="search-box">
        <h2 style="margin-bottom:20px;">Search Aircraft</h2>
        <form method="GET">
            <div class="search-row">
                <input name="tail" placeholder="Tail number (e.g. N12345)" value="{{ tail }}">
                <input name="model" placeholder="Model (e.g. 172)" value="{{ model }}">
            </div>
            <div class="search-row">
                <select name="state">
                    <option value="">All States</option>
                    {% for s in states %}
                    <option value="{{ s }}" {% if s == state %}selected{% endif %}>{{ s }}</option>
                    {% endfor %}
                </select>
                <input name="year_from" placeholder="Year from" value="{{ year_from }}" style="width:50%">
                <input name="year_to" placeholder="Year to" value="{{ year_to }}" style="width:50%">
                <button type="submit">Search</button>
            </div>
        </form>
    </div>
    {% if results is not none %}
    <div class="results">
        <p class="result-count">{{ result_count }} aircraft found</p>
        {% for r in results %}
        <div class="aircraft-card">
            <div class="aircraft-info">
                <h3>{{ r.model }}</h3>
                <p>{{ r.name }} &bull; {{ r.city }}, {{ r.state }}</p>
                <p style="color:#999; font-size:13px; margin-top:4px;">{{ r.year }}</p>
            </div>
            <div style="text-align:right">
                <div class="tail">N{{ r.tail }}</div>
                <div class="status-v">Active</div>
            </div>
        </div>
        {% endfor %}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    tail = request.args.get("tail", "")
    model = request.args.get("model", "")
    state = request.args.get("state", "")
    year_from = request.args.get("year_from", "")
    year_to = request.args.get("year_to", "")
    states = sorted(df["STATE"].dropna().unique().tolist())
    results = None
    result_count = 0
    if any([tail, model, state, year_from, year_to]):
        filtered = df[df["STATUS CODE"].str.strip() == "V"].copy()
        if tail:
            filtered = filtered[filtered["ï»¿N-NUMBER"].astype(str).str.strip() == tail.upper().replace("N","")]
        if state:
            filtered = filtered[filtered["STATE"] == state]
        if year_from:
            filtered = filtered[pd.to_numeric(filtered["YEAR MFR"], errors="coerce") >= int(year_from)]
        if year_to:
            filtered = filtered[pd.to_numeric(filtered["YEAR MFR"], errors="coerce") <= int(year_to)]
        if model:
            koder = ref[ref["MODEL"].astype(str).str.contains(model.upper(), na=False)]["ï»¿CODE"].astype(str).str.strip().tolist()
            filtered = filtered[filtered["MFR MDL CODE"].astype(str).str.strip().isin(koder)]
        result_count = len(filtered)
        filtered = filtered.head(50)
        results = []
        for _, row in filtered.iterrows():
            results.append({
                "tail": str(row["ï»¿N-NUMBER"]).strip(),
                "model": str(row["MFR MDL CODE"]).strip(),
                "name": str(row["NAME"]).strip(),
                "city": str(row["CITY"]).strip(),
                "state": str(row["STATE"]).strip(),
                "year": str(row["YEAR MFR"]).strip(),
            })
    return render_template_string(HTML, tail=tail, model=model, state=state,
        year_from=year_from, year_to=year_to, states=states,
        results=results, result_count=result_count)

if __name__ == "__main__":
    app.run(debug=True)
