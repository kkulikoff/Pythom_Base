# Task 4
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool

    def show_speed(self):
        return print(f'Текущая скорость автомобиля {self.name} составляет {self.speed}км/ч')
    
    def go(self):
        return print(f'{self.name} в движении')
  
    def stop(self):
        return print(f'{self.name} остановлена')
  
    def turn_left(self):
        return print(f'{self.name} повернула налево')
  
    def turn_right(self):
        return print(f'{self.name} повернула направо')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
        self.show_speed()
  
    def show_speed(self):
        if self.speed > 60:
        print ('Превышение скорости свыше 60 км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
        self.show_speed()
  
    def show_speed(self):
        if self.speed > 40:
        print ('Превышение скорости свыше 40 км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = bool):
        super().__init__(speed, color, name, is_police)
        self.is_police = True
        self.police()
  
    def police(self):
        if self.is_police == True:
        print('Это полицейская машина')


lincoln = TownCar(89, 'asphalt', 'Lincoln')
print(f'Название авто: {lincoln.name}, цвет: {lincoln.color}, текущая скорость: {lincoln.speed}км/ч')
lincoln.go()
lincoln.turn_left()
lincoln.stop()

print('')

porsche = SportCar(210, 'белый', 'Porsche')
print(f'Название авто: {porsche.name}, цвет: {porsche.color}, текущая скорость: {porsche.speed}км/ч')
porsche.go()
porsche.turn_right()
porsche.stop()

print('')

kamaz = WorkCar(45, 'красный', 'КаМАЗ')
print(f'Название авто: {kamaz.name}, цвет: {kamaz.color}, текущая скорость: {kamaz.speed}км/ч')
kamaz.go()
kamaz.show_speed()
kamaz.stop()

print('')

audi = PoliceCar(90, 'черно-белый', 'Audi')
print(f'Название авто: {audi.name}, цвет: {audi.color}, текущая скорость: {audi.speed}км/ч')
audi.go()
audi.show_speed()
audi.stop()