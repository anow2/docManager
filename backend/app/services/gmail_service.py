from googleapiclient.discovery import build
import base64
from .. import oauth

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