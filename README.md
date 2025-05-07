# ServiceTrack – Simple IT Ticket System

ServiceTrack is a basic ticketing app built with Python (Flask) and HTML. It lets you create, view, update, and delete support tickets using a web page or API.

## 🔧 Features
- Create tickets using a form
- View tickets in a table
- Edit or remove tickets from the UI
- Use API to access ticket data

## 📁 Folder Overview
```
service-track/
├── backend/
│   ├── app.py          # Main Flask app
│   ├── routes/         # Placeholder for route files
│   ├── templates/      # Web UI (HTML)
│   │   └── ticket_table.html
│   └── venv/           # Virtual environment
├── requirements.txt
├── README.md
```

## ▶️ How to Run

### 1. Open a terminal and clone the repo:
```bash
git clone https://github.com/your-username/service-track.git
cd service-track/backend
```

### 2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install packages:
```bash
pip install flask flask_sqlalchemy flask_cors
```

### 4. Start the app:
```bash
python app.py
```
Then open:
```
http://127.0.0.1:5000/tickets
```

## 📡 API Endpoints
- `GET /api/tickets` – Get all tickets
- `POST /api/tickets` – Create a ticket
- `PUT /api/tickets/<id>` – Update a ticket
- `DELETE /api/tickets/<id>` – Delete a ticket

## 🧰 Requirements
- Python 3.8+
- Flask (installed via pip)

---
Created to showcase software skills