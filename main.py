# -*- coding: utf-8 -*-

# # 1. Создать произвольный список
# lst = [1, 2, 3, 3, 5]
# # 2. Добавить новый элемент типа str в конец списка
# lst.append('str-1')
# # 3. Добавить новый элемент типа int на место с индексом
# lst.insert(4, 189)
# # 4. Добавить новый элемент типа list в конец списка
# lst.append([9, 8, 7])
# # 5. Добавить новый элемент типа tuple на место с индексом 3
# lst.insert(3, (56, 65))
# # 6. Получить элемент по индексу
# print(lst[3])
# # 7. Удалить элемент
# lst.remove([9, 8, 7])
# # 8. Найти число повторений элемента списка
# print(lst.count(1))
# # 9 Получите первый и последний элемент списка
# print(lst[0])
# print(lst[0])
# #Поменяйте значения переменных a и b местами
# a = 100
# b = 50
# a,b = b, a
#
#
# #Проверить, есть ли в последовательности дубликаты
# lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
# st = set(lst)
# print(len(lst) == len(st))
#
#
# # 1. Создать произвольный словарь
# dct = {1: 'value_1', 2: 'value_2', 3: 'value_3'}
# # 2. Добавить новый элемент с ключом типа str и значением типа int
# dct['abc'] = 777
# # 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# dct[(1, 2, 3)] = ['asd', 'dsa']
# # 4. Получить элемент по ключу
# print(dct[(1, 2, 3)])
# # 5. Удалить элемент по ключу
# dct.pop((1, 2, 3))
# print(dct)
# # 6. Получить список ключей словаря
# print(dct.keys())
#
#
# # 1. Создать множество(set)
# st = {'it', 'is', 'set', 1}
# # 2. Создать неизменяемое множество(frozenset)
# frzn_st = frozenset(st)
# # 3. Выполнить операцию объединения созданных множеств
# union = st | frzn_st
# # 4. Выполнить операцию пересечения созданных множеств
# intersection = st & union



# Есть словарь координат городов:
# sites = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480),
# }
# # Составить словарь словарей расстояний между ними
# distances = {}
# """создали пустой словарь distances, который в итоге наполним ключами и значениями"""
# moscow = sites['Moscow']
# london = sites['London']
# paris = sites['Paris']
# """ задали переменные для обращения к координатам абсцисс и ординат, которые являются значениями в словаре sites """
# moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
# moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
# london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5
# """ посчитали расстояния между городами"""
# distances['Moscow'] = {}
# distances['Moscow']['London'] = moscow_london
# distances['Moscow']['Paris'] = moscow_paris
# distances['London'] = {}
# distances['London']['Moscow'] = moscow_london
# distances['London']['Paris'] = london_paris
# distances['Paris'] = {}
# distances['Paris']['London'] = london_paris
# distances['Paris']['Moscow'] = moscow_paris
# """создали словарь"""
# print(distances)



# # Есть значение радиуса круга
# radius = 42
# # выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# # Выведите на консоль True если точка point = (23, 34) лежит внутри круга radius = 42, False - в противном случае
#
# print(round(3.1415926 * radius ** 2, 4))
# point = (23, 34)
# print((point[0] ** 2 + point[1] ** 2) ** .5 <= radius)



# Есть строка с перечислением фильмов

# my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
#
# # выведите на консоль с помощью индексации строки, последовательно:
# #   первый фильм
# print(my_favorite_movies[0:10])
# #   последний
# print(my_favorite_movies[-15:])
# #   второй
# print(my_favorite_movies[12:24])
# #   второй с конца
# print(my_favorite_movies[-22:-17])
# # обратите внимание что запятая не должна выводиться



#  # Создайте списки:
# # моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
# my_family = [
#     'отец',
#     'мать',
#     'сын',
# ]
## # список списков приблизителного роста членов вашей семьи
# my_family_height = [
#     ['отец', 186],
#     ['мать', 170],
#     ['сын', 165],
# ]
## # Выведите на консоль рост отца
# print('рост отца=', my_family_height[0][1],'см')
# # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов

# total_family_heigh = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
# print('общий рост семьи=', total_family_heigh, 'см')



# # есть список животных в зоопарке
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
#
# # посадите медведя (bear) во 2-ю клетку
# #  и выведите список на консоль
# zoo.insert(1, 'bear')
# print(zoo)
#
# # добавьте птиц в последние клетки
# birds = ['rooster', 'ostrich', 'lark', ]
# #  и выведите список на консоль
# zoo.extend(birds)
# print(zoo)
#
# # уберите слона
# #  и выведите список на консоль
# zoo.remove('elephant')
# print(zoo)



# # Есть список песен группы Depeche Mode
#
# violator_songs_list = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83],
# ]
# # # распечатайте общее время звучания песен 'Halo' 'Enjoy the Silence' 'Clean'
# print(round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[-1][1], 2))



# # в саду сорвали цветы
# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
#
# # на лугу сорвали цветы
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
#
# # создайте множество цветов, произрастающих в саду и на лугу
# garden_set = set(garden)
# meadow_set = set(meadow)
# # выведите на консоль все виды цветов
# print(garden_set | meadow_set)
#
# # выведите на консоль те, которые растут и там и там
# print(garden_set & meadow_set)
#
# # выведите на консоль те, которые растут только в саду
# print(garden_set - meadow_set)
#
# # выведите на консоль те, которые растут только на лугу
# print(meadow_set - garden_set)




# # Есть словарь кодов товаров
#
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
# # Есть словарь списков количества товаров на складе.
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
# # Рассчитать на какую сумму лежит каждого товара на складе
# # например для ламп
#
# lamp_code = goods['Лампа']
# lamp_item = store[lamp_code][0]
# lamp_qty = lamp_item['quantity']
# lamp_price = lamp_item['price']
# lamp_total_price = lamp_qty * lamp_price
# print('на складе хранится', lamp_qty, 'шт. ламп по цене', lamp_price, 'руб. на сумму', lamp_total_price, 'руб')





