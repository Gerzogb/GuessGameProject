import sys
from random import randint
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QPlainTextEdit
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.initUI()
        uic.loadUi('GameWindows.ui', self)

        self.settings_btn.clicked.connect(self.Test)
        # кнопка возвращени в меню
        self.back_btn = QPushButton(self)
        self.back_btn.resize(60, 60)
        self.back_btn.move(628, 500)
        self.back_btn.hide()
        self.back_btn.clicked.connect(self.back_to_menu)

        # объекты для больше-меньше
        # BUTTONS
        self.instruction = QLabel(self)
        self.instruction.setText('Вводите своё предпололжение в виде числа без другиз знаков')
        self.instruction.setFont(QFont('Times', 12))
        self.instruction.move(50, 80)
        self.instruction.hide()

        self.more_btn = QPushButton(self)
        self.more_btn.resize(60, 60)
        self.more_btn.setText('>')
        self.more_btn.move(140, 140)
        self.more_btn.clicked.connect(self.is_more)
        self.more_btn.hide()

        self.less_btn = QPushButton(self)
        self.less_btn.resize(60, 60)
        self.less_btn.setText('<')
        self.less_btn.move(140, 200)
        self.less_btn.clicked.connect(self.is_less)
        self.less_btn.hide()

        self.equal_btn = QPushButton(self)
        self.equal_btn.resize(60, 60)
        self.equal_btn.setText('=')
        self.equal_btn.move(140, 260)
        self.equal_btn.clicked.connect(self.is_equal)
        self.equal_btn.hide()

        # output and input
        self.answer = QPlainTextEdit(self)
        self.answer.setEnabled(False)
        self.answer.resize(150, 150)
        self.answer.move(220, 140)
        self.answer.hide()

        self.LessMore_btn.clicked.connect(self.less_more_game)
        self.inputGuess = QLineEdit(self)
        self.inputGuess.resize(80, 20)
        self.inputGuess.move(50, 140)
        self.inputGuess.hide()

        # различные переменные для игры:
        radius = 100
        self.num_guess = randint(0, radius)


    def Test(self):
        # да, это ужасный вариант
        self.MenuLabel.hide()
        self.ColdWarm_btn.hide()
        self.LessMore_btn.hide()
        self.settings_btn.hide()
        self.back_btn.show()

    def back_to_menu(self):
        self.MenuLabel.setText('МЕНЮ')
        self.MenuLabel.show()
        self.ColdWarm_btn.show()
        self.LessMore_btn.show()
        self.settings_btn.show()
        self.back_btn.hide()

        self.instruction.hide()
        self.more_btn.hide()
        self.less_btn.hide()
        self.equal_btn.hide()
        self.answer.hide()
        self.inputGuess.hide()

    def less_more_game(self):
        self.MenuLabel.move(20, 20)
        self.MenuLabel.resize(610, 40)
        self.MenuLabel.setFont(QFont('Times', 15))
        self.MenuLabel.setText('Добро пожаловать в Угадай Число Больше и Меньше!')

        self.more_btn.show()
        self.less_btn.show()
        self.equal_btn.show()
        self.answer.show()
        self.instruction.show()
        self.inputGuess.show()

        self.ColdWarm_btn.hide()
        self.LessMore_btn.hide()
        self.settings_btn.hide()

    #функции кнопок больше-меньше
    def is_more(self):
        self.instruction.hide()
        inputGuess = int(self.inputGuess.text())
        answer = self.num_guess > inputGuess
        if answer:  # запихай в try чтобы избежать ПУСТОЙ СТРОКИ, НЕ ЧИСЛА, ДРОБИ
            self.answer.setPlainText('Да, число больше')
        else:
            self.answer.setPlainText('Нет, число меньше')

    def is_less(self):
        self.instruction.hide()
        inputGuess = int(self.inputGuess.text())
        answer = self.num_guess < inputGuess
        if answer:  # запихай в try чтобы избежать ПУСТОЙ СТРОКИ, НЕ ЧИСЛА, ДРОБИ
            self.answer.setPlainText('Да, число меньше')
        else:
            self.answer.setPlainText('Нет, число больше')

    def is_equal(self):
        self.instruction.hide()
        inputGuess = int(self.inputGuess.text())
        answer = self.num_guess == inputGuess
        if answer:  # запихай в try чтобы избежать ПУСТОЙ СТРОКИ, НЕ ЧИСЛА, ДРОБИ
            self.answer.setPlainText('Йухуу, число угадано!!')
            self.back_btn.show()
            self.back_btn.clicked.connect(self.back_to_menu)
        else:
            self.answer.setPlainText('Нет, попробуй ещё раз')


    def initUI(self):
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('Угадай число')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())