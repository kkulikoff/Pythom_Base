# Task 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def my_func (*args):
    try:
        x = int(input("Enter x = "))
        y = int(input("Enter y = "))
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"


def to_fixed(numObj, digits=0):     
    return f"{numObj:.{digits}f}"
    
    
print(to_fixed(my_func(), 2))
