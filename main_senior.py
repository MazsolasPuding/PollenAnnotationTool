from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow

from Resources.ui_main_senior import Ui_Main_senior

class MainSenior(QMainWindow, Ui_Main_senior):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
