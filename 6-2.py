# Task 2
# Реализовать класс Road (дорога)
# в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500т

class Road:
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.weight = 25
        self.thickness = 5
        self.calculate()

    def calculate(self):
        self.full_weight = int((self.__length * self.__width * self.weight * self.thickness) / 1000)
        return print(f'{self.full_weight}т')
        
road = Road(20, 5000)