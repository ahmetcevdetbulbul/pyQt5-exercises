import sys
from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Lesson 4")
    okey = QtWidgets.QPushButton("Okey")
    cancel = QtWidgets.QPushButton("Cancel")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okey)
    h_box.addStretch()
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    #v_box.addWidget(okey)
    #v_box.addWidget(cancel)
    v_box.addStretch()
    v_box.addLayout(h_box)


    window.setLayout(v_box)
    window.setGeometry(100, 100, 500, 500)
    window.show()
    sys.exit(app.exec_())

Window()