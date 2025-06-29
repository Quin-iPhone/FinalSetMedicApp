from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import os
import stripe

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_key')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///setmedicapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from models import db, init_db
init_db(app)
db = SQLAlchemy(app)

# Dummy data
services = [
    {'id': 1, 'name': 'On-set Medical Support', 'description': 'Comprehensive on-set medical support for film productions.', 'price': 500},
    {'id': 2, 'name': 'Event First Aid Kit', 'description': 'Complete first aid kit services for events.', 'price': 300},
    {'id': 3, 'name': 'Post-Production Health Check', 'description': 'Health check services post event or filming.', 'price': 400},
]

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
        name = request.form.get('name')
        company = request.form.get('company')
        email = request.form.get('email')
        contact = request.form.get('contact')
        service_id = request.form.get('service')
        details = request.form.get('details')
        flash('Quote request submitted successfully!', 'success')
        return redirect(url_for('quote'))
    return render_template('quote.html', services=services)

@app.route('/invoice')
def invoice():
    invoice_data = {
        'id': 101,
        'date': '2025-06-28',
        'client_name': 'John Doe',
        'items': [
            {'description': 'On-set Medical Support', 'amount': 500},
            {'description': 'Event First Aid Kit', 'amount': 300}
        ],
        'total': 800
    }
    return render_template('invoice.html', invoice=invoice_data)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        flash('Payment processed successfully!', 'success')
        return redirect(url_for('payment'))
    return render_template('payment.html')

@app.route('/receipt')
def receipt():
    receipt_data = {
        'id': 202,
        'date': '2025-06-28',
        'client_name': 'John Doe',
        'amount': 800,
        'method': 'Credit Card'
    }
    return render_template('receipt.html', receipt=receipt_data)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if not post:
        flash('Blog post not found.', 'error')
        return redirect(url_for('blog'))
    return render_template('blog_detail.html', post=post)

# Stripe setup
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    invoice_data = session.get('invoice_data')
    if not invoice_data:
        return redirect(url_for('quote'))

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'zar',
                    'product_data': {
                        'name': invoice_data['service']['name'],
                    },
                    'unit_amount': int(invoice_data['total_amount'] * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('receipt', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('payment', _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
