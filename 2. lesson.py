import sys
from PyQt5 import QtWidgets,QtGui


def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("first class")
    sticker1 = QtWidgets.QLabel(window)
    sticker1.setText("Hello from lesson 2")
    sticker2 = QtWidgets.QLabel(window)
    sticker2.setPixmap(QtGui.QPixmap("firstphoto.jpg"))
    sticker1.move(260,50)
    sticker2.move(95,80)
    button = QtWidgets.QPushButton(window)
    button.setText("BUTTON")
    button.move(300,400)


    window.setGeometry(100,200,600,600)
    window.show()
    sys.exit(app.exec_())

Window()