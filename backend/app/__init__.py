from flask import Flask
from flask_oauthlib.client import OAuth
import os

# Initialize Flask app and OAuth
app = Flask(__name__)
app.config.from_pyfile('../config.py')
oauth = OAuth(app)

# Import routes after initializing the app
google = oauth.remote_app(
    'google',
    consumer_key=app.config['GOOGLE_CLIENT_ID'],
    consumer_secret=app.config['GOOGLE_CLIENT_SECRET'],
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/gmail.readonly'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

from .routes import main, gmail  # Import routes after initializing the app and OAuth