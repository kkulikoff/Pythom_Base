# task 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
my_list = ['Winter', 'Spring', 'Summer', 'Autumn']
my_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
user_input = int(input('Please enter the month number: '))
if user_input == 12 or user_input == 1 or user_input == 2:
    print(f'Season of this month: {my_list[0]}')
    print(f'Season of this month: {my_dict.get(1)}')
elif user_input == 3 or user_input == 4 or user_input == 5:
    print(f'Season of this month: {my_list[1]}')
    print(f'Season of this month: {my_dict.get(2)}')
elif user_input == 6 or user_input == 7 or user_input == 8:
    print(f'Season of this month: {my_list[2]}')
    print(f'Season of this month: {my_dict.get(3)}')
elif user_input == 9 or user_input == 10 or user_input == 11:
    print(f'Season of this month: {my_list[3]}')
    print(f'Season of this month: {my_dict.get(4)}')