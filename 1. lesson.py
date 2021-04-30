import sys
from PyQt5 import QtWidgets


def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("first class")
    window.show()
    sys.exit(app.exec_())

Window()