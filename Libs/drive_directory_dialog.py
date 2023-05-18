from PySide6.QtWidgets import QApplication, QTreeWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog

from Libs.google_drive import Drive


class DriveTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderLabels(['Name'])
        self.root_item = self.invisibleRootItem()

        drive = Drive()
        drive.fetch_all_items(self.root_item, '1UVoyWyg7XuaGbeyprWJuc0yWo9A1IzCN')

class DriveTreeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.selectButton = QPushButton('Select')
        self.cancelButton = QPushButton('Cancel')
        self.selected_folder = ''

        self.selectButton.clicked.connect(self.select)
        self.cancelButton.clicked.connect(self.cancel)

        self.tree_widget = DriveTreeWidget(self)
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.selectButton)
        horizontal_layout.addWidget(self.cancelButton)
        vertical_layout.addWidget(self.tree_widget)
        vertical_layout.addLayout(horizontal_layout)
        self.setLayout(vertical_layout)

    def cancel(self):
        self.close()

    def select(self):
        selected_items = self.tree_widget.selectedItems()
        selected_text_list = [item.text(0) for item in selected_items]
        self.selected_folder = selected_text_list[0]
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    dialog = DriveTreeDialog()
    dialog.show()
    app.exec()