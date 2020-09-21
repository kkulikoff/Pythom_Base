# Task 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    
    my_list = [arg1, arg2, arg3]
    new_my_list = []
    
    max_arg1 = max(my_list)
    new_my_list.append(max_arg1)
    my_list.remove(max_arg1)

    max_arg2 = max(my_list)
    new_my_list.append(max_arg2)
    my_list.remove(max_arg2)

    result = sum(new_my_list)
    print(result)


my_func(3, 4, 5)
