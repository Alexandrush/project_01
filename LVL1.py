# # Задача 1.1.
#
# # Есть строка с перечислением песен
#
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
#
# # Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# # Нельзя переопределять my_favorite_songs и запятая не должна выводит

# print(my_favorite_songs.find("New Salvation"))
# print(my_favorite_songs.find("Staying\' Alive"),my_favorite_songs.rfind("Staying\' Alive") )
# print(my_favorite_songs.find("Start Me Up"), len("Start Me Up"))
print(my_favorite_songs[:14])
print(my_favorite_songs[64:77])
print(my_favorite_songs[16:30])
print(my_favorite_songs[51:62])

# Задача 1.2

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
from random import choices
r =  choices(my_favorite_songs, k=3)
print(r)
a =(r[0][1])
b = (r[1][1])
c= (r[2][1])
total= a+b+c
print("Три выбранных песни звучат",total,"минут.")


# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
random_values = random.sample(list(my_favorite_songs_dict.values()), 3)
total1 = sum(random_values)
print("Три выбранных песни звучат", total1)

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца,
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

print("Привет!")
x = int(input("Номер_месяца:"))

month_number_dict = {"January": 1, "February": 2,"March": 3, "April": 4,
                      "May": 5, "June": 6, "July": 7, "August": 8,
                      "September": 9, "October": 10, "November": 11, "December": 12}


y = list(month_number_dict.keys()) [list(month_number_dict.values()).index(x)]
if x> 12:
    print("Такого месяца нет!")

if y == 'September' or y == 'April' or y == 'June' or y == 'November':
    print("Вы ввели", y,"30 дней")
elif y == 'January' or y == 'March' or y == 'May' or y== 'July' or y == 'August' or y == 'October' or y== 'December':
    print("Вы ввели", y,"31 день")
elif y == 'February':
    print("Вы ввели", y, "28 дней")

# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for item in titles:
    item_name = item
    item_code = titles[item_name]
    item_quantity = 0
    item_total_amount = 0

    for i in range(0, len(store[item_code])):
        item_quantity += store[item_code][i]['quantity']
        item_total_amount += store[item_code][i]['quantity'] * store[item_code][i]['price']

    print(item_name, item_quantity,'штук,' , 'стоимость', item_total_amount)
