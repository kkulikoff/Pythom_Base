# Task 1
# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.


from sys import argv
name, out_in_hours, rate_in_hours, prize = argv


def salary_calc (out_in_hours, rate_in_hours, prize):
    try:
        salary = (out_in_hours * rate_in_hours) + prize
        print(f'Employee salary is: {salary}')
    except NameError:
        print('Nope... Not a number!')
    except ValueError:
        print('Nope... Not a number!')
    except TypeError:
        print('Nope... Not a number!')
        
        
salary_calc(168, 2000, 15000)