# Task 1
# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("my_file_5-1.txt", "w", encoding='utf-8') as my_file:
    print('Введите данные поочерёдно, нажимая Enter. Для завершения программы введите "Выход"')
    data_input = '0'
    while True:
        if data_input == '':
            break
        else:
            data_input = input('Ввод данных: ')
            my_file.write(data_input)
            my_file.write('\n')
my_file = open("my_file_5-1.txt")
lines = my_file.readlines()
for line in lines:
    print(line, end='')