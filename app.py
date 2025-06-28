from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import string

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure key in production

# Dummy data for services
services = [
    {'id': 1, 'name': 'On-set Medical Support', 'description': 'Comprehensive on-set medical support for film productions.', 'price': 500},
    {'id': 2, 'name': 'Event First Aid Kit', 'description': 'Complete first aid kit services for events.', 'price': 300},
    {'id': 3, 'name': 'Post-Production Health Check', 'description': 'Health check services post event or filming.', 'price': 400},
]

# Dummy blog posts data
blog_posts = [
    {'id': 1, 'title': 'The Importance of On-set Medical Support', 'snippet': 'A look into why on-set support is crucial...', 'content': 'Full article content for on-set medical support blog post.', 'date': '2025-06-01'},
    {'id': 2, 'title': 'Innovative First Aid Solutions for Events', 'snippet': 'Exploring modern approaches to first aid kits...', 'content': 'Full article content for innovative first aid solutions blog post.', 'date': '2025-06-15'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        # Process quote request form
        name = request.form.get('name')
        company = request.form.get('company')
        email = request.form.get('email')
        contact = request.form.get('contact')
