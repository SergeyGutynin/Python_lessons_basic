#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import os
from random import randint

class Card():

    settings = {"cols": 9,
                "rows": 3,
                "step": 10,
                "digits": 5}
    min_val = 1
    max_val = 90

    def __init__(self, name):
        self.name = name
        self.values = self.generate()
        self.state = self.values
        self.closed_values = 0

    def generate(self):

        values = []

        for col_num in range(self.settings["cols"]):

            start = col_num*self.settings["step"]
            end = col_num*self.settings["step"]+self.settings["step"]-1

            if start < self.min_val:
                start = self.min_val

            if end == self.max_val-1:
                end = self.max_val

            count = self.settings["rows"]

            cols = []

            while count:

                val = randint(start, end)
                if val not in cols:
                    cols.append(val)
                    count -= 1

            values.append(cols)


        result = list(map(list,zip(*values)))

        for row in range(self.settings["rows"]):

            count = self.settings["cols"] - self.settings["digits"]

            remove_positions = []

            while count:
                position = randint(0, self.settings["cols"]-1)
                if position not in remove_positions:
                    remove_positions.append(position)
                    count -=1

            for ind in remove_positions:
                result[row][ind] = '  '

        self.state = result
        self.closed_values = 0

        return result


    def check_number(self, number):

        result = False

        for ri, row in enumerate(self.state):
            if number in row:
                self.closed_values +=1
                ci = self.state[ri].index(number)
                self.state[ri][ci] = '--'
                result = True
        return result

    def check_win(self):
        result = False
        if self.closed_values == self.settings['rows']*self.settings['digits']:
            result = True
        return result

    def print_card(self):
        self.print(self.values)

    def print_state(self):
        self.print(self.state)


    def print(self, value):
        out = f'-- {self.name} --\n'
        for row in value:
            for col in row:
                out += f'{str(col):2} '
            out += '\n'
        out += '----\n'
        print(out)

if __name__ == '__main__':

    my_card = Card('Ваша карточка')
    pc_card = Card('Карточка компьютера')


    finish = False
    values = []

    while not finish:

        pc_card.print_state()
        #print(pc_card.closed_values)
        my_card.print_state()
        #print(my_card.closed_values)
        check_failed = True

        value = 0

        min_val = 1
        max_val = 90

        while check_failed:
            value = randint(min_val, max_val)
            if value not in values:
                check_failed = False
                values.append(value)

        ostatok = max_val-len(values)

        print(f'Номер бочонка: {value} (осталось {ostatok})')

        user_check = my_card.check_number(value)
        pc_check = pc_card.check_number(value)

        user_win = my_card.check_win()
        pc_win = pc_card.check_win()

        user_in = input('Зачеркнуть цифру? (y/n)').lower()


        if user_in == 'y':
            if user_check:
                pass
            else:
                finish = True
        elif user_in == 'n':
            if user_check:
                finish = True
            else:
                pass
        else:
            finish = True

        if user_win:
            print('User win')
            finish = True

        if pc_win:
            print('PC win')
            finish = True

        if finish:
            print (f'В игре выпадали следующие номера {values}')

