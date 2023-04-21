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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTableView, QTableWidget, QTableWidgetItem,
    QToolBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_senior_MainWindow(object):
    def setupUi(self, senior_MainWindow):
        if not senior_MainWindow.objectName():
            senior_MainWindow.setObjectName(u"senior_MainWindow")
        senior_MainWindow.resize(1700, 950)
        font = QFont()
        font.setFamilies([u"SansSerif"])
        font.setPointSize(9)
        senior_MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/pollen-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        senior_MainWindow.setWindowIcon(icon)
        self.actionOpen_Dir = QAction(senior_MainWindow)
        self.actionOpen_Dir.setObjectName(u"actionOpen_Dir")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Dir.setIcon(icon1)
        self.actionSave = QAction(senior_MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionQuit = QAction(senior_MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionPrevious = QAction(senior_MainWindow)
        self.actionPrevious.setObjectName(u"actionPrevious")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrevious.setIcon(icon4)
        self.actionNext = QAction(senior_MainWindow)
        self.actionNext.setObjectName(u"actionNext")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNext.setIcon(icon5)
        self.actionAbout = QAction(senior_MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/aboutIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon6)
        self.actionAboutQt = QAction(senior_MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/aboutQtIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAboutQt.setIcon(icon7)
        self.actionZoom_In = QAction(senior_MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_In.setIcon(icon8)
        self.actionZoom_Out = QAction(senior_MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_Out.setIcon(icon9)
        self.actionFit_Window = QAction(senior_MainWindow)
        self.actionFit_Window.setObjectName(u"actionFit_Window")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/fit-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFit_Window.setIcon(icon10)
        self.centralwidget = QWidget(senior_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pictureLabel = QLabel(self.centralwidget)
        self.pictureLabel.setObjectName(u"pictureLabel")
        self.pictureLabel.setStyleSheet(u"background-color:rgb(216, 246, 255);\n"
"font: 20pt \"SansSerif\";")
        self.pictureLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.pictureLabel)

        senior_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(senior_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1700, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        senior_MainWindow.setMenuBar(self.menubar)
        self.thumbnailDock = QDockWidget(senior_MainWindow)
        self.thumbnailDock.setObjectName(u"thumbnailDock")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnailDock.sizePolicy().hasHeightForWidth())
        self.thumbnailDock.setSizePolicy(sizePolicy)
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
        senior_MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.thumbnailDock)
        self.metadataDock = QDockWidget(senior_MainWindow)
        self.metadataDock.setObjectName(u"metadataDock")
        sizePolicy.setHeightForWidth(self.metadataDock.sizePolicy().hasHeightForWidth())
        self.metadataDock.setSizePolicy(sizePolicy)
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
        self.label_10 = QLabel(self.dockWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.directoryView = QTreeWidget(self.dockWidgetContents_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.directoryView.setHeaderItem(__qtreewidgetitem)
        self.directoryView.setObjectName(u"directoryView")

        self.verticalLayout_4.addWidget(self.directoryView)

        self.line = QFrame(self.dockWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_5 = QLabel(self.dockWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.metadataTableWidget = QTableWidget(self.dockWidgetContents_2)
        self.metadataTableWidget.setObjectName(u"metadataTableWidget")

        self.verticalLayout_4.addWidget(self.metadataTableWidget)

        self.metadataDock.setWidget(self.dockWidgetContents_2)
        senior_MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.metadataDock)
        self.labellingDock = QDockWidget(senior_MainWindow)
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
        senior_MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.labellingDock)
        self.statusBar = QStatusBar(senior_MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        senior_MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(senior_MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setSizeIncrement(QSize(40, 40))
        self.toolBar.setBaseSize(QSize(40, 40))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        senior_MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionPrevious)
        self.menuView.addAction(self.actionNext)
        self.menuView.addAction(self.actionFit_Window)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.toolBar.addAction(self.actionOpen_Dir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFit_Window)
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)

        self.retranslateUi(senior_MainWindow)

        QMetaObject.connectSlotsByName(senior_MainWindow)
    # setupUi

    def retranslateUi(self, senior_MainWindow):
        senior_MainWindow.setWindowTitle(QCoreApplication.translate("senior_MainWindow", u"Pollen Annotation", None))
        self.actionOpen_Dir.setText(QCoreApplication.translate("senior_MainWindow", u"Open Dir", None))
        self.actionSave.setText(QCoreApplication.translate("senior_MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("senior_MainWindow", u"Quit", None))
        self.actionPrevious.setText(QCoreApplication.translate("senior_MainWindow", u"Prev", None))
        self.actionNext.setText(QCoreApplication.translate("senior_MainWindow", u"Next", None))
        self.actionAbout.setText(QCoreApplication.translate("senior_MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("senior_MainWindow", u"AboutQt", None))
        self.actionZoom_In.setText(QCoreApplication.translate("senior_MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("senior_MainWindow", u"Zoom Out", None))
        self.actionFit_Window.setText(QCoreApplication.translate("senior_MainWindow", u"Fit Window", None))
        self.pictureLabel.setText(QCoreApplication.translate("senior_MainWindow", u"Open a Directory to show images.", None))
        self.menuFile.setTitle(QCoreApplication.translate("senior_MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("senior_MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("senior_MainWindow", u"Help", None))
        self.thumbnailDock.setWindowTitle(QCoreApplication.translate("senior_MainWindow", u"Thumbnail Dock", None))
        self.label_11.setText(QCoreApplication.translate("senior_MainWindow", u"Current Directory:", None))
        self.metadataDock.setWindowTitle(QCoreApplication.translate("senior_MainWindow", u"Info Dock", None))
        self.label_10.setText(QCoreApplication.translate("senior_MainWindow", u"Driectroy View:", None))
        self.label_5.setText(QCoreApplication.translate("senior_MainWindow", u"Metadata:", None))
        self.labellingDock.setWindowTitle(QCoreApplication.translate("senior_MainWindow", u"Labelling Dock", None))
        self.label.setText(QCoreApplication.translate("senior_MainWindow", u"Pollen Type:", None))
        self.label_3.setText(QCoreApplication.translate("senior_MainWindow", u"Confidence Scale:", None))
        self.label_8.setText(QCoreApplication.translate("senior_MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("senior_MainWindow", u"50", None))
        self.label_7.setText(QCoreApplication.translate("senior_MainWindow", u"100", None))
        self.label_4.setText(QCoreApplication.translate("senior_MainWindow", u"Comment:", None))
        self.saveButton.setText(QCoreApplication.translate("senior_MainWindow", u"Save", None))
        self.prevButton.setText(QCoreApplication.translate("senior_MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("senior_MainWindow", u"Next", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("senior_MainWindow", u"toolBar", None))
    # retranslateUi
