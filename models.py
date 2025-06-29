from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User model for authentication or admin access
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

# Service model for services.html
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)

# ServiceProvider model for managing providers
class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(120))
    phone = db.Column(db.String(50))
    services_offered = db.relationship('Service', secondary='provider_services', backref='providers')

provider_services = db.Table('provider_services',
    db.Column('provider_id', db.Integer, db.ForeignKey('service_provider.id')),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'))
)

# QuoteRequest model for quote.html and form_validation_smooth_scroll.html
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    company = db.Column(db.String(100))
    email = db.Column(db.String(120))
    contact = db.Column(db.String(50))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    details = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    service = db.relationship('Service')

# Invoice model for invoice.html
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float)

    items = db.relationship('InvoiceItem', backref='invoice', lazy=True)

# InvoiceItem model for invoice line items
class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float)

# Payment model for payment.html and receipt.html
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    amount = db.Column(db.Float)
    method = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    invoice = db.relationship('Invoice')

# BlogPost model for blog.html and blog_detail.html
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    snippet = db.Column(db.String(300))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Function to initialize the database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
