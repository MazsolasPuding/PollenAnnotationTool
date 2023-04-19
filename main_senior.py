from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow

from Resources.ui_main_senior import Ui_senior_MainWindow

class MainSenior(QMainWindow, Ui_senior_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
