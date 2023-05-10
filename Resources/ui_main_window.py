# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDockWidget, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1700, 950)
        font = QFont()
        font.setFamilies([u"SansSerif"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/pollen-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen_Dir = QAction(MainWindow)
        self.actionOpen_Dir.setObjectName(u"actionOpen_Dir")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Dir.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionPrevious = QAction(MainWindow)
        self.actionPrevious.setObjectName(u"actionPrevious")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrevious.setIcon(icon4)
        self.actionNext = QAction(MainWindow)
        self.actionNext.setObjectName(u"actionNext")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNext.setIcon(icon5)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/aboutIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/aboutQtIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAboutQt.setIcon(icon7)
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_In.setIcon(icon8)
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_Out.setIcon(icon9)
        self.actionFit_Window = QAction(MainWindow)
        self.actionFit_Window.setObjectName(u"actionFit_Window")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/fit-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFit_Window.setIcon(icon10)
        self.actionSign_Out = QAction(MainWindow)
        self.actionSign_Out.setObjectName(u"actionSign_Out")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/sign-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSign_Out.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.annotation_tab = QWidget()
        self.annotation_tab.setObjectName(u"annotation_tab")
        self.verticalLayout_5 = QVBoxLayout(self.annotation_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pictureLabel = QLabel(self.annotation_tab)
        self.pictureLabel.setObjectName(u"pictureLabel")
        self.pictureLabel.setStyleSheet(u"background-color:rgb(216, 246, 255);\n"
"font: 20pt \"SansSerif\";")
        self.pictureLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.pictureLabel)

        self.tabWidget.addTab(self.annotation_tab, "")
        self.review_tab = QWidget()
        self.review_tab.setObjectName(u"review_tab")
        self.horizontalLayout_12 = QHBoxLayout(self.review_tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pictureLabel_2 = QLabel(self.review_tab)
        self.pictureLabel_2.setObjectName(u"pictureLabel_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictureLabel_2.sizePolicy().hasHeightForWidth())
        self.pictureLabel_2.setSizePolicy(sizePolicy)
        self.pictureLabel_2.setMinimumSize(QSize(800, 0))
        self.pictureLabel_2.setStyleSheet(u"background-color:rgb(216, 246, 255);\n"
"font: 20pt \"SansSerif\";")
        self.pictureLabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.pictureLabel_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.query_frame = QFrame(self.review_tab)
        self.query_frame.setObjectName(u"query_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.query_frame.sizePolicy().hasHeightForWidth())
        self.query_frame.setSizePolicy(sizePolicy1)
        self.query_frame.setMinimumSize(QSize(300, 0))
        self.query_frame.setStyleSheet(u"QFrame#query_frame{\n"
"border: 1px solid black;\n"
"}")
        self.query_frame.setFrameShape(QFrame.StyledPanel)
        self.query_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.query_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_28 = QLabel(self.query_frame)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setMinimumSize(QSize(0, 30))
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_28)

        self.line_4 = QFrame(self.query_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_32 = QLabel(self.query_frame)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_17.addWidget(self.label_32)

        self.user_list_comboBox = QComboBox(self.query_frame)
        self.user_list_comboBox.addItem("")
        self.user_list_comboBox.setObjectName(u"user_list_comboBox")

        self.horizontalLayout_17.addWidget(self.user_list_comboBox)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_29 = QLabel(self.query_frame)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_14.addWidget(self.label_29)

        self.from_dateTimeEdit = QDateTimeEdit(self.query_frame)
        self.from_dateTimeEdit.setObjectName(u"from_dateTimeEdit")
        self.from_dateTimeEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.from_dateTimeEdit.setCurrentSection(QDateTimeEdit.YearSection)

        self.horizontalLayout_14.addWidget(self.from_dateTimeEdit)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_30 = QLabel(self.query_frame)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_15.addWidget(self.label_30)

        self.until_dateTimeEdit = QDateTimeEdit(self.query_frame)
        self.until_dateTimeEdit.setObjectName(u"until_dateTimeEdit")
        self.until_dateTimeEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_15.addWidget(self.until_dateTimeEdit)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.all_times_checkBox = QCheckBox(self.query_frame)
        self.all_times_checkBox.setObjectName(u"all_times_checkBox")

        self.verticalLayout_9.addWidget(self.all_times_checkBox)

        self.include_senior_checkBox = QCheckBox(self.query_frame)
        self.include_senior_checkBox.setObjectName(u"include_senior_checkBox")

        self.verticalLayout_9.addWidget(self.include_senior_checkBox)

        self.load_annotations_Button = QPushButton(self.query_frame)
        self.load_annotations_Button.setObjectName(u"load_annotations_Button")
        self.load_annotations_Button.setMinimumSize(QSize(0, 30))

        self.verticalLayout_9.addWidget(self.load_annotations_Button)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.query_frame)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_13.addWidget(self.label_31)

        self.lcdNumber = QLCDNumber(self.query_frame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        self.lcdNumber.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_13.addWidget(self.lcdNumber)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.verticalLayout_8.addWidget(self.query_frame)

        self.data_frame = QFrame(self.review_tab)
        self.data_frame.setObjectName(u"data_frame")
        sizePolicy1.setHeightForWidth(self.data_frame.sizePolicy().hasHeightForWidth())
        self.data_frame.setSizePolicy(sizePolicy1)
        self.data_frame.setMinimumSize(QSize(300, 0))
        self.data_frame.setStyleSheet(u"QFrame#data_frame{\n"
"border: 1px solid black;\n"
"}")
        self.data_frame.setFrameShape(QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.data_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_27 = QLabel(self.data_frame)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setMinimumSize(QSize(0, 30))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_27)

        self.line_3 = QFrame(self.data_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.data_frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_18.addWidget(self.label_10)

        self.annotation_id_label = QLabel(self.data_frame)
        self.annotation_id_label.setObjectName(u"annotation_id_label")

        self.horizontalLayout_18.addWidget(self.annotation_id_label)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.data_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.path_label = QLabel(self.data_frame)
        self.path_label.setObjectName(u"path_label")

        self.horizontalLayout_4.addWidget(self.path_label)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.data_frame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.class_label = QLabel(self.data_frame)
        self.class_label.setObjectName(u"class_label")

        self.horizontalLayout_5.addWidget(self.class_label)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.data_frame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.confidence_label = QLabel(self.data_frame)
        self.confidence_label.setObjectName(u"confidence_label")

        self.horizontalLayout_6.addWidget(self.confidence_label)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.data_frame)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.comment_label = QLabel(self.data_frame)
        self.comment_label.setObjectName(u"comment_label")

        self.horizontalLayout_7.addWidget(self.comment_label)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_18 = QLabel(self.data_frame)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_8.addWidget(self.label_18)

        self.user_label = QLabel(self.data_frame)
        self.user_label.setObjectName(u"user_label")

        self.horizontalLayout_8.addWidget(self.user_label)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_20 = QLabel(self.data_frame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_9.addWidget(self.label_20)

        self.is_senior_label = QLabel(self.data_frame)
        self.is_senior_label.setObjectName(u"is_senior_label")

        self.horizontalLayout_9.addWidget(self.is_senior_label)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.data_frame)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_10.addWidget(self.label_22)

        self.timestamp_label = QLabel(self.data_frame)
        self.timestamp_label.setObjectName(u"timestamp_label")

        self.horizontalLayout_10.addWidget(self.timestamp_label)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout_8.addWidget(self.data_frame)

        self.review_frame = QFrame(self.review_tab)
        self.review_frame.setObjectName(u"review_frame")
        sizePolicy1.setHeightForWidth(self.review_frame.sizePolicy().hasHeightForWidth())
        self.review_frame.setSizePolicy(sizePolicy1)
        self.review_frame.setMinimumSize(QSize(300, 0))
        self.review_frame.setStyleSheet(u"QFrame#review_frame{\n"
"border: 1px solid black;\n"
"}")
        self.review_frame.setFrameShape(QFrame.StyledPanel)
        self.review_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.review_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_26 = QLabel(self.review_frame)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_26)

        self.line_2 = QFrame(self.review_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_24 = QLabel(self.review_frame)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_11.addWidget(self.label_24)

        self.score_spinBox = QSpinBox(self.review_frame)
        self.score_spinBox.setObjectName(u"score_spinBox")
        self.score_spinBox.setMaximum(100)
        self.score_spinBox.setValue(50)

        self.horizontalLayout_11.addWidget(self.score_spinBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.label_25 = QLabel(self.review_frame)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_7.addWidget(self.label_25)

        self.review_comment_lineEdit = QLineEdit(self.review_frame)
        self.review_comment_lineEdit.setObjectName(u"review_comment_lineEdit")

        self.verticalLayout_7.addWidget(self.review_comment_lineEdit)


        self.verticalLayout_8.addWidget(self.review_frame)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 1)

        self.horizontalLayout_12.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.review_tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1700, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.thumbnailDock = QDockWidget(MainWindow)
        self.thumbnailDock.setObjectName(u"thumbnailDock")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.thumbnailDock.sizePolicy().hasHeightForWidth())
        self.thumbnailDock.setSizePolicy(sizePolicy4)
        self.thumbnailDock.setMinimumSize(QSize(288, 300))
        self.thumbnailDock.setStyleSheet(u"QDockWidget#thumbnailDock{\n"
"border: 1px solid black;\n"
"}")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setStyleSheet(u"QWidget#dockWidgetContents{\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.dockWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.thumbnailsView = QTableView(self.dockWidgetContents)
        self.thumbnailsView.setObjectName(u"thumbnailsView")
        self.thumbnailsView.setMinimumSize(QSize(270, 0))

        self.verticalLayout_3.addWidget(self.thumbnailsView)

        self.thumbnailDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.thumbnailDock)
        self.metadataDock = QDockWidget(MainWindow)
        self.metadataDock.setObjectName(u"metadataDock")
        sizePolicy4.setHeightForWidth(self.metadataDock.sizePolicy().hasHeightForWidth())
        self.metadataDock.setSizePolicy(sizePolicy4)
        self.metadataDock.setMinimumSize(QSize(100, 450))
        self.metadataDock.setStyleSheet(u"QDockWidget#metadataDock{\n"
"border: 1px solid black;\n"
"}")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.dockWidgetContents_2.setStyleSheet(u"QWidget#dockWidgetContents_2{\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.dockWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.metadataTableWidget = QTableWidget(self.dockWidgetContents_2)
        self.metadataTableWidget.setObjectName(u"metadataTableWidget")

        self.verticalLayout_4.addWidget(self.metadataTableWidget)

        self.metadataDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.metadataDock)
        self.labellingDock = QDockWidget(MainWindow)
        self.labellingDock.setObjectName(u"labellingDock")
        self.labellingDock.setStyleSheet(u"QWidget#dockWidgetContents_3{\n"
"border: 1px solid black;\n"
"}")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.dockWidgetContents_3)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pollenListWidget = QListWidget(self.dockWidgetContents_3)
        self.pollenListWidget.setObjectName(u"pollenListWidget")

        self.verticalLayout.addWidget(self.pollenListWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.dockWidgetContents_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.confidenceSlider = QSlider(self.dockWidgetContents_3)
        self.confidenceSlider.setObjectName(u"confidenceSlider")
        self.confidenceSlider.setMinimum(0)
        self.confidenceSlider.setMaximum(10)
        self.confidenceSlider.setSingleStep(1)
        self.confidenceSlider.setPageStep(1)
        self.confidenceSlider.setSliderPosition(5)
        self.confidenceSlider.setOrientation(Qt.Horizontal)
        self.confidenceSlider.setTickPosition(QSlider.TicksBelow)
        self.confidenceSlider.setTickInterval(1)

        self.verticalLayout.addWidget(self.confidenceSlider)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.dockWidgetContents_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(self.dockWidgetContents_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_7 = QLabel(self.dockWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.dockWidgetContents_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.commentEdit = QLineEdit(self.dockWidgetContents_3)
        self.commentEdit.setObjectName(u"commentEdit")

        self.verticalLayout.addWidget(self.commentEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(self.dockWidgetContents_3)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 50))
        self.saveButton.setStyleSheet(u"")
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevButton = QPushButton(self.dockWidgetContents_3)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setMinimumSize(QSize(0, 50))
        self.prevButton.setIcon(icon4)
        self.prevButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.prevButton)

        self.nextButton = QPushButton(self.dockWidgetContents_3)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(0, 50))
        self.nextButton.setIcon(icon5)
        self.nextButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labellingDock.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.labellingDock)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setSizeIncrement(QSize(40, 40))
        self.toolBar.setBaseSize(QSize(40, 40))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSign_Out)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionPrevious)
        self.menuView.addAction(self.actionNext)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.toolBar.addAction(self.actionSign_Out)
        self.toolBar.addAction(self.actionOpen_Dir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pollen Annotation", None))
        self.actionOpen_Dir.setText(QCoreApplication.translate("MainWindow", u"Open Dir", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPrevious.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.actionNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.actionFit_Window.setText(QCoreApplication.translate("MainWindow", u"Fit Window", None))
        self.actionSign_Out.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.pictureLabel.setText(QCoreApplication.translate("MainWindow", u"Open a Directory to show images.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.annotation_tab), QCoreApplication.translate("MainWindow", u"Annotation Tab", None))
        self.pictureLabel_2.setText(QCoreApplication.translate("MainWindow", u"Load from Database to show images.", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Annotation Database Query", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.user_list_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Users", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Date from:", None))
        self.from_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d   h:mm", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Date Until:", None))
        self.until_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d   h:mm", None))
        self.all_times_checkBox.setText(QCoreApplication.translate("MainWindow", u"All times (ignore date settings)", None))
        self.include_senior_checkBox.setText(QCoreApplication.translate("MainWindow", u"Include Senior Annotations for review", None))
        self.load_annotations_Button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Selected Items for Review:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Annotation ID:", None))
        self.annotation_id_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.path_label.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Class:", None))
        self.class_label.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Confidence:", None))
        self.confidence_label.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.comment_label.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.user_label.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Experience:", None))
        self.is_senior_label.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None))
        self.timestamp_label.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Review", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Review Score: [1-100]", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.review_tab), QCoreApplication.translate("MainWindow", u"Review Tab", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.thumbnailDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thumbnail Dock", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Current Directory:", None))
        self.metadataDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Info Dock", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Metadata:", None))
        self.labellingDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Labelling Dock", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pollen Type:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confidence Scale:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

