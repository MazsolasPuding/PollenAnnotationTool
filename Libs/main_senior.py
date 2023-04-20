from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

import os.path
import sys
import glob
import codecs
from collections import namedtuple
import sqlite3
import datetime

from Resources.ui_main_senior import Ui_senior_MainWindow
from Libs.thumbnails import PreviewDelegate, PreviewModel
from Libs.pollen import Pollen

__appname__ = "Pollen"
preview = namedtuple("preview", ['id', 'path', 'image'])

class MainSenior(QMainWindow, Ui_senior_MainWindow):
    def __init__(self, app, user, is_senior):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.images_directory_path = ""
        self.predef_classes_path = "./Data/predefined_classes.txt"
        self.label_list = []
        self.images = []
        self.user = user
        self.is_senior = is_senior
        self.index = 0

        # Load Pollen classes
        self.load_predefined_classes(self.predef_classes_path)

        # Add Menu actions
        self.label_dock_view_action = self.labellingDock.toggleViewAction()
        self.label_dock_view_action.setText("Labelling Dock")
        self.menuView.addAction(self.label_dock_view_action)
        self.info_dock_view_action = self.metadataDock.toggleViewAction()
        self.info_dock_view_action.setText("Info Dock")
        self.menuView.addAction(self.info_dock_view_action)
        self.thumbnail_dock_view_action = self.thumbnailDock.toggleViewAction()
        self.thumbnail_dock_view_action.setText("Thumbnail Dock")
        self.menuView.addAction(self.thumbnail_dock_view_action)
        

        # Set actions
        self.actionQuit.triggered.connect(self.quit)
        self.actionOpen_Dir.triggered.connect(self.load_images)
        self.actionNext.triggered.connect(self.next)
        self.actionPrevious.triggered.connect(self.previous)
        self.actionSave.triggered.connect(self.save)
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        self.pollenListWidget.itemClicked.connect(self.class_selected)
        self.nextButton.clicked.connect(self.next)
        self.prevButton.clicked.connect(self.previous)
        self.saveButton.clicked.connect(self.save)

        # Init thumbnail view
        self.thumbnailsView.setGridStyle(Qt.NoPen)
        self.thumbnailsView.horizontalHeader().hide()
        self.thumbnailsView.verticalHeader().hide()
        self.delegate = PreviewDelegate()
        self.thumbnailsView.setItemDelegate(self.delegate)
        self.model = PreviewModel()
        self.thumbnailsView.setModel(self.model)


    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.information(self, "About", "For Help check the included README File or contact the creator of the app.")

    def aboutQt(self):
        QApplication.aboutQt()

    def load_images(self):
        self.reset()
        self.open_dir_dialog()

        for n, fn in enumerate(glob.glob(f"{self.images_directory_path}/*.jpg")):
            p = Pollen()
            p.path = fn
            p.user = self.user
            p.is_senior = self.is_senior
            p.pixmap = QPixmap(fn)
            try:
                p.get_image_metadata()
            except:
                print(f"No metadata at {fn}")
            self.images.append(p)
        
        self.show_image()
        self.show_thumbnails()


    def open_dir_dialog(self):
        self.images_directory_path = QFileDialog.getExistingDirectory(self,
                                                                    '%s - Open Directory' % __appname__, "",
                                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

    def show_image(self):
        self.pictureLabel.setPixmap(self.images[self.index].pixmap)

    def show_thumbnails(self):
        for n, fn in enumerate(glob.glob(f"{self.images_directory_path}/*.jpg")):
            image = QImage(fn)
            item = preview(n, fn, image)
            self.model.previews.append(item)
        self.model.layoutChanged.emit()
        self.thumbnailsView.resizeRowsToContents()
        self.thumbnailsView.resizeColumnsToContents()

    def load_predefined_classes(self, predef_classes_file):
        if os.path.exists(predef_classes_file) is True:
            with codecs.open(predef_classes_file, 'r', 'utf8') as f:
                for line in f:
                    line = line.strip()
                    if self.label_list is None:
                        self.label_list = [line]
                    else:
                        self.label_list.append(line)
        self.pollenListWidget.addItems(self.label_list)

    def class_selected(self, item):
        self.images[self.index].class_ = item.text()

    def previous(self):
        self.index -= 1
        self.show_image()

    def next(self):
        self.index += 1
        try:
            self.show_image()
        except IndexError:
            self.index = 0
            self.show_image()

    def save(self):
        self.images[self.index].confidence = self.confidenceSlider.value()
        self.images[self.index].comment = self.commentEdit.text()
        attrs = vars(self.images[self.index])
        print(', '.join("%s: %s" % item for item in attrs.items()))
        self.save_to_db()

    def reset(self):
        self.images = []
        self.index = 0
        self.delegate = PreviewDelegate()
        self.thumbnailsView.setItemDelegate(self.delegate)
        self.model = PreviewModel()
        self.thumbnailsView.setModel(self.model)

    def save_to_db(self):
        connection = sqlite3.connect("annotation.db")
        cursor = connection.cursor()
        pollen_info = [self.images[self.index].path,
                       self.images[self.index].class_,
                       self.images[self.index].confidence,
                       self.images[self.index].comment,
                       self.images[self.index].user,
                       self.images[self.index].is_senior,
                       datetime.datetime.now()]
        query = 'INSERT INTO annotation (path, class, confidence, comment, user, is_senior, time_stamp) VALUES (?,?,?,?,?,?,?)'
        cursor.execute(query, pollen_info)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainSenior(app)
    window.show()
    app.exec()
