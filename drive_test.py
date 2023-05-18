import io
import os.path
import sqlite3
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

class Drive():
    def __init__(self):
            self.creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('./Data/token.json'):
                self.creds = Credentials.from_authorized_user_file('./Data/token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        './Data/credentials.json', SCOPES)
                    self.creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('./Data/token.json', 'w') as token:
                    token.write(self.creds.to_json())



# Create a Drive API client object
drive_service = build('drive', 'v3', credentials=Drive().creds)

from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout


class DriveTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderLabels(['Name'])
        self.root_item = self.invisibleRootItem()

    def fetch_directory_tree(self, parent_item, parent_id='root'):
        query = f"'{parent_id}' in parents and trashed=false"
        response = drive_service.files().list(q=query, fields="files(id, name, mimeType)", pageSize=1000).execute()
        items = response.get('files', [])
        for item in items:
            item_id = item['id']
            item_name = item['name']
            if item_name == 'Data' and item['mimeType'] == 'application/vnd.google-apps.folder':
                self.fetch_subdirectories(parent_item, item_id)
                break

    def fetch_subdirectories(self, parent_item, parent_id):
        query = f"'{parent_id}' in parents and trashed=false"
        response = drive_service.files().list(q=query, fields="files(id, name, mimeType)", pageSize=1000).execute()
        items = response.get('files', [])
        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                item_id = item['id']
                item_name = item['name']
                child_item = QTreeWidgetItem(parent_item, [item_name])
                self.fetch_subdirectories(child_item, item_id)


# Create a Qt application object
app = QApplication([])

# Create a QWidget as the main window
window = QWidget()

# Create a QTreeWidget to display the directory structure
tree_widget = DriveTreeWidget()

# Fetch the Google Drive directory tree and populate the tree widget
tree_widget.fetch_directory_tree(tree_widget.root_item)

# Create a QVBoxLayout and add the tree widget to it
layout = QVBoxLayout()
layout.addWidget(tree_widget)

# Set the QVBoxLayout as the layout of the main window
window.setLayout(layout)

# Show the main window
window.show()

# Start the Qt event loop
app.exec()
