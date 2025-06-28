from app import app
from models import db

# Create all tables within the app context
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
