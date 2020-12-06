import random


class GuessNumberLossOrMore:
    def __init__(self):  #не знаю зачем это тут
        pass  # оно да

    @staticmethod
    def win(c):  # функция проверяет вариант игрока и говорит выиграл ли он
        global num
        if c == num:
            print('You win!!!')
            return True
        print('Нет, попробуйте ещё')
        return False

    @staticmethod
    def more(c):  # проверка больше ли вводимое игроком число
        global num
        if c == num:
            return 'близко'
        return num > c

    @staticmethod
    def less(c):
        global num  # проверка меньше ли вводимое число
        if c == num:
            return 'близко'
        return num < c

    @classmethod
    def start_game(cls):
        global num
        guessed = False
        turn = 0
        print('Добро пожаловать в Угадай Число Больше и Меньше!')
        print('Ход типа\n= [число]\nсчитается за два')
        num = random.randint(0, 100)
        while True:
            print('Я загадал число от 0 до 100')
            print('Хочешь изменить промежуток? [y/n]')

            if input().lower() == 'y':
                num = random.randint(0, int(input('Введи новую границу от 0 до ')))

            print('Пжлста, вводи предположение так: ')
            print('> 50')
            print('Start!')

            while ~guessed:
                check = input()
                if check == 'check':
                    print(num)
                    guessed = True
                    break
                check = check.split()
                if len(check) == 2 and check[1].isdigit():
                    now = int(check[1])
                    if check[0] == '>':
                        print(cls.more(now))
                        turn += 1
                    elif check[0] == '<':
                        print(cls.less(now))
                        turn += 1
                    elif check[0] == '=':
                        so = cls.win(now)
                        turn += 2
                        guessed = so
                        if so:
                            turn -= 1
                            break
                elif check[0] == '666':  # маленькая пасхалка
                    print('____________$$$$$$$$$$$$$$$$$$$\n___________$$$$$$$$$$$$$$$$$$$$$$$\n________$$$$___$$$$$$$$$$$$$$$___$$$')
                    print('______$$$$______$$$$$$$$$$$$______$$$$\n____$$$$$________$$$$$$$$$$________$$$$\n___$$$$$__________$$$$$$$$___________$$$$')
                    print('__$$$$$____________$$$$$$____________$$$$$\n_$$$$$$____________$$$$$$$____________$$$$$\n_$$$$$$___________$$$$$$$$$___________$$$$$$')
                    print('_$$$$$$$_________$$$_$$$_$$$_________$$$$$$$\n_$$$$$$$$______$$$$___$___$$$$______$$$$$$$$\n_$$$$$$$$$$$$$$$$$___$$$___$$$$$$$$$$$$$$$$$')
                    print('_$$$_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_o$$\n_$$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__$$$\n__$$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__o$$$')
                    print('__$$o__$$__$$$$$$$$$$$$$$$$$$__$$_____o$$\n____$$o$____$$__$$$$$$__$$______$___o$$\n_____$$$o$__$____$$___$$___$$_____$$__o$')
                    print('______$$$$O$____$$____$$___$$ ____o$$$\n_________$$o$$___$$___$$___$$___o$$$\n___________$$$$o$o$o$o$o$o$o$o$$$$')
                    print('______________$$$$$$$$$$$$$$$$$$$\nА теперь вводи правильно!\n')
                else:
                    print('Неверно, давай ещё раз')
            print('Вы потратили', turn, 'ходов!')
            turn = 0
            print('Хотите сыграть ещё раз?[y/n]')
            if input().lower() == 'y':
                pass
            else:
                break


