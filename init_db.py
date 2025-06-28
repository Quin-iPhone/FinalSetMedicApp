from app import app
from models import db

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
except Exception as e:
    print(f"Error creating tables: {e}")
