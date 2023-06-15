import sys
import cv2
import datetime
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore

class ui(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("RecordVideo.ui", self)

        self.logic = 0

        self.START.clicked.connect(self.STARTClicked)

        self.TEXT.setText('비디오를 녹화하시려면 "Start Recoding" 버튼을 누르세요')

        self.STOP.clicked.connect(self.STOPClicked)

    @pyqtSlot()
    def STARTClicked(self):
        self.logic = 1
        cap = cv2.VideoCapture(0)
        date = datetime.datetime.now()
        # filename, fourcc, fps, frameSize
        out = cv2.VideoWriter('videos/Video_%s%s%sT%s%s%s.mp4' %(date.year,date.month,date.day,date.hour,date.minute,date.second), -1, 20.0, (640, 480))
        Duration = self.Duration.toPlainText()
        duration = int(Duration)
        count = 0
        print('here')
        while (cap.isOpened()):

            date1 = datetime.datetime.now()
            if (((date1.second-date.second) >= 1) | ((date.second-date1.second) >= 1)):
                count = count + 1
                date = datetime.datetime.now()

                print(count)

            ret, frame = cap.read()
            if ret == True:

                self.displayImage(frame, 0)
                cv2.waitKey()

                if (self.logic == 1):
                    out.write(frame)

                    self.TEXT.setText('Vedeo 레코딩 시작')
                if (self.logic == 0):
                    self.TEXT.setText('Vedeo 레코딩 종료')

                    break

                if (count > duration):
                    self.TEXT.setText('Vedeo 레코딩 종료')

                    break
            else:
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()

    @pyqtSlot()
    def STOPClicked(self):
        self.logic = 0


    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(img))
        self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    sys.exit(app.exec())