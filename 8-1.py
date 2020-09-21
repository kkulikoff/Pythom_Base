# Task 1
'''
== Лото ==
Правила игры в лото.
Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
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
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
'''

from random import randint


class Loto:
    def __init__(self):
        self.bag = BarrelsBag()
        self.human = Human(input('Представьтесь: '))
        self.computer = Computer('Computer')

    def start(self):
        move_number = 0
        for barrel in self.bag:
            move_number += 1
            print(f'Ход {move_number}, в мешке осталось {len(self.bag)} бочонков')
            print(f'Выпал бочонок: {barrel}')
            print(f'Карточка игрока: {self.human.name}')
            self.human.print_card()
            print(f'Карточка игрока: {self.computer.name}')
            self.computer.print_card()
            if not self.human.move(barrel.number):
                print('--- GAME OVER ---')
                break
            if self.human.is_win():
                print(f'Player {self.human.name} победил!')
                break

            self.computer.move(barrel.number)
            if self.computer.is_win():
                print(f'Player {self.computer.name} победил!')
                break
        return


class BarrelsBag(list):
    def __init__(self):
        super().__init__()
        self.extend([Barrel(i + 1) for i in range(90)])

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        return self.pop(randint(1, len(self)) - 1)


class Barrel:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def print(self):
        print(f'{self.number}')


class Card:
    def __init__(self):
        numbers = []
        self.rows = []
        for i in range(3):
            self.rows.append([])
            for j in range(5):
                while True:
                    num = randint(1, 90)
                    if (num not in numbers) and (self.decade(num) not in [self.decade(k) for k in self.rows[i]]):
                        self.rows[i].append(num)
                        numbers.append(num)
                        break
            self.rows[i].sort()

    @staticmethod
    def decade(number):
        return abs(number) // 10 if abs(number) < 90 else 8

    def __contains__(self, item):
        for row in self.rows:
            for i in row:
                if item == i:
                    return True
        return False

    def cross_out(self, number):
        if number in self:
            for row in self.rows:
                if number in row:
                    index = row.index(number)
                    row[index] *= -1

    def print(self):
        print('----------------------------------------------')
        for row in self.rows:
            print_row = ['' for i in range(9)]
            for i in row:
                if i > 0:
                    print_row[self.decade(i)] = str(i)
                else:
                    print_row[self.decade(i)] = "-"
            print('| {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} |'.format(*print_row))
            print('----------------------------------------------')


class Player:
    def __init__(self, name):
        self.name = name    
        self.card = Card()  

    def print_card(self):
        self.card.print()

    def move(self, number):
        print(f'Ход игрока {self.name}...')

    def is_win(self):
        count = 0
        for row in self.card.rows:
            for item in row:
                if item < 0:
                    count += 1
        return count == 15


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def move(self, number):
        super().move(number)
        answer = ''
        while answer not in ['y', 'Y', 'n', 'N']:
            answer = input('Зачеркнуть цифру (y/n)?')
        print(f'Игрок {self.name} сделал свой ход')
        if (answer.lower() == 'n') and (number in self.card):
            print(f'За мухлёж игрок {self.name} дисквалифицирован!')
            return False
        if (answer.lower() == 'y') and (number not in self.card):
            print(f'За мухлёж игрок {self.name} дисквалифицирован!')
            return False
        self.card.cross_out(number)
        return True


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def move(self, number):
        super().move(number)
        if number in self.card:
            self.card.cross_out(number)
        print(f'Игрок {self.name} сделал свой ход')
        return True


loto = Loto()
loto.start()