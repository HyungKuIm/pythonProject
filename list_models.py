import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QModelIndex


class FoodModel(qtc.QObject):

    def __init__(self):
        super().__init__()
        self.foods = self.getFoodList()

    def getFoodList(self):
        return [
            'Hamburger', 'Cheeseburger',
            'Chicken Nuggets', 'Hot Dog', 'Fish Sandwich'
        ]


class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.setLayout(qtw.QVBoxLayout())

        # data = [
        #     'Hamburger', 'Cheeseburger',
        #     'Chicken Nuggets', 'Hot Dog', 'Fish Sandwich'
        # ]
        foodModel = FoodModel()
        foodModel = qtc.QStringListModel(foodModel.foods)

        listview = qtw.QListView()
        listview.setModel(foodModel)
        model_combobox = qtw.QComboBox()
        model_combobox.setModel(foodModel)

        self.layout().addWidget(listview)
        self.layout().addWidget(model_combobox)

        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
