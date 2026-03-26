import resend
import os

resend.api_key = os.environ.get("RESEND_API_KEY")

FROM = "PanPanParts <noreply@panpanparts.com>"

def send_verification_email(to_email, name, token):
    url = f"https://panpanparts.com/verify-email/{token}"
    resend.Emails.send({
        "from": FROM,
        "to": to_email,
        "subject": "Verify your PanPanParts account",
        "html": f"""
        <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:40px 20px">
            <h1 style="color:#ff6b35">PanPan<span style="color:#1a1a2e">Parts</span></h1>
            <h2>Welcome, {name}!</h2>
            <p style="color:#666">Please verify your email address to activate your account.</p>
            <a href="{url}" style="display:inline-block;background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;margin:24px 0">
                Verify email address
            </a>
            <p style="color:#999;font-size:13px">Link expires in 24 hours. If you didn't sign up, ignore this email.</p>
        </div>
        """
    })

def send_password_reset_email(to_email, name, token):
    url = f"https://panpanparts.com/reset-password/{token}"
    resend.Emails.send({
        "from": FROM,
        "to": to_email,
        "subject": "Reset your PanPanParts password",
        "html": f"""
        <div style="font-family:sans-serif;max-width:500px;margin:0 auto;padding:40px 20px">
            <h1 style="color:#ff6b35">PanPan<span style="color:#1a1a2e">Parts</span></h1>
            <h2>Password reset</h2>
            <p style="color:#666">Hi {name}, we received a request to reset your password.</p>
            <a href="{url}" style="display:inline-block;background:#ff6b35;color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;margin:24px 0">
                Reset password
            </a>
            <p style="color:#999;font-size:13px">Link expires in 1 hour. If you didn't request this, ignore this email.</p>
        </div>
        """
    })
