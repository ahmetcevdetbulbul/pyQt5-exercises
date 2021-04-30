import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sqlite3


class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
        self.connect()
    def  connect(self):
        con = sqlite3.connect("database.db")

        self.cursor = con.cursor()

        self.cursor.execute("Create Table If not exists users (user_name TEXT,password TEXT)")
        con.commit()

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_in = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")
        self.setWindowTitle("User Login")
        self.setGeometry(100,100,900,700)
        self.label = QLabel(self)
        self.pixmap = QPixmap('secondphoto.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())



        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.log_in)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.log_in.clicked.connect(self.login)

        self.show()

    def login(self):
        name = self.user_name.text()
        pas = self.password.text()

        self.cursor.execute("Select * From users where user_name = ? and password = ?",(name,pas))

        data = self.cursor.fetchall()


        if len(data) == 0:
            self.text_area.setText("Please try again")
        else:
            self.text_area.setText("Welcome "+name)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window1 = Window()



    sys.exit(app.exec_())
