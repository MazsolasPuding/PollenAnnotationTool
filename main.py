"""
Main Pytho file for running the Annotation Tool.
"""

import sys
import base64
import logging

from PySide6.QtWidgets import QApplication, QDialog, QStackedWidget, QLineEdit
from PySide6.QtCore import qInstallMessageHandler

from Resources.ui_welcome import Ui_Welcome
from Resources.ui_login import Ui_Login
from Resources.ui_create_account import Ui_Create_account
from Libs.main_window import MainWindow
from Libs.connect_to_db import Connection


class Welcome(QDialog, Ui_Welcome):
    def __init__(self, widget, app):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.app = app

        self.loginButton.clicked.connect(self.goto_login)
        self.createButton.clicked.connect(self.goto_create)
        qInstallMessageHandler(self.customMessageHandler)

    def goto_login(self):
        login = Login(self.widget, self.app)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def goto_create(self):
        create = CreateAccount(self.widget)
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def customMessageHandler(self, type_, context, message):
        if "QSvgHandler: Image filename is empty" in message:
            return


class CreateAccount(QDialog, Ui_Create_account):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit_2.setEchoMode(QLineEdit.Password)
        self.createButton.clicked.connect(self.create_account)
        self.backButton.clicked.connect(self.go_back)

    def create_account(self):
        username = self.usernameEdit.text().lower()
        password = self.passwordEdit.text()
        password_2 = self.passwordEdit_2.text()
        experience = self.comboBox.currentText()

        if not username or not password or not password_2 or not experience:
            self.errorLabel.setText("Please fill out all the fields!")
            return
        if password != password_2:
            self.errorLabel.setText("Passwords does not match!")
            return
        senior = True if experience == "Senior" else False
        self.errorLabel.setText("")

        try:
            connection = Connection().connect
            cursor = connection.cursor()
            encoded = base64.b64encode(password.encode("utf-8"))
            user_info = [username, str(encoded), senior]
            query = """INSERT INTO users (username, password, senior)
                    VALUES (%s,%s,%s)"""
            cursor.execute(query, user_info)
        except:
            self.errorLabel.setText("Username already in use.")
            return
        connection.commit()
        connection.close()
        logging.info(f"Account successfully Created: {username}")
        self.goto_login()

    def go_back(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))

    def goto_login(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class Login(QDialog, Ui_Login):
    def __init__(self, widget, app):
        super().__init__()
        self.setupUi(self)
        self.widget = widget
        self.app = app

        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.loginButton.clicked.connect(self.login_user)
        self.backButton.clicked.connect(self.go_back)

    def login_user(self):
        username = self.usernameEdit.text().lower()
        password = self.passwordEdit.text()

        if not username or not password:
            self.errorLabel.setText("Please fill out all the fields!")
            return
        self.errorLabel.setText("")

        connection = Connection().connect
        cursor = connection.cursor()
        query = f"""
                SELECT password, senior FROM users
                WHERE username = '{username}'
                """
        cursor.execute(query)
        try:
            fetched = cursor.fetchall()
            fetched_password = fetched[0][0]
            fetched_is_senior = fetched[0][1]
            if fetched_password != str(base64.b64encode(password.encode("utf-8"))):
                self.errorLabel.setText("Invalid password\nIf you forgot your username or password please contact your administrator.")
                return
            logging.info(f"Successfully logged in: {username}")
            connection.close()
        except IndexError:
            self.errorLabel.setText("Username not found, please create an account.\nIf you forgot your username or password please\ncontact your administrator.")
            return
        self.widget.close()
        self.main = MainWindow(self.app, username, fetched_is_senior)
        self.main.show()

    def go_back(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="./Data/usage.log"
    )

    logging.warning("App Launched!")
    app = QApplication(sys.argv)

    widget = QStackedWidget()
    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)

    welcome = Welcome(widget, app)
    widget.addWidget(welcome)

    def restart():
        widget.removeWidget(widget.widget(widget.currentIndex()))
        widget.show()

    app.aboutToQuit.connect(restart)
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
