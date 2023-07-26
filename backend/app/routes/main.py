# backend/app/routes/main.py

from flask import redirect, url_for, session
from .. import app

@app.route('/')
def index():
    return 'Welcome to DocManager!'

@app.route('/logout')
def logout():
    session.pop('google_token')
    return redirect(url_for('index'))
