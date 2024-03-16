import sys

from PyQt5 import QtWidgets
# from PyQt5.uic import loadUi
from design import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        # loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
