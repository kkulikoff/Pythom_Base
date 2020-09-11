# Task 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
my_list = []

with open("my_file_5-4.txt", encoding='utf-8') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        my_list.append(dict_translate[i[0]] + ' ' + i[1])

with open('new_my_file_5-4.txt', 'w+', encoding='utf-8' ) as new_my_file:
    new_my_file.writelines(my_list)