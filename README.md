# URL Monitor mit GitHub Actions

Ein einfaches Monitoring-Tool das automatisch prüft ob Websites erreichbar sind — und bei einem Fehler eine E-Mail schickt.

Gebaut als Lernprojekt um CI/CD Pipelines und Automatisierung zu verstehen.

---

## Was macht dieses Projekt?

- Prüft eine Liste von URLs ob sie erreichbar sind
- Misst wie lange jede URL zum Antworten braucht
- Schickt automatisch eine E-Mail wenn eine URL nicht erreichbar ist
- Läuft automatisch bei jedem Push und zusätzlich jede Stunde

---

## Wie funktioniert es?

```
Du pushst Code auf GitHub
        ↓
GitHub Actions startet automatisch
        ↓
Ein Ubuntu-Server wird gestartet
        ↓
Python wird installiert
        ↓
Das Skript prüft alle URLs
        ↓
Fehler? → E-Mail wird geschickt
Alles ok? → Fertig
```

---

## Projektstruktur

```
Learn/
├── .github/
│   └── workflows/
│       └── pipeline.yml   ← Die Pipeline (was GitHub automatisch ausführt)
├── scripts/
│   └── check_urls.py      ← Das Monitoring-Skript
└── README.md              ← Diese Datei
```

---

## Technologien

| Tool | Wofür |
|---|---|
| Python | Das Skript das die URLs prüft |
| GitHub Actions | Führt das Skript automatisch aus |
| Gmail SMTP | Schickt E-Mails bei Fehlern |
| Git | Versionskontrolle des Codes |

---

## Setup — so richtest du es selbst ein

**1. Repository klonen**
```
git clone git@github.com:DEINUSERNAME/Learn.git
cd Learn
```

**2. Gmail App-Passwort erstellen**
- Geh auf myaccount.google.com
- Sicherheit → 2-Schritt-Verifizierung aktivieren
- App-Passwörter → neues Passwort erstellen

**3. Secrets in GitHub hinterlegen**
- Repository → Settings → Secrets and variables → Actions
- `GMAIL_USER` = deine Gmail-Adresse
- `GMAIL_PASSWORD` = dein App-Passwort

**4. URLs anpassen**

Öffne `scripts/check_urls.py` und passe die Liste an:
```python
urls = [
    "https://www.deine-website.ch",
    "https://www.google.com",
]
```

**5. Pushen und fertig**
```
git add .
git commit -m "Meine URLs hinzugefügt"
git push
```

GitHub startet die Pipeline automatisch.

---

## Was ich dabei gelernt habe

- Wie GitHub Actions und CI/CD Pipelines funktionieren
- Wie man Secrets sicher in GitHub speichert
- Wie man Python für Automatisierung einsetzt
- Wie SMTP für automatische E-Mails funktioniert
- Grundlagen von Git und Versionskontrolle

---
