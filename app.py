from flask import request, flash

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
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
