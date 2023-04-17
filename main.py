import sys
from PySide6.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget
from welcome import Welcome
from main_senior import MainSenior


app = QApplication(sys.argv)


widget = QStackedWidget()
widget.setFixedWidth(1200)
widget.setFixedHeight(800)

welcome = Welcome(widget)
widget.addWidget(welcome)

widget.show()
app.exec()


