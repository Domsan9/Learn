import urllib.request
import time
import smtplib
from email.mime.text import MIMEText
import os

urls = [
    "https://www.swisscom.ch",
    "https://www.google.com",
    "https://www.github.com",
    "https://www.dieseseitegibtesnicht123456.ch",
]

def send_email(subject, body):
    sender = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_PASSWORD"]
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = sender

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    print("E-Mail gesendet")

print("=" * 40)
print("URL Monitor")
print("=" * 40)

fehler = []

for url in urls:
    try:
        start = time.time()
        urllib.request.urlopen(url, timeout=5)
        duration = round((time.time() - start) * 1000)
        print(f"OK      {duration}ms   {url}")
    except Exception as e:
        print(f"FEHLER  -        {url}")
        fehler.append(url)

print("=" * 40)

if fehler:
    body = "Folgende URLs sind nicht erreichbar:\n\n"
    for url in fehler:
        body += f"- {url}\n"
    send_email("URL Monitor: Fehler gefunden", body)
else:
    print("Alle URLs erreichbar - keine E-Mail nötig")