from __future__ import print_function

import io
import os.path
import sqlite3
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from PySide6.QtWidgets import QTreeWidgetItem, QLabel
from PySide6.QtGui import QImage, QPixmap

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
        try:
            self.service = build('drive', 'v3', credentials=self.creds)
        except HttpError as error:
            # TODO(developer) - Handle errors from drive API.
            print(f'An error occurred: {error}')

    def download_db(self):
        try:
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
    
    def fetch_directory_tree(self, parent_item, parent_id='root', fetch_files=False):
        query = f"'{parent_id}' in parents and trashed=false"
        response = self.service.files().list(q=query, fields="files(id, name, mimeType)", pageSize=1000).execute()
        items = response.get('files', [])
        for item in items:
            item_id = item['id']
            item_name = item['name']
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                child_item = QTreeWidgetItem(parent_item, [item_name])
                if not fetch_files:
                    self.fetch_directory_tree(child_item, item_id, fetch_files)
            elif fetch_files:
                QTreeWidgetItem(parent_item, [item_name])

    def fetch_all_items(self, root_item, start_folder_id=None):
        if start_folder_id:
            self.fetch_directory_tree(root_item, start_folder_id)
        else:
            self.fetch_directory_tree(root_item)

    def fetch_image_names_from_folder(self, folder_name):
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        response = self.service.files().list(q=query, fields="files(id)", pageSize=1).execute()
        items = response.get('files', [])
        if items:
            folder_id = items[0]['id']
            query = f"'{folder_id}' in parents and mimeType contains 'image/' and trashed=false"
            response = self.service.files().list(q=query, fields="files(name)", pageSize=1000).execute()
            image_items = response.get('files', [])
            image_ids = [item['name'] for item in image_items]
            return image_ids
        else:
            return []
    
    def get_pixmap_from_drive(self, image_name):
        query = f"name='{image_name}' and mimeType contains 'image/' and trashed=false"
        try:
            response = self.service.files().list(q=query, fields="files(id)", pageSize=1).execute()
            items = response.get('files', [])
            if items:
                image_id = items[0]['id']
                request = self.service.files().get_media(fileId=image_id)
                file_stream = io.BytesIO()
                downloader = MediaIoBaseDownload(file_stream, request)
                done = False
                while not done:
                    _, done = downloader.next_chunk()
    
                image_data = file_stream.getvalue()
                image = QImage.fromData(image_data)
                if not image.isNull():
                    pixmap = QPixmap.fromImage(image)
                    return pixmap
        except Exception as e:
            print(f"Error fetching image from Google Drive: {str(e)}")
    
        return None



if __name__ == '__main__':
    d = Drive()
    # d.download_db()
    # d.try_db()
    # d.update_db()
    d.google_directory()