# task 1
# Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for el, num in zip(old_list, old_list[1:]) if num > el]
print(new_list)