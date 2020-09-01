# task 6
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
goods = []
while input('Would you like add product? Enter yes/no: ') == 'yes':
    number = ''
    while number is not int:
        try:
            number = int(input('Enter product number: '))
            break
        except ValueError:
            print('Please enter a valid number: ')
    features = {}
    while input('Would you like add product parameters? Enter yes/no: ') == 'yes':
        feature_key = input('Enter feature product: ')
        feature_value = input('Enter feature value product: ')
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
print(analitics)