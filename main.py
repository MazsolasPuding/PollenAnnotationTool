from PySide6.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget, QLineEdit
import sys
import sqlite3
from Resources.ui_welcome import Ui_Welcome
from Libs.main_senior import MainSenior
from Resources.ui_login import Ui_Login
from Resources.ui_create_account import Ui_Create_account

"""
Mac init.
"""



class Welcome(QDialog, Ui_Welcome):
    def __init__(self, widget):
        super().__init__()
        self.setupUi(self)
        self.widget = widget

        self.loginButton.clicked.connect(self.goto_login)
        self.createButton.clicked.connect(self.goto_create)

    def goto_login(self):
        login = Login(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def goto_create(self):
        create = CreateAccount(self.widget)
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


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
        query = f'SELECT password, senior FROM login_info WHERE username =\'{username}\''
        cursor.execute(query)
        try:
            fetched = cursor.fetchall()
            fetched_password = fetched[0][0]
            fetched_is_senior = fetched[0][1]
            if fetched_password != password:
                self.errorLabel.setText("Invalid password")
                return
            print("Successfully logged in.")
            connection.close()
        except TypeError:
            self.errorLabel.setText("Username not found, please create an account.")
            return
        self.widget.hide()
        self.main = MainSenior(app, username, fetched_is_senior )
        self.main.show()

    def go_back(self):
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()))


app = QApplication(sys.argv)

# widget = QStackedWidget()
# widget.setFixedWidth(1200)
# widget.setFixedHeight(800)

# welcome = Welcome(widget)
# widget.addWidget(welcome)

# widget.show()
window = MainSenior(app, "horvada", 1)
window.show()
app.exec()


