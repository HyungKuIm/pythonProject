import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication

import sounddevice as sd
from scipy.io.wavfile import write

class ui(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("RecordAudio.ui", self)
        self.Return = 0
        self.fs = 16000
        self.a = 0

        self.Text.setText('녹음을 하시려면 start recording 버튼을 클릭해 주세요')
        self.START.clicked.connect(self.STARTVOICERECORDING)

    @pyqtSlot()
    def STARTVOICERECORDING(self):
        Duration = int(self.Input.toPlainText())
        self.a = sd.rec(int(Duration*self.fs), self.fs, 1)
        sd.wait()

        write('output.wav', self.fs, self.a)

        self.Text.setText('레코딩 완료')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    try:
        sys.exit(app.exec())
    except:
        print('exiting')