
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide2 import QtGui

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.button = QPushButton('Hello', self)
        #self.label = QLabel("Hello World")
        #label.show()
        icon = QtGui.QIcon("happy.gif")
        self.button.setIcon(icon)
        # トグル式にする
        #self.button.setCheckable(True)
        # シグナル・スロットの設定
        self.button.pressed.connect(self.slot_button_pressed)
        self.button.released.connect(self.slot_button_released)

    def slot_button_pressed(self):
        """ ボタンが押されたときのスロット """

        self.button.setText('Pressed')

    def slot_button_released(self):
        """ ボタンが話されたときのスロット """

        self.button.setText('Released')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())