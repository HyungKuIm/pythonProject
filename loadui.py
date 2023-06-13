import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class ui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)

        self.pushButton.clicked.connect(self.change_label)

    def change_label(self):
        self.label_result.setText("Hello label!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    sys.exit(app.exec())