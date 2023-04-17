# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Welcome.sizePolicy().hasHeightForWidth())
        Welcome.setSizePolicy(sizePolicy)
        Welcome.setStyleSheet(u"QDialog#Welcome{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.329545 rgba(106, 169, 200, 255), stop:1 rgba(205, 238, 255, 255));\n"
"}")
        Welcome.setSizeGripEnabled(False)
        self.label = QLabel(Welcome)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(470, 170, 248, 79))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 48pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Welcome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 280, 409, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 24pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.createButton = QPushButton(Welcome)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(450, 510, 280, 50))
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)
        self.createButton.setMinimumSize(QSize(280, 50))
        self.createButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);")
        self.createButton.setAutoDefault(False)
        self.loginButton = QPushButton(Welcome)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(450, 440, 280, 50))
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QSize(280, 50))
        self.loginButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);")
        self.loginButton.setAutoDefault(False)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Welcome", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("Welcome", u"Sign in or create a new account", None))
        self.createButton.setText(QCoreApplication.translate("Welcome", u"Create a new account", None))
        self.loginButton.setText(QCoreApplication.translate("Welcome", u"Log In", None))
    # retranslateUi

