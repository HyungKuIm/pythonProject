# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radiobutton.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 515)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButton_python = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_python.setFont(font)
        self.radioButton_python.setObjectName("radioButton_python")

        self.radioButton_python.toggled.connect(self.radio_button)

        self.verticalLayout.addWidget(self.radioButton_python)
        self.radioButton_java = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_java.setFont(font)
        self.radioButton_java.setObjectName("radioButton_java")

        self.radioButton_java.toggled.connect(self.radio_button)

        self.verticalLayout.addWidget(self.radioButton_java)
        self.radioButton_c = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.radioButton_c.setFont(font)
        self.radioButton_c.setObjectName("radioButton_c")

        self.radioButton_c.toggled.connect(self.radio_button)

        self.verticalLayout.addWidget(self.radioButton_c)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_result)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def radio_button(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label_result.setText("you choose: {}".format(radio_btn.text()))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Choose Programming Language"))
        self.radioButton_python.setText(_translate("Form", "Python"))
        self.radioButton_java.setText(_translate("Form", "Java"))
        self.radioButton_c.setText(_translate("Form", "C++"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())