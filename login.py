from PySide6.QtWidgets import QApplication, QDialog, QWidget, QLineEdit
import sqlite3

from ui_login import Ui_Login
from main_senior import MainSenior


class Login(QDialog, Ui_Login):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.loginButton.clicked.connect(self.login_user)
        self.backButton.clicked.connect(self.go_back)

    def login_user(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        if not username or not password:
            self.errorLabel.setText("Please fill out all the fields!")
            return
        self.errorLabel.setText("")

        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        query = f'SELECT password FROM login_info WHERE username =\'{username}\''
        cursor.execute(query)
        try:
            fetched_password = cursor.fetchone()[0]
            if fetched_password != password:
                self.errorLabel.setText("Invalid password")
                return
            print("Successfully logged in.")
            connection.close()
        except TypeError:
            self.errorLabel.setText("Username not found, please create an account.")
            return
        self.widget.hide()
        self.main = MainSenior()
        self.main.show()

    def go_back(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))