class GuessNumberHotCold:
    def __init__(self):
        pass

    @staticmethod
    def win(c):
        global num
        if c == num:
            print('You win!!!')
            return True
        print('Нет, попробуйте ещё')
        return False

    @classmethod
    def start_game(cls):
        global num
        guessed = False
        turn = 0
        radius = 100

        print('Добро пожаловать в Угадай Число Тепло-Холодно!')
        num = random.randint(0, 100)
        while True:
            print('Я загадал число от 0 до 100')
            print('Хочешь изменить промежуток?[y/n]')

            if input().lower() == 'y':
                radius = int(input('Введи новую границу от 0 до '))
                num = random.randint(0, radius)

            print('Пжлста, вводи предположение так: ')
            print('50')
            print('Если уверен в ответе то пиши:')
            print('= 49')
            print('Start!')

            while ~guessed:
                guessNum = input()
                while not(guessNum.isdigit()) and guessNum[0] != '=':
                    if guessNum == 'check':
                        print(num)
                        guessed = True
                        break
                    elif guessNum == 'гусь':
                        print('░░░░░░░░░░░░░░░░░░░░░▄▄▄░░░░\n░░░░░░░░░░░░░░░░░░░▄█████▄░░\n░░░░░░░░░░░░░░░░░░░████████▄')
                        print('░░░░░░░░░░░░░░░░░░░███░░░░░░\n░░░░░░░░░░░░░░░░░░░███░░░░░░\n░░░░░░░░░░░░░░░░░░░███░░░░░░')
                        print('░░░░░░░░░░░░░░░░░░░███░░░░░░\n░░░░░░░░░░░░░░░░░░░███░░░░░░\n░░░░░░░░░░░░░▄▄▄▄▄████░░░░░░')
                        print('░░░░░░░░▄▄████████████▄░░░░░\n░░░░▄▄██████████████████░░░░\n▄▄██████████████████████░░░░')
                        print('░▀▀████████████████████▀░░░░\n░░░░▀█████████████████▀░░░░░\n░░░░░░▀▀███████████▀▀░░░░░░░')
                        print('░░░░░░░░░▀███▀▀██▀░░░░░░░░░░\n░░░░░░░░░░█░░░░██░░░░░░░░░░░\n░░░░░░░░░░█░░░░█░░░░░░░░░░░░')
                        print('░░░▄▄▄▄███████▄███████▄▄▄▄░░')
                    print('Нужно ввести число!')
                    guessNum = input()
                if guessNum[0] == '=':
                    so = cls.win(int(guessNum[1:]))
                    turn += 1
                    guessed = so
                    if so:
                        break
                if len(guessNum.split(

                )) >= 2:
                    guessNum = int(guessNum[1:])
                else:
                    guessNum = int(guessNum)
                if num > guessNum:  # рассчитывает удаленность если число бота больше числа игрока
                    well = num - guessNum
                    if well >= radius // 2:
                        print('Холодно')
                    elif radius // 4 <= well < radius // 2:
                        print('Прохладно')
                    elif radius // 16 <= well < radius // 4:
                        print('Горячо')
                    elif well <= radius // 16:
                        print('Огонь близок')
                    elif well == num:
                        print('Горишь')
                    turn += 1
                elif num < guessNum:  # рассчитывает удаленность если число бота меньше числа игрока
                    well = guessNum - num
                    if well >= radius // 2:
                        print('Холодно')
                    elif radius // 4 <= well < radius // 2:
                        print('Прохладно')
                    elif radius // 16 <= well < radius // 4:
                        print('Горячо')
                    elif well <= radius // 16:
                        print('Огонь близок')
                    elif well == num:
                        print('Горишь')
                    turn += 1
                elif num == guessNum:
                    print('Вы выиграли!')
                    break

                else:
                    print('Неверно, давай ещё раз')
            print('Вы потратили', turn, 'ходов!')
            turn = 0
            print('Хотите сыграть ещё раз? [y/n]')
            if input().lower() == 'y':
                pass
            else:
                break
        num = 0


print('Привет, как хочешь играть?')
while True:
    print('> и < (1)')
    print('Горячо-Холодно (2)')
    print('выход [q]')
    want = input()
    while want != '1' and want != '2' and want != 'q':  # защита от дураков
        print('Такой вариант невозможен')
        want = input()
