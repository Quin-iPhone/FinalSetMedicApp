from flask import Flask
from flask_migrate import Migrate
from models import db
import os

def create_app():
    app = Flask(__name__)

    # Configuration for Render.com or local development
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///setmedicapp.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('SECRET_KEY', 'default_key')

    db.init_app(app)
    Migrate(app, db)

    return app

# For command-line usage with Flask CLI
app = create_app()
