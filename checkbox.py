# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(514, 409)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_chicken = QtWidgets.QCheckBox(Dialog)
        self.checkBox_chicken.setObjectName("checkBox_chicken")

        self.checkBox_chicken.stateChanged.connect(self.selected)

        self.verticalLayout.addWidget(self.checkBox_chicken)
        self.checkBox_fish = QtWidgets.QCheckBox(Dialog)
        self.checkBox_fish.setObjectName("checkBox_fish")

        self.checkBox_fish.stateChanged.connect(self.selected)

        self.verticalLayout.addWidget(self.checkBox_fish)
        self.checkBox_water = QtWidgets.QCheckBox(Dialog)
        self.checkBox_water.setObjectName("checkBox_water")

        self.checkBox_water.stateChanged.connect(self.selected)

        self.verticalLayout.addWidget(self.checkBox_water)
        self.checkBox_tea = QtWidgets.QCheckBox(Dialog)
        self.checkBox_tea.setObjectName("checkBox_tea")

        self.checkBox_tea.stateChanged.connect(self.selected)

        self.verticalLayout.addWidget(self.checkBox_tea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout_2.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def selected(self):
        price = 0
        if self.checkBox_chicken.isChecked():
            price = price + 3000

        if self.checkBox_fish.isChecked():
            price = price + 4000

        if self.checkBox_water.isChecked():
            price = price + 3000

        if self.checkBox_tea.isChecked():
            price = price + 3000

        self.label_result.setText("total price is: {}".format(price))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "choose food"))
        self.checkBox_chicken.setText(_translate("Dialog", "Chicken"))
        self.checkBox_fish.setText(_translate("Dialog", "fish"))
        self.checkBox_water.setText(_translate("Dialog", "water"))
        self.checkBox_tea.setText(_translate("Dialog", "tea"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())