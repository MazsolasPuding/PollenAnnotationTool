# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_account.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Create_account(object):
    def setupUi(self, Create_account):
        if not Create_account.objectName():
            Create_account.setObjectName(u"Create_account")
        Create_account.setEnabled(True)
        Create_account.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Create_account.sizePolicy().hasHeightForWidth())
        Create_account.setSizePolicy(sizePolicy)
        Create_account.setStyleSheet(u"QDialog#Create_account{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.329545 rgba(106, 169, 200, 255), stop:1 rgba(205, 238, 255, 255));\n"
"}")
        Create_account.setSizeGripEnabled(False)
        self.label = QLabel(Create_account)
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
        self.label_2 = QLabel(Create_account)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 170, 431, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 24pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.createButton = QPushButton(Create_account)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(460, 700, 280, 50))
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)
        self.createButton.setMinimumSize(QSize(280, 50))
        self.createButton.setAcceptDrops(False)
        self.createButton.setAutoFillBackground(False)
        self.createButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")
        self.usernameEdit = QLineEdit(Create_account)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setGeometry(QRect(450, 270, 300, 40))
        self.usernameEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_3 = QLabel(Create_account)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 240, 161, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_4 = QLabel(Create_account)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 340, 161, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.passwordEdit = QLineEdit(Create_account)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(450, 370, 300, 40))
        self.passwordEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.errorLabel = QLabel(Create_account)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setEnabled(True)
        self.errorLabel.setGeometry(QRect(450, 630, 301, 21))
        self.errorLabel.setAcceptDrops(False)
        self.errorLabel.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(200, 0, 0);")
        self.backButton = QPushButton(Create_account)
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
        self.passwordEdit_2 = QLineEdit(Create_account)
        self.passwordEdit_2.setObjectName(u"passwordEdit_2")
        self.passwordEdit_2.setGeometry(QRect(450, 470, 300, 40))
        self.passwordEdit_2.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_5 = QLabel(Create_account)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 440, 161, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.label_6 = QLabel(Create_account)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 540, 161, 21))
        self.label_6.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")
        self.comboBox = QComboBox(Create_account)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(450, 570, 300, 40))
        self.comboBox.setEditable(False)

        self.retranslateUi(Create_account)

        QMetaObject.connectSlotsByName(Create_account)
    # setupUi

    def retranslateUi(self, Create_account):
        Create_account.setWindowTitle(QCoreApplication.translate("Create_account", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Create_account", u"Sign up", None))
        self.label_2.setText(QCoreApplication.translate("Create_account", u"Register a new account", None))
        self.createButton.setText(QCoreApplication.translate("Create_account", u"Create accont", None))
        self.label_3.setText(QCoreApplication.translate("Create_account", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("Create_account", u"Password:", None))
        self.errorLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("Create_account", u"Back", None))
        self.label_5.setText(QCoreApplication.translate("Create_account", u"Confirm password:", None))
        self.label_6.setText(QCoreApplication.translate("Create_account", u"Experince Level:", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Create_account", u"Medior", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Create_account", u"Senior", None))

        self.comboBox.setCurrentText("")
    # retranslateUi

