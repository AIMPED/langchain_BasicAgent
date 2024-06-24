import os
import base64
import pickle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pathlib import PurePath

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

# get paths of files. Not sure if that is a good way to do it
base_path = PurePath(__file__).parent.parent.joinpath('auth/')
token_path = base_path.joinpath('token.pickle')
json_path = base_path.joinpath('cs.json')


def load_credentials():
    creds = None
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file=json_path,
                scopes=['https://www.googleapis.com/auth/gmail.send']
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return creds


# this class is needed for langchain. It basically describes each parameter of the actual function
class SendGmail(BaseModel):
    to: str = Field(description="the recipients email address")
    subject: str = Field(description="the subject of the email")
    body: str = Field(description="the email text")


@tool("SendMail", args_schema=SendGmail)
def send_gmail(to: str, subject: str, body: str) -> str:
    """
    use this function if you have to send an email
    """
    creds = load_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Create the email
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)

    # Encode the message
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the message
    try:
        message = (service.users().messages().send(userId="me", body={'raw': raw})
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(f'An error occurred: {error}')
        return ""
