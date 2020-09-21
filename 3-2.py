# Task 2
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, year, city, email, tel):
    print(name, surname, year, city, email, tel)

    
my_func(name = 'Anton', surname = 'Kulikov', year = '30', city = 'Taganrog', email = 'kulikoff.ab@yandex.ru', tel = '79123456789')
