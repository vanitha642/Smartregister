# app.py
from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)
# Set a secret key for session management (required even if not explicitly used for Flask-Login, etc.)
# It's good practice for Flask apps. For a real app, use a strong, environment variable.
# For production, consider using a secret key from environment variables:
# app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))
app.secret_key = os.urandom(24) # Generates a random secret key for development

@app.route('/')
def index():
    """
    Renders the main index.html template for the Smart Register application.
    The client-side JavaScript will handle authentication redirection if not logged in.
    """
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_page():
    """
    Renders the dedicated login.html template.
    """
    return render_template('login.html')

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    app.run(debug=True)
