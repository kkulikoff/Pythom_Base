# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
count_elements = int(input('Please enter the max counts elements in list: '))
user_count = 1
num_element = 1
while user_count <= count_elements:
    element_input = input(f'Please enter element value #{num_element}: ')
    my_list.append(element_input)
    user_count += 1
    num_element += 1
print(f'You enter next value >>> {my_list}')
user_list_id = 0
for element in range(int(len(my_list)/2)):
    my_list[user_list_id], my_list[user_list_id + 1] = my_list [user_list_id + 1], my_list[user_list_id]
    user_list_id += 2
print(f'Result >>> {my_list}')