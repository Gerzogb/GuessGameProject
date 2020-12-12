import sys
from random import randint
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QPlainTextEdit
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.initUI()
        uic.loadUi('GameWindows.ui', self)

        self.settings_btn.clicked.connect(self.settings)
        # кнопка возвращения в меню
        self.back_btn = QPushButton(self)
        self.back_btn.resize(60, 60)
        self.back_btn.move(628, 500)
        self.back_btn.setText('В меню')
        self.back_btn.clicked.connect(self.back_to_menu)

        self.again_btn = QPushButton(self)
        self.again_btn.setText('Ещё раз')
        self.again_btn.resize(60, 60)
        self.again_btn.move(560, 500)
        self.again_btn.hide()
        self.again_btn.clicked.connect(self.restart_game)

        self.change_radius = QLineEdit(self)
        self.change_radius.resize(80, 20)
        self.change_radius.move(50, 140)
        self.change_radius.hide()

        self.change_btn = QPushButton(self)
        self.change_btn.setText('изменить')
        self.change_btn.resize(80, 50)
        self.change_btn.move(50, 165)
        self.change_btn.hide()
        self.change_btn.clicked.connect(self.new_radius)

        self.now_settings = QPlainTextEdit(self)
        self.now_settings.setEnabled(False)
        self.now_settings.resize(300, 200)
        self.now_settings.move(200, 140)
        self.now_settings.hide()

        # объекты для больше-меньше
        # BUTTONS
        self.instruction = QLabel(self)
        self.instruction.setText('Вводите своё предпололжение в виде числа без другиз знаков')
        self.instruction.setFont(QFont('Times', 12))
        self.instruction.move(50, 80)
        self.instruction.hide()

        self.NameMoreLess = QLabel(self)

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
        #надо было капсом делать все
        self.radius = 100
        self.num_guess = randint(0, self.radius)
        self.moves = 0
        con = sqlite3.connect('gamer_stats.db')
        self.cur = con.cursor()
        self.max_moves = self.cur.execute('''SELECT max FROM stats''').fetchall()
        self.min_moves = self.cur.execute('''SELECT min FROM stats''').fetchall()
        self.wins = self.cur.execute('''SELECT wins FROM stats''').fetchall()
        self.loses = self.cur.execute('''SELECT loses FROM stats''').fetchall()

    def settings(self):
        # да, это ужасный вариант
        self.MenuLabel.hide()
        self.ColdWarm_btn.hide()
        self.LessMore_btn.hide()
        self.settings_btn.hide()

        self.back_btn.show()
        self.change_radius.show()
        self.change_btn.show()
        self.now_settings.show()

    def new_radius(self):
        self.radius = int(self.change_radius.text())
        self.num_guess = randint(0, self.radius)
        self.max_moves = self.cur.execute('''SELECT max FROM stats''').fetchall()
        self.min_moves = self.cur.execute('''SELECT min FROM stats''').fetchall()
        self.wins = self.cur.execute('''SELECT wins FROM stats''').fetchall()
        self.loses = self.cur.execute('''SELECT loses FROM stats''').fetchall()
        self.now_settings.setPlainText(f'Случайное число от 0 до {str(self.radius)}\n'
                                       f'Колчиество побед:{str(self.wins[0][0])}\n'
                                       f'Самое минимальное кол-во ходов:{str(self.min_moves[0][0])}\n'
                                       f'Самое максимальное кол-во ходов:{str(self.max_moves[0][0])}\n')
        print('удачное изменение')

    def back_to_menu(self):
        self.MenuLabel.show()
        self.ColdWarm_btn.show()
        self.LessMore_btn.show()
        self.settings_btn.show()

        self.instruction.hide()
        self.more_btn.hide()
        self.less_btn.hide()
        self.equal_btn.hide()
        self.answer.hide()
        self.inputGuess.hide()
        self.change_radius.hide()
        self.change_btn.hide()
        self.NameMoreLess.hide()
        self.now_settings.hide()
        self.again_btn.hide()

    def restart_game(self):
        self.answer.setPlainText('')
        self.num_guess = randint(0, self.radius)
        self.inputGuess.setText('')
        self.again_btn.hide()

    def less_more_game(self):
        self.MenuLabel.hide()

        self.NameMoreLess.move(20, 20)
        self.NameMoreLess.resize(610, 40)
        self.NameMoreLess.setFont(QFont('Times', 15))
        self.NameMoreLess.setText('Добро пожаловать в Угадай Число Больше и Меньше!')

        self.answer.setPlainText('За догадку > или < дается 0.5\n'
                                 'За догадку = дается 1.0')

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
        inputGuess = self.inputGuess.text()
        if inputGuess.isdigit():
            inputGuess = int(self.inputGuess.text())
            answer = self.num_guess > inputGuess
            self.moves += 0.5
            if answer:
                self.answer.setPlainText('Да, число больше')
            else:
                self.answer.setPlainText('Нет, число меньше')
        else:
            self.answer.setPlainText('Некорректный ввод')

    def is_less(self):
        self.instruction.hide()
        inputGuess = self.inputGuess.text()
        if inputGuess.isdigit():
            inputGuess = int(self.inputGuess.text())
            answer = self.num_guess < inputGuess
            self.moves += 0.5
            if answer:
                self.answer.setPlainText('Да, число меньше')
            else:
                self.answer.setPlainText('Нет, число больше')
        else:
            self.answer.setPlainText('Некорректный ввод')

    def is_equal(self):
        self.instruction.hide()
        inputGuess = self.inputGuess.text()

        if inputGuess.isdigit():
            self.moves += 1.0
            inputGuess = int(self.inputGuess.text())
            answer = self.num_guess == inputGuess

            if answer:
                self.answer.setPlainText('Йухуу, число угадано!!')
                con = sqlite3.connect('gamer_stats.db')
                cur = con.cursor()
                if self.moves > self.max_moves[0][0]:
                    print(self.max_moves[0][0])
                    cur.execute(f"""UPDATE stats SET max={str(self.moves)}""")
                if self.moves < self.min_moves[0][0]:
                    print(self.min_moves[0][0])
                    cur.execute(f"""UPDATE stats SET max={str(self.moves)}""")
                now = self.wins[0][0] + 1
                cur.execute(f'''UPDATE stats SET wins={str(now)}''')
                con.commit()
                self.back_btn.show()
                self.again_btn.show()
                self.back_btn.clicked.connect(self.back_to_menu)
                self.moves = 0
            else:
                self.answer.setPlainText('Нет, попробуй ещё раз')
        else:
            self.answer.setPlainText('Некорректный ввод')
    # конец функций кнопок

    def initUI(self):
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('Угадай число')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()

    sys.exit(app.exec())
