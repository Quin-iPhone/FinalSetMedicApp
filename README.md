# Set Medic App

Set Medic App is a Flask-based web application designed to provide professional and reliable medical services to film and television productions in South Africa.

---

## 🏥 Company Overview

**Company Name**: Set Medic South Africa  
**Mission**: To ensure the safety and well-being of all cast and crew members through expert medical support.

---

## 🚑 Services Offered

- On-Set Medical Support
- Health and Safety Training
- Medical Equipment Supply
- Consultation Services

---

## 🌐 Website

www.setmedicsa.com

---

## ⚙️ Environment Setup

### Prerequisites

- Python 3.9+
- pip
- PostgreSQL (for production)
- SQLite (for local development)

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/SetMedicApp.git
   cd SetMedicApp

2. Install dependencies
2. pip install -r requirements.txt

3. Set environment variables
Create a .env file in the root directory with the following content:
3. SECRET_KEY=your_secret_key
FLASK_ENV=production
DATABASE_URL=postgresql://your_user:your_password@your_host/your_db

⸻
🗃️ Database Setup with Flask-Migrate
1. Initialize migrations
1. flask db init

2. Generate migration script
2. flask db migrate -m "Initial migration"

3. Apply migrations
3. flask db upgrade

⸻
🚀 Deployment on Render.com
1. Create a new Web Service on Render.com.
2. Connect your GitHub repo and select the branch.
3. Set environment variables in the Render dashboard:
    • FLASK_ENV=production
    • SECRET_KEY=your_secret_key
    • DATABASE_URL=your_postgresql_url
4. Build Command:
4. pip install -r requirements.txt

5. Start Command:
5. gunicorn app:app

⸻
🧪 Running the App Locally
flask run --host=0.0.0.0 --port=5000

Visit http://localhost:5000 in your browser.
⸻
📞 Contact
• Phone: +27 066 220 8586
• Email: info@setmedicsa.com
• Location: City of Tshwane, Gauteng, South Africa
⸻
✅ License
This project is licensed for internal use by Set Medic South Africa.
