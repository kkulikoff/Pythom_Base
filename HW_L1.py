#  Hello teacher.
#  I'm starting my homework №1.
#  I think you will like my work.
#  Best wishes, Anton Kulikov. 

#  task 1
#  Поработайте с переменными, создайте несколько, выведите на экран.
#  запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print('Task №1 starting...')
print(' ')
_int_var = 5
print(_int_var)
print(f'{_int_var} is a {type(_int_var)}')
print(' ')

_float_var = 5.0
print(_float_var)
print(f'{_float_var} is a {type(_float_var)}')
print(' ')

_string_var = 'string'
print(_string_var)
print(f'{_string_var} is a {type(_string_var)}')
print(' ')

_list_var = [5, 5.0, 'string']
print(_list_var)
print(f'{_list_var} is a {type(_list_var)}')
print(' ')

_bunch_var = {1, 2, 3, 4, 5}
print(_bunch_var)
print(f'{_bunch_var} is a {type(_bunch_var)}')
print(' ')

_bool_var = True
print(_bool_var)
print(f'{_bool_var} is a {type(_bool_var)}')
print(' ')

_none_var = None
print(_none_var)
print(f'{_none_var} is a {type(_none_var)}')
print(' ')

user_int_var = int(input('Please, enter the number: '))
user_string_var = input('Please, enter the text: ')
print(f'You enter {user_int_var} and {user_string_var}')
print(f'{user_int_var} in squared will be {user_int_var ** 2}')
print(f'When multiplying a string by a number, the string is concatenated. Example: {user_string_var}*2 will be >>> {user_string_var * 2} <<<')
print(' ')

#  task 2
#  Пользователь вводит время в секундах.
#  Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
#  Используйте форматирование строк.
print('Task №2 starting...')
print(' ')
question_time_sec = int(input('Please, enter the time in seconds: '))
hours = question_time_sec // 3600
minutes = (question_time_sec - (hours * 3600)) // 60
seconds = (question_time_sec - (hours * 3600) - (minutes * 60))
print(' ')
print('Answer task #2')
print(f'Time in format HH:MM:SS - {hours}:{minutes}:{seconds}')
print(' ')

#  task 3
#  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('Task №3 starting...')
print(' ')
number_n = input('Please, enter the number: ')
number_one = int(number_n)
number_two = number_n*2
number_two = int(number_two)
number_three = number_n*3
number_three = int(number_three)
number_x = number_one + number_two + number_three
print(f'You enter a number: N = {number_n}. The assignment condition has the form: "N = n + nn + nnn"')
print(f'Solution of the task "N = n + nn + nnn" >>> N = {number_one} + {number_two} + {number_three} = {number_x}')
print(' ')

#  task 4
#  Пользователь вводит целое положительное число.
#  Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.
print('Task №4 starting...')
print(' ')
user_integer = int(input('Please, enter the number: '))
user_list = []
while user_integer > 10:
    user_list.append(user_integer % 10)
    #  print(user_list)
    user_integer //= 10
    #  print(user_integer)
result = max(user_list)
print(f'The largest digit in the entered number is: {result}.')
print(' ')

#  task 5
#  Запросите у пользователя значения выручки и издержек фирмы.
#  Определите, с каким финансовым результатом работает фирма
#  (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#  Выведите соответствующее сообщение.
#  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#  Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('Task №5 starting...')
print(' ')
def toFixed(numObj, digits=0):     #  Украдено с интернета для
    return f"{numObj:.{digits}f}"  #  сокращения знаков после запятых

income = int(input('Please, enter income value: '))
cost = int(input('Please, enter cost value: '))
if income > cost:
    print('Profit. Income is greater than costs.')
elif income < cost:
    print('Defeat. The cost is more than the income.')
rent = ((income - cost) / income) * 100
print(f"The company's profitability is {toFixed(rent, 1)}%")
employers = int(input('Please, enter the number of employers in your company: '))
rent_emp = rent / employers
print(f'Each employee brought the company the same income {toFixed(rent_emp, 1)}')
print(' ')

#  task 6
#  Спортсмен занимается ежедневными пробежками.
#  В первый день его результат составил a километров.
#  Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#  Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
#  Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = int(input("Please, enter your first day run results: "))
b = int(input("Please, enter the overall desired result: "))
days = 1
distance = a
while distance < b:
    a = a + 0.1 * a
    # print(a)
    days += 1
    # print(days)
    distance = distance + a
    # print(distance)
print(f'You will reach the required indicators on day {days}')

######################################################################
#                                                                    #
#  ##################     #################     #################### #
#  ##################     #################     #################### #
#  ##### THANK'S ####     ###### FOR ######     ##### WATCHING ##### #
#  ##################     #################     #################### #
#  ##################     #################     #################### #
#                                                                    #
######################################################################