from google.oauth2.credentials import credentials
from google_auth.oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapi.com/auth/gmail.send']

def get_credentials():
    creds = None
    flow = InstalledAppFlow.from_client_secret_files('credential.json', SCOPES)
    creds = flow.run_local_server(port = 0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json)
    

if __name__ == '__main__':
    get_credentials()
