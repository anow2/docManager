from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from .. import oauth

from .document_classifier import classify_document
from .document_processing import extract_text_from_pdf



def fetch_emails():
    # Build the Gmail API service
    credentials = oauth.google.get_credentials()
    service = build('gmail', 'v1', credentials=credentials)
    
    # List the first 10 emails
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])
    
    return messages

def download_attachments(message_id):
    # Build the Gmail API service
    credentials = oauth.google.get_credentials()
    service = build('gmail', 'v1', credentials=credentials)
    
    # Get the specific email by ID
    message = service.users().messages().get(userId='me', id=message_id).execute()
    
    # Check for attachments
    for part in message['payload']['parts']:
        if 'filename' in part and part['filename']:
            attachment = service.users().messages().attachments().get(userId='me', messageId=message_id, id=part['body']['attachmentId']).execute()
            file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
            
            # Save the file (you can specify a path or use the filename from the email)
            with open(part['filename'], 'wb') as f:
                f.write(file_data)

def fetch_recent_emails(max_results=10):
    """Fetch the most recent emails."""
    try:
        # Build the Gmail API service
        credentials = oauth.google.get_credentials()
        service = build('gmail', 'v1', credentials=credentials)
        
        # List the most recent emails
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])
        
        # Fetch details for each message
        emails = []
        for message in messages:
            email_data = service.users().messages().get(userId='me', id=message['id']).execute()
            emails.append(email_data)
        
        return emails

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def fetch_recent_emails_with_details(max_results=10):
    """Fetch the most recent emails along with their details."""
    try:
        # Build the Gmail API service
        credentials = oauth.google.get_credentials()
        service = build('gmail', 'v1', credentials=credentials)
        
        # List the most recent emails
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])
        
        # Fetch details for each message
        emails = []
        for message in messages:
            email_data = service.users().messages().get(userId='me', id=message['id']).execute()
            
            # Extract the subject, body, and sender
            subject = [header['value'] for header in email_data['payload']['headers'] if header['name'] == 'Subject'][0]
            sender = [header['value'] for header in email_data['payload']['headers'] if header['name'] == 'From'][0]
            body = base64.urlsafe_b64decode(email_data['payload']['body']['data']).decode('utf-8') if 'data' in email_data['payload']['body'] else ""
            
            # Append the extracted details to the emails list
            emails.append({
                'id': message['id'],
                'subject': subject,
                'sender': sender,
                'body': body
            })
        
        return emails

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
