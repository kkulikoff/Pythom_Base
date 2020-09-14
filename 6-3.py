# Task 3
# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, wage, bonus):
        self.name = 'Михаил'
        self.surname = 'Валапасов'
        self.position = 'Крановщик'
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        self.full_name = f'{self.surname} {self.name}'
        return print(f'{self.full_name}\n{self.position}')

    def get_total_income(self):
        inp_wage = self._income['wage']
        inp_bonus = self._income['bonus']
        total_income = int(inp_wage) * (int(inp_bonus) / 100) + int(inp_wage)
        return print(f'Доход: {int(total_income)}')

employer = Position(input('Оклад в рублях: '), input('Премия в процентах: '))
employer.get_full_name()
employer.get_total_income()