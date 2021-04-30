import sys
from PyQt5 import QtWidgets

import requests
import random

from bs4 import BeautifulSoup

class Window(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.text_area = QtWidgets.QLabel("")
        self.setGeometry(100, 100, 500, 400)
        self.button = QtWidgets.QPushButton("New Movie")
        self.setWindowTitle("New Day New Movie")
        self.url = "http://www.imdb.com/chart/top"
        self.response = requests.get(self.url)
        self.list = list()
        self.list2 = list()
        self.html_icerigi = self.response.content

        self.soup = BeautifulSoup(self.html_icerigi, "html.parser")
        self.basliklar = self.soup.find_all("td", {"class": "titleColumn"})
        self.ratingler = self.soup.find_all("td", {"class", "ratingColumn imdbRating"})

        for baslik, rating in zip(self.basliklar, self.ratingler):
            baslik = baslik.text
            rating = rating.text

            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")
            self.list.append(baslik)
            self.list2.append(rating)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.button)



        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)

        self.show()

    def click(self):
        randomx = random.randint(0, len(self.list) - 1)
        self.text_area.setText("Movie of the day\n{}".format(self.list[randomx]))










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window1 = Window()



    sys.exit(app.exec_())
