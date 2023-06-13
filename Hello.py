from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

first_window = QtWidgets.QWidget()

first_window.resize(400, 300)

first_window.setWindowTitle("The first pyqt program")

first_window.show()

sys.exit(app.exec())