import sys
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Please log in:'))
        layout.addWidget(QPushButton('Log in'))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        layout = QVBoxLayout()
        layout.addWidget(QLabel('This is the main window.'))
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)
    
    def closeEvent(self, event):
        QApplication.instance().aboutToQuit.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    login_window = LoginWindow()

    # Connect the aboutToQuit signal to a function that shows the login window.
    app.aboutToQuit.connect(login_window.show)

    main_window.show()
    sys.exit(app.exec())
