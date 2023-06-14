
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QTreeWidgetItem, QSizePolicy
from PySide6.QtCore import Qt, QtMsgType, qInstallMessageHandler
from PySide6.QtGui import QImage, QPixmap

import os
import sys
import glob
import codecs
import datetime
import psycopg2
from pprint import pprint
from collections import namedtuple
import xml.etree.ElementTree as ET

from Resources.ui_main_window import Ui_MainWindow
from Libs.thumbnails import PreviewDelegate, PreviewModel
from Libs.pollen import Pollen
from Libs.connect_to_db import Connection

__appname__ = "Pollen"
preview = namedtuple("preview", ['id', 'path', 'image'])

class MainWindow(QMainWindow, Ui_MainWindow):
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
        self.names_loaded = False
        self.loaded_data = {}
        self.mode = "annotation"

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
        self.actionSign_Out.triggered.connect(self.sing_out)

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
        self.saveButton.setEnabled(False)

        # Review Page
        self.tabWidget.setCurrentIndex(0)
        if self.is_senior != 1:
            self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.tabBarClicked.connect(self.tab_selected)
        self.load_annotations_Button.clicked.connect(self.load_data_from_db)
        self.all_times_checkBox.clicked.connect(self.all_times)
        self.user_list_comboBox.textActivated.connect(self.user_selected)
        

    def quit(self):
        self.app.quit()
    
    def closeEvent(self, event):
        QApplication.instance().aboutToQuit.emit()

    def sing_out(self):
        button = QMessageBox.question(self, "Signing out?", "Do you want to Sign Out?")
        if button == QMessageBox.Yes:
            self.close()
        return

    def about(self):
        QMessageBox.information(self, "About", "For Help check the included README File or contact the creator of the app.")

    def aboutQt(self):
        QApplication.aboutQt()

    def load_images(self, *,mode='annotation'):
        self.reset()
        if mode == 'annotation':
            self.open_dir_dialog()
        self.create_pollen_objects(mode)
        if self.images:
            self.show_image()
            self.show_thumbnails(mode)
            self.toggle_all_actions()
            self.actionSave.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.prevButton.setEnabled(False)
            self.actionPrevious.setEnabled(False)

    def load_images_from_google(self):
        self.reset()
        


    def create_pollen_objects(self, mode):
        if mode == "annotation":
            paths = glob.glob(f"{self.images_directory_path}/*.jp*g")
        elif mode == "review":
            paths = []
            for row in self.loaded_data:
                paths.append(row[1])
        for n, path in enumerate(paths):
            p = Pollen()
            p.path = path
            p.user = self.user
            p.is_senior = self.is_senior
            p.pixmap = QPixmap(path)
            try:
                p.get_image_metadata()
            except:
                print(f"No metadata at {path}")
            if mode == "review":
                p.annotation_id = self.loaded_data[n][0]
                p.previous_class = self.loaded_data[n][2]
                p.previous_confidence = self.loaded_data[n][3]
                p.previous_comment = self.loaded_data[n][4]
                p.previous_user = self.loaded_data[n][5]
                p.previous_is_senior = self.loaded_data[n][6]
                p.previous_timestamp = self.loaded_data[n][7]
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
        self.load_metadata_to_table()
        if not os.path.exists(self.current_pollen.path):
           self.pictureLabel_2.setText("Path Error. The current was not found on your system.")
           return
        current_image = self.images[self.index].pixmap
        self.scale_image(current_image, self.pictureLabel)
        self.scale_image(current_image, self.pictureLabel_2)

    def scale_image(self, image, label):
        size = label.size()
        scaled_image = image.scaled(size, aspectMode=Qt.KeepAspectRatio)
        label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        label.setPixmap(scaled_image)

    def load_metadata_to_table(self):
        metadata = self.current_pollen.metadata
        if not metadata:
            self.metadataTableWidget.clear()
            return
        self.metadataTableWidget.setRowCount(len(metadata))
        col = 0
        for k, v in metadata.items():
            self.metadataTableWidget.setItem(col, 0, QTableWidgetItem(str(k)))
            self.metadataTableWidget.setItem(col, 1, QTableWidgetItem(str(v)))
            col += 1        

    def show_thumbnails(self, mode):
        if mode == "annotation":
            paths = glob.glob(f"{self.images_directory_path}/*.jp*g")
        elif mode == "review":
            paths = []
            for row in self.loaded_data:
                paths.append(row[1])
        for n, path in enumerate(paths):
            image = QImage(path)
            item = preview(n, path, image)
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
        self.reset_inputs()
        self.show_image()
        if self.mode == "review":
            self.load_data_to_ui()

    def next(self):
        self.index += 1
        self.current_pollen = self.images[self.index]
        self._keep_in_range()
        self._set_style_sheet(self.current_pollen.labelled)
        self.reset_inputs()
        self.show_image()
        if self.mode == "review":
            self.load_data_to_ui()
    
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
            self.pictureLabel_2.setStyleSheet("background-color:rgb(89, 255, 103)")
            self.saveButton.setStyleSheet("background-color:rgb(89, 255, 103)")
            self.actionSave.setEnabled(False)
            self.saveButton.setEnabled(False)
        else:
            self.pictureLabel.setStyleSheet("background-color:rgb(216, 246, 255); font: 20pt 'SansSerif';")
            self.pictureLabel_2.setStyleSheet("background-color:rgb(216, 246, 255); font: 20pt 'SansSerif';")
            self.saveButton.setStyleSheet("")

    def _is_remaining(self):
        for pollen in self.images:
            if not pollen.labelled:
                return True
        return False
        
    def finished_folder(self):
        self.reset()
        QMessageBox.information(self, "Finished", "You have labelled all pictures in this folder.")


    def save(self):
        self.current_pollen.confidence = self.confidenceSlider.value()
        self.current_pollen.comment = self.commentEdit.text()
        if not self.save_to_db():
            QMessageBox.critical(self, "Database Error", "Could not write to database, plase try again or restart the application.")
            return
        if self.mode == "review":
            self.current_pollen.reviewer = self.user
            self.current_pollen.review_score = self.score_spinBox.value()
            self.current_pollen.review_comment = self.review_comment_lineEdit.text()
            try:
                self.save_review_to_db()
            except psycopg2.OperationalError or psycopg2.IntegrityError:
                QMessageBox.critical(self, "Database Error", "Could not write to database, plase try again or restart the application.")
        self.saved = True
        self.current_pollen.labelled = True
        self._set_style_sheet(True)
        print(self.current_pollen)
        if not self._is_remaining():
            self.finished_folder()

    def save_to_db(self):
        connection = Connection().connect
        cursor = connection.cursor()
        pollen_info = [self.current_pollen.path,
                       self.current_pollen.class_,
                       self.current_pollen.confidence,
                       self.current_pollen.comment,
                       self.current_pollen.user,
                       self.current_pollen.is_senior,
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        try:
            query = """INSERT INTO annotation (path, class, confidence, comment, username, senior, timestamp) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
            cursor.execute(query, pollen_info)
            connection.commit()
            connection.close()
            return True
        except psycopg2.OperationalError or psycopg2.IntegrityError:
            return False
        
    def save_review_to_db(self):
        connection = Connection().connect
        cursor = connection.cursor()
        review_info = [self.current_pollen.annotation_id,
                       self.current_pollen.review_score,
                       self.current_pollen.reviewer,
                       self.current_pollen.review_comment,
                       self.current_pollen.class_,
                       self.current_pollen.confidence,
                       self.current_pollen.comment,
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        try:
            query = 'INSERT INTO review (annotation_id, review_score, reviewer, review_comment, new_class, new_confidence, new_comment, timestamp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(query, review_info)
            connection.commit()
            connection.close()
            return True
        except psycopg2.OperationalError or psycopg2.IntegrityError:
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

    def reset_inputs(self):
        self.commentEdit.clear()
        self.review_comment_lineEdit.clear()
        self.confidenceSlider.setValue(5)
        self.score_spinBox.setValue(50)

    #########################################
    #               Review Page             #
    #########################################

    def tab_selected(self, tab_index):
        if tab_index == 0:
            self.mode = "annotation"
        elif tab_index == 1:
            self.mode = "review"
            self.add_names_to_combo()

    def add_names_to_combo(self):
        if self.names_loaded == True:
            return
        connection = Connection().connect
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT username FROM annotation")
        users = cursor.fetchall()
        for user in users:
            self.user_list_comboBox.addItem(user[0])
        connection.commit()
        connection.close()
        self.names_loaded = True

    def load_data_from_db(self):
        self.fetch_annotation()
        if not self.check_loaded():
            return
        self.load_data_to_ui()
        self.load_images(mode="review")

    def fetch_annotation(self):
        connection = Connection().connect
        cursor = connection.cursor()
        date_from = self.from_dateTimeEdit.dateTime().toPython().strftime("%Y-%m-%d %H:%M:%S")
        date_until = self.until_dateTimeEdit.dateTime().toPython().strftime("%Y-%m-%d %H:%M:S")
        user = self.user_list_comboBox.currentText()
        all_times = self.all_times_checkBox.isChecked()
        include_senior = self.include_senior_checkBox.isChecked()

        query_params_map = {
            (True, True, True): ("SELECT * FROM annotation", ()),
            (True, False, True): ("SELECT * FROM annotation WHERE senior = False", ()),
            (True, True, False): ("SELECT * FROM annotation WHERE timestamp BETWEEN %s AND %s", (date_from, date_until)),
            (True, False, False): ("SELECT * FROM annotation WHERE senior = False AND timestamp BETWEEN %s AND %s", (date_from, date_until)),
            (False, True, True): ("SELECT * FROM annotation WHERE username = %s", (user,)),
            (False, True, False): ("SELECT * FROM annotation WHERE username = %s AND timestamp BETWEEN %s AND %s", (user, date_from, date_until)),
            # Not Callable. When a name is selected, the Senior option should ALWAYS be True
            # (False, False, False): (f"SELECT * FROM annotation WHERE user = %s AND senior = 0 AND timestamp BETWEEN %s AND %s", (user, date_from, date_until)),
            # (False, False, True): (f"SELECT * FROM annotation WHERE user = %s AND senior = 0", (user,)),
        }

        query, params = query_params_map[(user == "All Users", include_senior, all_times)]
        print(query)
        print(params)
        cursor.execute(query, params)
        self.loaded_data = cursor.fetchall()
        connection.commit()
        connection.close()

    def check_loaded(self):
        if not self.loaded_data:
            QMessageBox.warning(self, "No record Found", "No record Found in the Database with the current filter.")
            return False
        return True

    def load_data_to_ui(self):
        self.lcdNumber.display(len(self.loaded_data))
        # pprint(self.loaded_data)
        self.annotation_id_label.setText(str(self.loaded_data[self.index][0]))
        self.path_label.setText(os.path.basename(self.loaded_data[self.index][1]))
        self.class_label.setText(self.loaded_data[self.index][2])
        self.confidence_label.setText(str(self.loaded_data[self.index][3]))
        self.comment_label.setText(self.loaded_data[self.index][4])
        self.user_label.setText(self.loaded_data[self.index][5])
        self.is_senior_label.setText("Senior" if self.loaded_data[self.index][6] == 1 else "Medior")
        self.timestamp_label.setText(str(self.loaded_data[self.index][7]))

    def all_times(self):
        checked = self.all_times_checkBox.isChecked()
        self.from_dateTimeEdit.setEnabled(not checked)
        self.until_dateTimeEdit.setEnabled(not checked)

    def user_selected(self, user):
        if user == "All Users":
            self.include_senior_checkBox.setEnabled(True)
        else:
            self.include_senior_checkBox.setChecked(True)
            self.include_senior_checkBox.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    app.exec()
