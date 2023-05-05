from PySide6.QtWidgets import QApplication, QDialog, QWidget, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QTreeWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

import os
import sys
import glob
import codecs
import sqlite3
import datetime
from collections import namedtuple
import xml.etree.ElementTree as ET

from Resources.ui_main_window import Ui_MainWindow
from Libs.thumbnails import PreviewDelegate, PreviewModel
from Libs.pollen import Pollen

__appname__ = "Pollen"
preview = namedtuple("preview", ['id', 'path', 'image'])

class MainSenior(QMainWindow, Ui_MainWindow):
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
        self.current_pollen = ""
        self.saved = False

        # Load Pollen classes
        self.load_predefined_classes(self.predef_classes_path)
        self.toggle_all_actions(False)

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
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionZoom_Out.triggered.connect(self.zoom_out)
        self.actionFit_Window.triggered.connect(self.fit_window)

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

        # Set Table widget
        self.metadataTableWidget.setColumnCount(2)
        self.metadataTableWidget.horizontalHeader().hide()
        self.directoryView.setHeaderHidden(True)
        self.saveButton.setEnabled(False)
        

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.information(self, "About", "For Help check the included README File or contact the creator of the app.")

    def aboutQt(self):
        QApplication.aboutQt()

    def load_images(self):
        self.reset()
        self.open_dir_dialog()
        self.load_subdirectory_tree(self.directoryView)
        self.create_pollen_objects()
        if self.images:
            self.show_image()
            self.show_thumbnails()
            self.toggle_all_actions()
            self.actionSave.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.prevButton.setEnabled(False)
            self.actionPrevious.setEnabled(False)

    def create_pollen_objects(self):
        for n, fn in enumerate(glob.glob(f"{self.images_directory_path}/*.jp*g")):
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
        try:
            self.current_pollen = self.images[self.index]
        except IndexError:
            QMessageBox.information(self, "Empty Directory", "The current directory does not contain any pictures.")

    def open_dir_dialog(self):
        self.images_directory_path = QFileDialog.getExistingDirectory(self,
                                                                    '%s - Open Directory' % __appname__, "",
                                                                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

    def load_subdirectory_tree(self, tree_widget):
        root_element = ET.Element("directory_tree")
        for root, dirs, files in os.walk(self.images_directory_path):
            dir_element = ET.SubElement(root_element, "directory", name=os.path.basename(root))
            for f in files:
                ET.SubElement(dir_element, "file", name=f)

        # clear the tree widget before populating it
        tree_widget.clear()

        # create the root item
        root_item = QTreeWidgetItem(tree_widget)
        root_item.setText(0, os.path.basename(self.images_directory_path))

        # recursively add child items for each directory and file in the tree
        self._add_child_items(root_element, root_item)

    def _add_child_items(self, xml_element, parent_item):
        # iterate over the child elements of the XML element
        for child_element in xml_element:
            # create an item for the directory or file
            item = QTreeWidgetItem(parent_item)
            item.setText(0, child_element.get('name'))
            if child_element.tag == 'directory':
                # if the child element is a directory, recursively add child items
                self._add_child_items(child_element, item)


    def show_image(self):
        current_image = self.images[self.index].pixmap
        size = self.pictureLabel.size()
        scaled_image = current_image.scaled(size, aspectMode=Qt.KeepAspectRatio)
        self.pictureLabel.setPixmap(scaled_image)
        self.load_metadata_to_table()

    def load_metadata_to_table(self):
        metadata = self.current_pollen.metadata
        if not metadata:
            return
        self.metadataTableWidget.setRowCount(len(metadata))
        col = 0
        for k, v in metadata.items():
            self.metadataTableWidget.setItem(col, 0, QTableWidgetItem(str(k)))
            self.metadataTableWidget.setItem(col, 1, QTableWidgetItem(str(v)))
            col += 1        

    def show_thumbnails(self):
        for n, fn in enumerate(glob.glob(f"{self.images_directory_path}/*.jp*g")):
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
        if self.current_pollen.labelled == False:
            self.current_pollen.class_ = item.text()
            self.saveButton.setEnabled(True)
            self.actionSave.setEnabled(True)

    def previous(self):
        self.index -= 1
        self.current_pollen = self.images[self.index]
        self._keep_in_range()
        self._set_style_sheet(self.current_pollen.labelled)
        self.show_image()

    def next(self):
        self.index += 1
        self.current_pollen = self.images[self.index]
        self._keep_in_range()
        self._set_style_sheet(self.current_pollen.labelled)
        self.show_image()
    
    def _keep_in_range(self):
        if self.index >= len(self.images) - 1:
            self.nextButton.setEnabled(False)
            self.actionNext.setEnabled(False)
        elif self.index <= 0:
            self.prevButton.setEnabled(False)
            self.actionPrevious.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)
            self.actionNext.setEnabled(True)
            self.prevButton.setEnabled(True)
            self.actionPrevious.setEnabled(True)

    def _set_style_sheet(self, green=False):
        if green:
            self.pictureLabel.setStyleSheet("background-color:rgb(89, 255, 103)")
            self.saveButton.setStyleSheet("background-color:rgb(89, 255, 103)")
            self.actionSave.setEnabled(False)
            self.saveButton.setEnabled(False)
        else:
            self.pictureLabel.setStyleSheet("background-color:rgb(216, 246, 255); font: 20pt 'SansSerif';")
            self.saveButton.setStyleSheet("")

    def _is_remaining(self):
        for pollen in self.images:
            if not pollen.labelled:
                return True
        return False
        
    def finished_folder(self):
        self.reset()
        QMessageBox.information(self, "Finished", "You have labelled all pictures in this folder.")

    def zoom_in(self):
        pass

    def zoom_out(self):
        pass

    def fit_window(self):
        pass

    def save(self):
        self.current_pollen.confidence = self.confidenceSlider.value()
        self.current_pollen.comment = self.commentEdit.text()
        if not self.save_to_db():
            QMessageBox.critical(self, "Database Error", "Could not write to database, plase try again or restart the application.")
            return
        self.saved = True
        self.current_pollen.labelled = True
        self._set_style_sheet(True)
        print(self.current_pollen)
        if not self._is_remaining():
            self.finished_folder()

    def save_to_db(self):
        connection = sqlite3.connect("annotation.db")
        cursor = connection.cursor()
        pollen_info = [self.current_pollen.path,
                       self.current_pollen.class_,
                       self.current_pollen.confidence,
                       self.current_pollen.comment,
                       self.current_pollen.user,
                       self.current_pollen.is_senior,
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M")]
        try:
            query = 'INSERT INTO annotation (path, class, confidence, comment, user, is_senior, time_stamp) VALUES (?,?,?,?,?,?,?)'
            cursor.execute(query, pollen_info)
            connection.commit()
            connection.close()
            return True
        except sqlite3.OperationalError or sqlite3.IntegrityError:
            return False

    def reset(self):
        self.images = []
        self.index = 0
        self.delegate = PreviewDelegate()
        self.thumbnailsView.setItemDelegate(self.delegate)
        self.model = PreviewModel()
        self.thumbnailsView.setModel(self.model)
        self._set_style_sheet(False)
        self.toggle_all_actions(False)
        self.pictureLabel.setText("Open a Directory to show images.")

    def toggle_all_actions(self, enable=True):
        self.saveButton.setEnabled(enable)
        self.nextButton.setEnabled(enable)
        self.prevButton.setEnabled(enable)
        self.actionNext.setEnabled(enable)
        self.actionPrevious.setEnabled(enable)
        self.actionSave.setEnabled(enable)
        self.confidenceSlider.setEnabled(enable)
        self.commentEdit.setEnabled(enable)
        self.pollenListWidget.setEnabled(enable)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainSenior(app)
    window.show()
    app.exec()
