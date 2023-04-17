# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setEnabled(True)
        Login.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setStyleSheet(u"QDialog#Login{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.329545 rgba(106, 169, 200, 255), stop:1 rgba(205, 238, 255, 255));\n"
"}")
        Login.setSizeGripEnabled(False)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(480, 60, 248, 79))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 48pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 170, 431, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 24pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.loginButton = QPushButton(Login)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(470, 580, 280, 50))
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QSize(280, 50))
        self.loginButton.setAcceptDrops(False)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")
        self.usernameEdit = QLineEdit(Login)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setGeometry(QRect(460, 320, 300, 50))
        self.usernameEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 290, 161, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 410, 161, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.passwordEdit = QLineEdit(Login)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(460, 440, 300, 50))
        self.passwordEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.errorLabel = QLabel(Login)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setEnabled(True)
        self.errorLabel.setGeometry(QRect(460, 500, 301, 21))
        self.errorLabel.setAcceptDrops(False)
        self.errorLabel.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(200, 0, 0);")
        self.backButton = QPushButton(Login)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(20, 740, 100, 50))
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QSize(100, 50))
        self.backButton.setAcceptDrops(False)
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Sign in to your existing account", None))
        self.loginButton.setText(QCoreApplication.translate("Login", u"Log in", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.errorLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("Login", u"Back", None))
    # retranslateUi

