# Task 4
# Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.


def my_func(x, y):
    return 1 / x ** y


print(int(my_func(5, -3)))


def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / x ** y
 
 
print(int(my_func2(int(input("First value: ")), int(input("Second value: ")))))
