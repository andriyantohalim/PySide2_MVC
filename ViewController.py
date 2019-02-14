#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

ViewController.py

This file implements view and controller in the same file.
View        : QPushButton and statusBar()
Controller  : StatusUpdate() which will change statusBar

"""

import sys
from PySide2 import QtWidgets

import Model


class ViewController(QtWidgets.QMainWindow):
    def initUI(self):
        btn = QtWidgets.QPushButton("Button", self)
        btn.setGeometry(100, 50, 100, 30)
        btn.clicked.connect(self.StatusUpdate)

        self.statusBar()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('View Controller')
        self.show()

    def StatusUpdate(self):
        resp = "Halim"
        self.statusBar().showMessage(resp)

        c = Model.Simple()
        c.greeting(resp)

    def __init__(self):
        super().__init__()
        self.initUI()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = ViewController()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
