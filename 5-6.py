# Task 6
# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему.
# Вывести словарь на экран.

def brute_force(val):
    num_list = []
    num = ''
    for char in val:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list


activities = {}
new_activities = {}
with open('my_file_5-6.txt', 'r') as my_file:
    for line in my_file:
        key, *value = line.split()
        activities[key] = value

storage = 0

for dig in activities['Comp_science:']:
    a = brute_force(dig)
    a_int = a[0]
    storage += a_int
new_activities['Comp_science:'] = storage
    
for dig in activities['Physics:']:
    a = brute_force(dig)
    a_int = a[0]
    storage += a_int
new_activities['Physics:'] = storage
print(new_activities)
    
for dig in activities['Physics_edu:']:
    a = brute_force(dig)
    a_int = a[0]
    storage += a_int
new_activities['Physics_edu:'] = storage
print(new_activities)