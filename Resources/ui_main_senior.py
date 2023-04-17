# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_senior.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Main_senior(object):
    def setupUi(self, Main_senior):
        if not Main_senior.objectName():
            Main_senior.setObjectName(u"Main_senior")
        Main_senior.resize(800, 600)
        self.centralwidget = QWidget(Main_senior)
        self.centralwidget.setObjectName(u"centralwidget")
        Main_senior.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main_senior)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Main_senior.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main_senior)
        self.statusbar.setObjectName(u"statusbar")
        Main_senior.setStatusBar(self.statusbar)

        self.retranslateUi(Main_senior)

        QMetaObject.connectSlotsByName(Main_senior)
    # setupUi

    def retranslateUi(self, Main_senior):
        Main_senior.setWindowTitle(QCoreApplication.translate("Main_senior", u"MainWindow", None))
    # retranslateUi

