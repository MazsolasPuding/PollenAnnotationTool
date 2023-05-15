import psycopg2


connection = psycopg2.connect(database ="bql3duq2x8p5l7r5ahz0",
                              host="bql3duq2x8p5l7r5ahz0-postgresql.services.clever-cloud.com",
                              user="ucsuarf2fko8ds4k3443",
                              password="W2JF95zE1czTx9ngxrZyX2nHxi3Drm",
                              port="5432")

sql = """
DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE "users" (
	"username"	VARCHAR(255) NOT NULL,
	"password"	VARCHAR(255) NOT NULL,
	"senior"	BOOLEAN NOT NULL,
	PRIMARY KEY("username")
);

DROP TABLE IF EXISTS annotation CASCADE;
CREATE TABLE "annotation" (
	"annotation_id"	BIGSERIAL NOT NULL,
	"path"	TEXT NOT NULL,
	"class"	VARCHAR(255) NOT NULL,
	"confidence"	INTEGER NOT NULL,
	"comment"	TEXT,
	"user"	VARCHAR(255) NOT NULL,
	"senior"	BOOLEAN NOT NULL,
	"timestamp"	TIMESTAMP NOT NULL,
	PRIMARY KEY("annotation_id"),
	FOREIGN KEY("user") REFERENCES "users"("username")
);

DROP TABLE IF EXISTS review CASCADE;
CREATE TABLE "review" (
	"review_id"	BIGSERIAL NOT NULL,
	"annotation_id"	INTEGER NOT NULL,
	"reviewer"	VARCHAR(255) NOT NULL,
	"review_score"	INTEGER NOT NULL,
	"review_comment"	TEXT,
	"new_class"	VARCHAR(255) NOT NULL,
	"new_confidence"	INTEGER NOT NULL,
	"new_comment"	TEXT,
	"timestamp"	TIMESTAMP NOT NULL,
	PRIMARY KEY("review_id"),
	FOREIGN KEY("annotation_id") REFERENCES "annotation"("annotation_id"),
	FOREIGN KEY("reviewer") REFERENCES "users"("username")
);
"""

print(connection)
cursor = connection.cursor()
cursor.execute(sql)
# data = cursor.fetchall()
connection.commit()
connection.close()


# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build
# from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem
# from pprint import pprint

# # Create a Drive API client object
# SCOPES = ['https://www.googleapis.com/auth/drive']
# creds = Credentials.from_authorized_user_file('./Data/token.json', SCOPES)
# drive_service = build('drive', 'v3', credentials=creds)

# # Retrieve a list of folders in the user's Google Drive account
# results = drive_service.files().list(
#     q="mimeType='application/vnd.google-apps.folder'",
#     fields="nextPageToken, files(id, name)"
# ).execute()

# # Create a Qt application object
# app = QApplication([])

# # Create a QListWidget to display the list of folders
# list_widget = QListWidget()

# pprint(results)
# print(len(results.get('files', [])))
# # Add each folder to the QListWidget
# for item in results.get('files', []):
#     # Create a QListWidgetItem for the folder
#     list_item = QListWidgetItem(item['name'], list_widget)
#     # Set the item's data to the folder's ID
#     list_item.setData(64, item['id'])

# # Show the QListWidget
# list_widget.show()

# # Start the Qt event loop
# app.exec()
