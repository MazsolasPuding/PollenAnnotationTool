from PySide6.QtWidgets import QApplication, QTreeWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QTreeWidgetItem

from Resources.ui_drive_dialog import Ui_DriveDialog
from Libs.google_drive import Drive


class DriveTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderLabels(['Name'])
        self.root_item = self.invisibleRootItem()

        

class DriveTreeDialog(QDialog ,Ui_DriveDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selected_folder = ''
        self.root_item = self.treeWidget.invisibleRootItem()
        
        drive = Drive()
        drive.fetch_all_items(self.root_item, '1UVoyWyg7XuaGbeyprWJuc0yWo9A1IzCN')

        self.selectButton.clicked.connect(self.select)
        self.cancelButton.clicked.connect(self.cancel)

    def cancel(self):
        self.close()

    def select(self):
        selected_items = self.treeWidget.selectedItems()
        selected_text_list = [item.text(0) for item in selected_items]
        self.selected_folder = selected_text_list[0]
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    dialog = DriveTreeDialog()
    dialog.show()
    app.exec()