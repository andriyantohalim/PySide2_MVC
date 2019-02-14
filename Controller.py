#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Controller.py

This file load the Controller from View.ui file and implement Controller.
View        : "View.ui" which consists of QPushButton and statusBar. Open with Qt Designer
Controller  : UpdateStatus which will change statusBar

"""


import sys
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets, QtCore

import Model
import random

class MyApp(QtWidgets.QMainWindow):

    def initUI(self, ui_file):
        uifile = QtCore.QFile(ui_file)
        uifile.open(QtCore.QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(uifile)
        uifile.close()

        self.window.pushButton.clicked.connect(self.UpdateStatus)
        self.window.setWindowTitle("View and Controller")
        self.window.show()

    def UpdateStatus(self):
        resp = "Andriyanto\t" + "Num: " + str(random.randint(1, 10))
        self.window.statusBar().showMessage(resp)

        c = Model.Simple()
        c.greeting(resp)

    def __init__(self, ui_file):
        super(MyApp, self).__init__()
        self.initUI(ui_file)


def main():
    app = QtWidgets.QApplication(sys.argv)
    myappl = MyApp("View.ui")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
