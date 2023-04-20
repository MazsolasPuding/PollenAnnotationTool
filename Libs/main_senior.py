from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

import os.path
import sys
import glob
import codecs
from collections import namedtuple

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

        #
        self.load_predefined_classes(self.predef_classes_path)

        # Set actions
        self.actionQuit.triggered.connect(self.quit)
        self.actionOpen_Dir.triggered.connect(self.load_images)
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

    def reset(self):
        self.images = []
        self.index = 0
        self.delegate = PreviewDelegate()
        self.thumbnailsView.setItemDelegate(self.delegate)
        self.model = PreviewModel()
        self.thumbnailsView.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainSenior(app)
    window.show()
    app.exec()
