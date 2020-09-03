# Task 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"


def to_fixed(numObj, digits=0):     
    return f"{numObj:.{digits}f}"
    
    
result = (my_func(int(input("Enter x = ")), int(input("Enter y = "))))
print(to_fixed(result, 2))