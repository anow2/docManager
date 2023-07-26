from flask import redirect, url_for, session, jsonify, request
from .. import app, oauth
from ..services.gmail_service import fetch_emails, download_attachments

@app.route('/login')
def login():
    return oauth.google.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    response = oauth.google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (response['access_token'], '')
    return 'Logged in successfully!'

@app.route('/process-emails')
def process_and_download_emails():
    messages = fetch_emails()
    for message in messages:
        download_attachments(message['id'])
    return f"Processed and downloaded attachments from {len(messages)} emails."

@app.route('/list-emails', methods=['GET'])
def list_emails():
    emails = fetch_emails()
    if emails:
        return jsonify(emails), 200
    else:
        return jsonify({"error": "Failed to list emails"}), 500