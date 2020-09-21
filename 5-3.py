# Task 3
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_dict = {}
low_employee = {}
with open("my_file_5-3.txt", encoding='utf-8') as my_file:
    for line in my_file:
        key, value = line.split()
        my_dict[key] = value
        if int(value) < 20000:
            low_employee[key] = value

for emp in low_employee:
    print(f'Сотрудник {emp} имеет величину оклада {low_employee.get(emp)}р., что составляет менее 20 тыс.')
emp_list = [int(item) for item in list(my_dict.values())]

print(f'Средняя зарплата сотрудников составляет: {int(sum(emp_list) / len(emp_list))}р.')
