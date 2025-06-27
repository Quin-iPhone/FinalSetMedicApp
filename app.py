from flask import request, flash

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')

    if not name or not email or not service:
        flash('All fields are required.', 'error')
        return redirect(url_for('quote'))

    # Simulate saving or processing the quote
    flash(f'Thank you {name}, your quote request for "{service}" has been received!', 'success')
    return redirect(url_for('quote'))
