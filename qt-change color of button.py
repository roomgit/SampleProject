# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *argv, **keywords ):
        super(MyMainWindow,self).__init__(*argv,**keywords)
        self.btn = QtWidgets.QPushButton('Button', self)
        self.btn.clicked.connect(self.changeColor)
        self.btn.move(20, 20)

    def changeColor(self):
        col = QtWidgets.QColorDialog.getColor()
        s = 'background-color: %s;' % col.name()
        self.btn.setStyleSheet(s)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()