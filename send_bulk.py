from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_credentials():
    """Get valid user credentials from storage."""
    creds = None
    # TODO: Load your credentials from the 'token.json' file if it exists.
    # If it doesn't exist or if the token is invalid, run the OAuth2 flow to obtain new credentials.
    return creds

def create_message(sender, to, subject, message_text):
    """Create a message for an email."""
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_message(service, user_id, message):
    """Send an email message."""
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f"Message Id: {message['id']}")
        return message
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    """Shows basic usage of the Gmail API."""
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API to send email
    sender = "your_email@gmail.com"
    to = "recipient_email@gmail.com"
    subject = "Your Subject Here"
    message_text = "Your Message Here"
    message = create_message(sender, to, subject, message_text)
    send_message(service, "me", message)

if __name__ == '__main__':
    main()
