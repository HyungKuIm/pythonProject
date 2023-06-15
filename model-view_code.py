import sys
from os import path

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class Model(qtc.QObject):

    error = qtc.pyqtSignal(str)  # 에러 처리를 위한 시그널

    # 파일처리(저장)을 위한 파일명, 내용을 받아서 저장하는 메소드
    def save(self, filename, content):
        print("save_called")
        error = ''
        if not filename:
            error = 'Filename empty'
        elif path.exists(filename):
            error = f'Will not overwrite {filename}'
        else:
            try:
                with open(filename, 'w', encoding='utf8') as fh:
                    fh.write(content)
            except Exception as e:
                error = f'Cannot write file: {e}'
        if error:
            self.error.emit(error)


class View(qtw.QWidget):

    submitted = qtc.pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.filename = qtw.QLineEdit()
        self.filecontent = qtw.QTextEdit()
        self.savebutton = qtw.QPushButton(
            'Save',
            clicked=self.submit
        )

        self.layout().addWidget(self.filename)
        self.layout().addWidget(self.filecontent)
        self.layout().addWidget(self.savebutton)

    def submit(self):
        filename = self.filename.text()
        filecontent = self.filecontent.toPlainText()
        self.submitted.emit(filename, filecontent)

    def show_error(self, error):
        qtw.QMessageBox.critical(None, 'Error', error)


class MainWindow(qtw.QMainWindow):

    def __init__(self):

        super().__init__()

        self.view = View()
        self.setCentralWidget(self.view)

        self.model = Model()

        self.view.submitted.connect(self.model.save)
        self.model.error.connect(self.view.show_error)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())