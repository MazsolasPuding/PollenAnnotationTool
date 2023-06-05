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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

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
        icon = QIcon()
        icon.addFile(u":/Icons/pollen-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"QDialog#Login{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.329545 rgba(106, 169, 200, 255), stop:1 rgba(205, 238, 255, 255));\n"
"}")
        Login.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 48pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 24pt \"Corbel\"; color:rgb(79, 79, 79);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_3)

        self.usernameEdit = QLineEdit(Login)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setMinimumSize(QSize(0, 40))
        self.usernameEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.usernameEdit)

        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_4)

        self.passwordEdit = QLineEdit(Login)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setMinimumSize(QSize(0, 40))
        self.passwordEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.passwordEdit)

        self.errorLabel = QLabel(Login)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setEnabled(True)
        self.errorLabel.setAcceptDrops(False)
        self.errorLabel.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(200, 0, 0);")

        self.verticalLayout.addWidget(self.errorLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.loginButton = QPushButton(Login)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QSize(280, 50))
        self.loginButton.setAcceptDrops(False)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")

        self.horizontalLayout_4.addWidget(self.loginButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.backButton = QPushButton(Login)
        self.backButton.setObjectName(u"backButton")
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QSize(100, 50))
        self.backButton.setAcceptDrops(False)
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")

        self.verticalLayout_2.addWidget(self.backButton)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Pollen Annotation", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Sign in to your existing account", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.errorLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("Login", u"Log in", None))
        self.backButton.setText(QCoreApplication.translate("Login", u"Back", None))
    # retranslateUi

