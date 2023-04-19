from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage

import os.path
import sys
import glob
from collections import namedtuple

from Resources.ui_main_senior import Ui_senior_MainWindow
from Libs.thumbnails import PreviewDelegate, PreviewModel

__appname__ = "Pollen"
preview = namedtuple("preview", "id title image")

class MainSenior(QMainWindow, Ui_senior_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.open_directory = ""

        self.actionQuit.triggered.connect(self.quit)
        self.actionOpen_Dir.triggered.connect(self.open_dir_dialog)
        

        # self.thumbnailsView.horizontalHeader.hide()
        # self.thumbnailsView.verticalHeader.hide()
        self.thumbnailsView.setGridStyle(Qt.NoPen)
        
        self.delegate = PreviewDelegate()
        self.thumbnailsView.setItemDelegate(self.delegate)
        self.model = PreviewModel()
        self.thumbnailsView.setModel(self.model)

        

    
    def quit(self):
        self.app.quit()

    def open_dir_dialog(self):
        self.open_directory = QFileDialog.getExistingDirectory(self,
                                                                    '%s - Open Directory' % __appname__, "",
                                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print(self.open_directory)
        self.show_thumbnails()
    
    def show_thumbnails(self):
        for n, fn in enumerate(glob.glob(f"{self.open_directory}/*.jpg")):
            image = QImage(fn)
            item = preview(n, fn, image)
            self.model.previews.append(item)
        self.model.layoutChanged.emit()
        self.thumbnailsView.resizeRowsToContents()
        self.thumbnailsView.resizeColumnsToContents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainSenior(app)
    window.show()
    app.exec()