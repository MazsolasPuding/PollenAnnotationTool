# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drive_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_DriveDialog(object):
    def setupUi(self, DriveDialog):
        if not DriveDialog.objectName():
            DriveDialog.setObjectName(u"DriveDialog")
        DriveDialog.resize(400, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DriveDialog.sizePolicy().hasHeightForWidth())
        DriveDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(DriveDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(DriveDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)

        self.verticalLayout.addWidget(self.treeWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectButton = QPushButton(DriveDialog)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout.addWidget(self.selectButton)

        self.cancelButton = QPushButton(DriveDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(DriveDialog)

        QMetaObject.connectSlotsByName(DriveDialog)
    # setupUi

    def retranslateUi(self, DriveDialog):
        DriveDialog.setWindowTitle(QCoreApplication.translate("DriveDialog", u"Open a Drive Driectory", None))
        self.selectButton.setText(QCoreApplication.translate("DriveDialog", u"Select", None))
        self.cancelButton.setText(QCoreApplication.translate("DriveDialog", u"Cancel", None))
    # retranslateUi

