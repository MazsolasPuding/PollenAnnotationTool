from __future__ import print_function


import io
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from PySide6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout, QFileSystemModel
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from PySide6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout
# from PySide6.QtCore import QFileSystemModel


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

    def download_db(self):
        try:
            self.service = build('drive', 'v3', credentials=self.creds)
            query = "name='pollen.db'"
            results = self.service.files().list(q=query, fields='nextPageToken, files(id, name)').execute()
            items = results.get('files', [])
            if not items:
                print('No files found.')
            else:
                for item in items:
                    print(f"Found file: {item['name']}, ID: {item['id']}")
                    self.file_id = item['id']

            request = self.service.files().get_media(fileId=self.file_id)
            with open('./Data/pollen.db', 'wb') as f:
                f.write(request.execute())
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')
    
    def update_db(self):
        file_metadata = {'name': 'pollen.db'}
        media = MediaFileUpload('pollen.db', mimetype='application/x-sqlite3')
        file = self.service.files().update(fileId=self.file_id, body=file_metadata, media_body=media).execute()
        print(f"File ID: {file.get('id')}")

    def try_db(self):
        conn = sqlite3.connect('./Data/pollen.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM annotation')
        rows = cursor.fetchone()
        for row in rows:
            print(row)
        conn.close()
    
    
    def get_directory_tree(self):
        pass


    def google_directory(self):
        # Create a Drive API client object
        drive_service = build('drive', 'v3', credentials=self.creds)

        # Function to recursively fetch directories
        def fetch_directories(parent_id='root'):
            results = []
            query = f"'{parent_id}' in parents and trashed=false"
            response = drive_service.files().list(q=query, fields="files(id, name, mimeType)", pageSize=1000).execute()
            results.extend(response.get('files', []))

            for item in results:
                if item['mimeType'] == 'application/vnd.google-apps.folder':
                    item['children'] = fetch_directories(item['id'])

            return results

        # Function to populate the tree view
        def populate_tree_view(parent, items):
            for item in items:
                if item['mimeType'] == 'application/vnd.google-apps.folder':
                    directory_name = item['name']
                    directory_id = item['id']
                    directory_path = model.filePath(parent) + '/' + directory_name

                    model.mkdir(parent, directory_name)
                    index = model.index(directory_path)
                    model.setData(index, directory_id, QFileSystemModel.FilePathRole)

                    if 'children' in item:
                        populate_tree_view(index, item['children'])

        # Create a Qt application object
        app = QApplication([])

        # Create a QWidget as the main window
        window = QWidget()

        # Create a QTreeView to display the directory structure
        tree_view = QTreeView()

        # Create a QFileSystemModel to populate the tree view
        model = QFileSystemModel()
        root_path = "/"
        model.setRootPath(root_path)
        tree_view.setModel(model)

        # Fetch directories from Google Drive
        directories = fetch_directories()
        pprint(directories)

        # Populate the tree view with directories
        root_index = model.index(root_path)
        populate_tree_view(root_index, directories)

        # Set the root index of the model
        tree_view.setRootIndex(root_index)

        # Show the directory structure in the tree view
        tree_view.show()

        # Create a QVBoxLayout and add the tree view to it
        layout = QVBoxLayout()
        layout.addWidget(tree_view)

        # Set the QVBoxLayout as the layout of the main window
        window.setLayout(layout)

        # Show the main window
        window.show()

        # Start the Qt event loop
        app.exec()



if __name__ == '__main__':
    d = Drive()
    # d.download_db()
    # d.try_db()
    # d.update_db()
    d.google_directory()