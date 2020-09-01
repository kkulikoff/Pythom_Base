# task 5
# Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
user_number = ''
my_list = [7, 5, 3, 3, 2]
while user_number is not int:
    try:
        user_number = int(input('Enter a number: '))
        count = my_list.count(user_number)
        break
    except ValueError:
        print('Please enter a valid number: ')
print('You entered {}'.format(user_number))
for element in my_list:
    if count > 0:
        i = my_list.index(user_number)
        my_list.insert(i+count, user_number)
        break
    else:
        if user_number > element:
            j = my_list.index(element)
            my_list.insert(j, user_number)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
print(my_list)