# task 7
# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.


def fact(number):
    count = 1
    while count <= number:
        yield count
        count += 1
        
        
def my_func():
    i = 1
    result = []
    fact_n = int(input('Enter a factorial number: '))
    result_count = int(input('How many numbers to output: '))
    for el in fact(result_count):
        if i > fact_n:
            break
        else:
            result.append(el)
            i += 1
    print(result)


my_func()