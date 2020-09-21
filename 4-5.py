# task 5
# Реализовать формирование списка, используя функцию range()
# и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def my_func(el_p, el):
    return el_p * el


values = [el for el in range(99, 1001) if el % 2 == 0]
multi_values = reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])
print(f'List of even values: {values}')
print(f'The result of multiplying all the elements of the list: {multi_values}')