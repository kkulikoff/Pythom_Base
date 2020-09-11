# Task 5
# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("my_file_5-5.txt", "w+", encoding='utf-8') as my_file:
    user_line = '10 20 30 40 99'
    my_file.writelines(user_line)
    user_numb = user_line.split()
    print(sum(map(int, user_numb)))