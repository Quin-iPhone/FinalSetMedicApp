
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample blog posts data
blog_posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the first post.'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the second post.'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if not post:
        return redirect(url_for('blog'))
    return render_template('blog_detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
