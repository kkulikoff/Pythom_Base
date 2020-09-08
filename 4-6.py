# task 6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)

my_count_func(start_number = int(input('Enter start number: ')), stop_number = int(input('Enter stop number: ')))

from itertools import cycle


def my_cycle_func(my_list, iteration):
    i = 0
    _iter = cycle(my_list)
    while i < iteration:
        print(next(_iter))
        i += 1


my_cycle_func(my_list = [1, 1.0, True, 'String'], iteration = int(input('Enter iteration: '))) 