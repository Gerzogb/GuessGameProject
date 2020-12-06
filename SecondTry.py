import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.initUI()
        uic.loadUi('GameWindows.ui', self)

        self.settings_btn.clicked.connect(self.Test)

        self.back_btn = QPushButton(self)
        self.back_btn.resize(60, 60)
        self.back_btn.move(628, 500)
        self.back_btn.hide()
        self.back_btn.clicked.connect(self.back_to_menu)

        # объекты для больше-меньше
        self.instruction = QLabel(self)
        self.instruction.setText('Вводите своё предпололжение в виде "> 50"')
        self.instruction.setFont(QFont('Times', 12))
        self.instruction.move(50, 80)
        self.instruction.hide()

        self.LessMore_btn.clicked.connect(self.less_more_game)
        self.inputGuess = QLineEdit(self)
        self.inputGuess.resize(80, 20)
        self.inputGuess.move(50, 140)
        self.inputGuess.hide()

        # различные переменные для игры:
        radius = 100


    def Test(self):
        # да, это ужасный вариант
        self.MenuLabel.hide()
        self.ColdWarm_btn.hide()
        self.LessMore_btn.hide()
        self.settings_btn.hide()
        self.back_btn.show()

    def back_to_menu(self):
        self.MenuLabel.show()
        self.ColdWarm_btn.show()
        self.LessMore_btn.show()
        self.settings_btn.show()
        self.back_btn.hide()

    def less_more_game(self):
        self.MenuLabel.move(20, 20)
        self.MenuLabel.resize(610, 40)
        self.MenuLabel.setFont(QFont('Times', 15))
        self.MenuLabel.setText('Добро пожаловать в Угадай Число Больше и Меньше!')
        self.instruction.show()
        self.inputGuess.show()

        self.ColdWarm_btn.hide()
        self.LessMore_btn.hide()
        self.settings_btn.hide()


    def initUI(self):
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('Угадай число')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())