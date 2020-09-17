# Task 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_count_coat(self):
        count = round((self.width / 6.5 + 0.5), 2)
        return count

    def get_count_costume(self):
        count = round((self.height * 2 + 0.3), 2)
        return count

    @property
    def get_count_total(self):
        total = str(f'Общий расход ткани: {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')
        return total


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.count_coat = round((self.width / 6.5 + 0.5), 2)

    def __str__(self):
        total =  f'Расход ткани на пальто: {self.count_coat}'
        return total


class Costume(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.count_costume = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        total = f'Расход ткани на костюм: {self.count_costume}'
        return total

coat = Coat(10, 20)
costume = Costume(10, 20)

print(coat)
print(costume)
print(coat.get_count_total)
print(coat.get_count_coat())
print(coat.get_count_costume())
print(costume.get_count_total)
print(costume.get_count_coat())
print(costume.get_count_costume())