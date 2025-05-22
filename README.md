
# Django Fitness Studio CRM

Dies ist ein Mini-CRM-System für eine Fitnessstudio-Website, entwickelt im Rahmen meiner Umschulung zum Fachinformatiker für Anwendungsentwicklung.  
Das Projekt wurde mit Django umgesetzt und enthält Benutzer-Authentifizierung, Rollenverwaltung (Mitarbeiter und Mitglieder) sowie ein REST API.

## Features

- Benutzerregistrierung und -authentifizierung
- Rollenbasierter Zugriff: Mitglieder / Mitarbeiter
- CRUD-Funktionalität für Mitglieder und Mitarbeiter
- REST API mit Django REST Framework
- Adminbereich
- Responsive Benutzeroberfläche (HTML, CSS, JavaScript)

## Installation

```bash
git clone https://github.com/dein-benutzername/django-fitness-crm.git
cd django-fitness-crm
python -m venv venv
source venv/bin/activate  # auf Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## API-Endpunkte

- `/api/members/` – Liste der Mitglieder
- `/api/employees/` – Liste der Mitarbeiter
- Authentifizierung über Token oder Session möglich

## Verwendete Technologien

- Python
- Django
- Django REST Framework
- SQLite (standardmäßig)
- HTML/CSS/JavaScript

