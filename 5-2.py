# Task 2
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("my_file_5-2.txt", encoding='utf-8') as my_file:
    my_list = [j.strip() for j in my_file]
print(f'Количество строк в файле: {len(my_list)}')
string = 1
for word in my_list:
    word_list = list(word.split())
    print(f'Количество слов в {string}-й строке: {len(word_list)}')
    string += 1
