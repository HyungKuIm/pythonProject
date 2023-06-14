import sys

import cv2

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class ui(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('capture_screen.ui', self)
        self.logic = 0
        self.value = 1
        self.close = False
        self.SHOW.clicked.connect(self.onClicked)
        self.CAPTURE.clicked.connect(self.CaptureClicked)
        self.CLOSE.clicked.connect(self.CloseVideo)
        self.closeEvent = self.CloseVideo

    @pyqtSlot()
    def onClicked(self):
        cap = cv2.VideoCapture(0)  # 노트북일 경우 내장 카메라 0, 그다음 1

        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == True:
                print('here')
                self.displayImage(frame, 1)
                cv2.waitKey()

                if self.close == True:
                    break

                if (self.logic==2):
                    self.value = self.value + 1
                    cv2.imwrite('SavedImages/%s.png' % (self.value), frame)

                    self.logic = 1
            else:
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()
    @pyqtSlot()
    def CaptureClicked(self):
        self.logic = 2

    def CloseVideo(self):
        self.close = True

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.imglabel.setPixmap(QPixmap.fromImage(img))
        self.imglabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    sys.exit(app.exec())