import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

def send_email_alert(subject, message):
    email = EmailMessage()
    email["From"] = EMAIL_ADDRESS
    email["To"] = EMAIL_TO
    email["Subject"] = subject
    email.set_content(message)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email)

def send_alerts(alerts):
    if not alerts:
        print("No alerts to send.")
        return
    subject = "Ad Pipeline Monitoring Alert"
    message = "\n".join(alerts)
    send_email_alert(subject, message)
    print("Alerts sent via email.")

