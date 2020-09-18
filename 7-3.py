# Task 3
# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Organic():
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'{self.size}'

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size         
        
    def __mul__(self, other):
        return self.size * other.size

    def __truediv__(self, other):
        return int(self.size / other.size)

org_1 = Organic(10)
org_2 = Organic(20)

print('add:', org_1 + org_2)
print('sub:', org_2 - org_1)
print('mul:', org_1 * org_2)
print('div:', org_1 / org_2)