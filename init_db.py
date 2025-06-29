from app import app
from models import db
import logging

with app.app_context():
    db.create_all()
    logging.basicConfig(level=logging.INFO)
    logging.info("Database tables created successfully.")
  
