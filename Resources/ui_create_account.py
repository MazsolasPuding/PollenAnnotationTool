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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Create_account(object):
    def setupUi(self, Create_account):
        if not Create_account.objectName():
            Create_account.setObjectName(u"Create_account")
        Create_account.setEnabled(True)
        Create_account.resize(700, 583)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Create_account.sizePolicy().hasHeightForWidth())
        Create_account.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Icons/pollen-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Create_account.setWindowIcon(icon)
        Create_account.setStyleSheet(u"QDialog#Create_account{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.329545 rgba(106, 169, 200, 255), stop:1 rgba(205, 238, 255, 255));\n"
"}")
        Create_account.setSizeGripEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(Create_account)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Create_account)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 36pt \"Corbel\"; color:rgb(79, 79, 79);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(Create_account)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 22pt \"Corbel\"; color:rgb(79, 79, 79);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Create_account)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_3)

        self.usernameEdit = QLineEdit(Create_account)
        self.usernameEdit.setObjectName(u"usernameEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.usernameEdit.sizePolicy().hasHeightForWidth())
        self.usernameEdit.setSizePolicy(sizePolicy3)
        self.usernameEdit.setMinimumSize(QSize(0, 0))
        self.usernameEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.usernameEdit)

        self.label_4 = QLabel(Create_account)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_4)

        self.passwordEdit = QLineEdit(Create_account)
        self.passwordEdit.setObjectName(u"passwordEdit")
        sizePolicy3.setHeightForWidth(self.passwordEdit.sizePolicy().hasHeightForWidth())
        self.passwordEdit.setSizePolicy(sizePolicy3)
        self.passwordEdit.setMinimumSize(QSize(0, 0))
        self.passwordEdit.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.passwordEdit)

        self.label_5 = QLabel(Create_account)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_5)

        self.passwordEdit_2 = QLineEdit(Create_account)
        self.passwordEdit_2.setObjectName(u"passwordEdit_2")
        self.passwordEdit_2.setMinimumSize(QSize(0, 0))
        self.passwordEdit_2.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.passwordEdit_2)

        self.label_6 = QLabel(Create_account)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_6)

        self.comboBox = QComboBox(Create_account)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setEditable(False)

        self.verticalLayout.addWidget(self.comboBox)

        self.errorLabel = QLabel(Create_account)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setEnabled(True)
        self.errorLabel.setAcceptDrops(False)
        self.errorLabel.setStyleSheet(u"font: 12pt \"Corbel\"; color:rgb(200, 0, 0);")

        self.verticalLayout.addWidget(self.errorLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.createButton = QPushButton(Create_account)
        self.createButton.setObjectName(u"createButton")
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)
        self.createButton.setMinimumSize(QSize(280, 0))
        self.createButton.setAcceptDrops(False)
        self.createButton.setAutoFillBackground(False)
        self.createButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")

        self.horizontalLayout_4.addWidget(self.createButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.backButton = QPushButton(Create_account)
        self.backButton.setObjectName(u"backButton")
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QSize(100, 0))
        self.backButton.setAcceptDrops(False)
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet(u"font: 20pt \"Corbel\";\n"
"color:rgb(79, 79, 79);\n"
"")

        self.verticalLayout_2.addWidget(self.backButton)


        self.retranslateUi(Create_account)

        QMetaObject.connectSlotsByName(Create_account)
    # setupUi

    def retranslateUi(self, Create_account):
        Create_account.setWindowTitle(QCoreApplication.translate("Create_account", u"Pollen Annotation", None))
        self.label.setText(QCoreApplication.translate("Create_account", u"Sign up", None))
        self.label_2.setText(QCoreApplication.translate("Create_account", u"Register a new account", None))
        self.label_3.setText(QCoreApplication.translate("Create_account", u"Username:", None))
        self.label_4.setText(QCoreApplication.translate("Create_account", u"Password:", None))
        self.label_5.setText(QCoreApplication.translate("Create_account", u"Confirm password:", None))
        self.label_6.setText(QCoreApplication.translate("Create_account", u"Experince Level:", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Create_account", u"Medior", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Create_account", u"Senior", None))

        self.comboBox.setCurrentText("")
        self.errorLabel.setText("")
        self.createButton.setText(QCoreApplication.translate("Create_account", u"Create accont", None))
        self.backButton.setText(QCoreApplication.translate("Create_account", u"Back", None))
    # retranslateUi

