from PySide6.QtWidgets import QApplication, QDialog, QWidget


from ui_welcome import Ui_Welcome
from login import Login
from create_account import CreateAccount

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