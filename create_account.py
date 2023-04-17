from PySide6.QtWidgets import QApplication, QDialog, QWidget, QLineEdit
import sqlite3

from ui_create_account import Ui_Create_account
from login import Login

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
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        password_2 = self.passwordEdit_2.text()
        experience = self.comboBox.currentText()

        if not username or not password or not password_2 or not experience:
            self.errorLabel.setText("Please fill out all the fields!")
            return
        if password != password_2:
            self.errorLabel.setText("Passwords does not match!")
            return
        if experience == "Medior":
            senior = 0
        else:
            senior = 1

        self.errorLabel.setText("")

        try:
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            user_info = [username, password, senior]
            query = 'INSERT INTO login_info (username, password, senior) VALUES (?,?,?)'
            cursor.execute(query, user_info)
        except sqlite3.IntegrityError:
            self.errorLabel.setText("Username already in use.")
            return
        connection.commit()
        connection.close()
        self.goto_login()


    def go_back(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))

    def goto_login(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)