# Task 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,
# выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def my_func():
    sum_res = 0
    some = True
    while some == True:
        user_number = input('Please enter the numbers or Q for quit - ').split()
        result = 0
        for element in range(len(user_number)):
            if user_number[element] == 'q' or user_number[element] == 'Q':
                some = False
                break
            else:
                result = result + int(user_number[element])
        sum_res = sum_res + result
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_func()
