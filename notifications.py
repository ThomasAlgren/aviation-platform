import os
import resend
from datetime import datetime, date, timedelta

resend.api_key = os.environ.get("RESEND_API_KEY")
FROM = "PanPanParts <noreply@panpanparts.com>"

def days_until(date_str):
    if not date_str:
        return None
    for fmt in ['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y']:
        try:
            d = datetime.strptime(date_str, fmt).date()
            return (d - date.today()).days
        except:
            pass
    return None

def send_expiry_email(to_email, name, items):
    rows = ""
    for item in items:
        color = "#ff6b35" if item['days'] < 30 else "#ffc107"
        rows += f"""
        <tr>
            <td style="padding:10px;border-bottom:1px solid #eee">{item['type']}</td>
            <td style="padding:10px;border-bottom:1px solid #eee">{item['expires']}</td>
            <td style="padding:10px;border-bottom:1px solid #eee;color:{color};font-weight:600">{item['days']} days</td>
        </tr>"""
    
    resend.Emails.send({
        "from": FROM,
        "to": to_email,
        "subject": f"PanPanParts — Expiry reminder for {name}",
        "html": f"""
        <div style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:40px 20px">
            <h1 style="color:#ff6b35">PanPan<span style="color:#1a1a2e">Parts</span></h1>
            <h2 style="margin-bottom:8px">Expiry reminder</h2>
            <p style="color:#666;margin-bottom:24px">Hi {name}, the following items are expiring soon:</p>
            <table style="width:100%;border-collapse:collapse;margin-bottom:24px">
                <tr style="background:#f5f5f5">
                    <th style="padding:10px;text-align:left">Item</th>
                    <th style="padding:10px;text-align:left">Expires</th>
                    <th style="padding:10px;text-align:left">Days left</th>
                </tr>
                {rows}
            </table>
            <a href="https://panpanparts.com/my-profile" 
               style="background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600">
                View my profile →
            </a>
            <p style="color:#999;font-size:12px;margin-top:24px">
                You receive this because you have an account on PanPanParts.com
            </p>
        </div>
        """
    })

def check_and_notify(app, db, User, ClaimedAircraft, PilotCertificate):
    with app.app_context():
        users = User.query.all()
        notified = 0
        
        for user in users:
            if not user.email or not user.email_verified:
                continue
            
            items_to_notify = []
            
            # Medical
            days = days_until(user.medical_valid_until)
            if days is not None and 0 <= days <= 60:
                items_to_notify.append({
                    'type': f'Medical ({user.medical_class or ""})',
                    'expires': user.medical_valid_until,
                    'days': days
                })
            
            # Licens
            days = days_until(user.license_valid_until)
            if days is not None and 0 <= days <= 60:
                items_to_notify.append({
                    'type': f'Pilot licence ({user.license_type or ""})',
                    'expires': user.license_valid_until,
                    'days': days
                })
            
            # Pilot certifikater
            certs = PilotCertificate.query.filter_by(user_id=user.id).all()
            for cert in certs:
                days = days_until(cert.valid_until)
                if days is not None and 0 <= days <= 60:
                    items_to_notify.append({
                        'type': cert.cert_type,
                        'expires': cert.valid_until,
                        'days': days
                    })
            
            # Claimed aircraft
            import json
            claimed_tails = json.loads(user.claimed_aircraft or '[]')
            for tail in claimed_tails:
                ca = ClaimedAircraft.query.filter_by(tail=tail).first()
                if not ca:
                    continue
                
                # ARC
                days = days_until(ca.arc_valid_until)
                if days is not None and 0 <= days <= 60:
                    items_to_notify.append({
                        'type': f'ARC — {tail}',
                        'expires': ca.arc_valid_until,
                        'days': days
                    })
                
                # Forsikring
                days = days_until(ca.insurance_valid_until)
                if days is not None and 0 <= days <= 60:
                    items_to_notify.append({
                        'type': f'Insurance — {tail}',
                        'expires': ca.insurance_valid_until,
                        'days': days
                    })
                
                # CoA
                days = days_until(ca.coa_valid_until)
                if days is not None and 0 <= days <= 60:
                    items_to_notify.append({
                        'type': f'CoA — {tail}',
                        'expires': ca.coa_valid_until,
                        'days': days
                    })
            
            if items_to_notify:
                try:
                    send_expiry_email(user.email, user.name, items_to_notify)
                    notified += 1
                    print(f"Notified {user.email}: {len(items_to_notify)} items")
                except Exception as e:
                    print(f"Email fejl for {user.email}: {e}")
        
        print(f"Notifications sent: {notified}")
