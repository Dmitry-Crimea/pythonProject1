# # 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк,
# # и сохраните в переменные, выведите на экран.
#
# # Создаём переменные и выводим на экран
# my_int = 5
# my_str = 'string'
# my_float = 2.1
# print(f"Число с точкой: {my_float}, Строка: {my_str}, Целое число: {my_int}")
#
# # Просим пользователя ввести значения и выводим их на экран
# my_int = int(input("Введите целое число: "))
# my_str = input("Введите строку: ")
# my_float = float(input("Введите число с точкой: "))
# print(f"Число с точкой: {my_float}, Строка: {my_str}, Целое число: {my_int}")
#
# # 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# # Используйте форматирование строк
#
# #Пользовательский ввод
# duration = int(input("Введите время в секундах: "))
#
# # Определяем константы
# minute = 60
# hour = minute * 60
# day = hour * 24
#
# # Для секунд
# if 0 < duration < 60:
#     print(f"{duration} сек.")
#
# # Для минут
# elif  minute < duration < hour:
#     print(f"{duration // minute}:{duration % minute} мин.")
#
# # Для часов
# elif hour < duration < day:
#     print(f"{duration // hour}:{duration // minute % minute}:{duration % minute} ")
#
# # Для дней
# elif day < duration:
#     print(f"{duration // day}:{duration % day // hour % minute}:{duration // minute % minute}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите цыфру: "))     # Запрашиваем ввод у пользователя
str_n = str(n)                        # Переводим число в строку
str_nn = str_n + str_n                # Конкатенируем строки
str_nnn = str_n + str_nn              # --------------------
sum_n = int(str_n) + int(str_nn) + int(str_nnn) # Переводим обчратно в "int" и суммируем

print(f" Сумма: {str_n} + {str_nn} + {str_nnn} = {sum_n}")

















