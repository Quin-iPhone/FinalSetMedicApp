from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        flash('Quote submitted successfully!', 'success')
        return redirect(url_for('quote'))
    return render_template('quote.html')

if __name__ == '__main__':
    app.run(debug=True)

# Simulate saving or processing the quote
    flash(f'Thank you {name}, your quote request for "{service}" has been received!', 'success')
    return redirect(url_for('quote'))
