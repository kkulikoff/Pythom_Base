# task 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
user_input = input('Please enter a few words separated by a space: ')
new_list = user_input.split(' ')
id_list = 0
number = 1
for i in new_list:
    print(f'{number}: {new_list[id_list][:10]}')
    id_list += 1
    number += 1