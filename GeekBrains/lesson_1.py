# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк,
# и сохраните в переменные, выведите на экран.

# Создаём переменные и выводим на экран
my_int = 5
my_str = 'string'
my_float = 2.1
print(f"Число с точкой: {my_float}, Строка: {my_str}, Целое число: {my_int}")

# Просим пользователя ввести значения и выводим их на экран
my_int = int(input("Введите целое число: "))
my_str = input("Введите строку: ")
my_float = float(input("Введите число с точкой: "))
print(f"Число с точкой: {my_float}, Строка: {my_str}, Целое число: {my_int}")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

#Пользовательский ввод
duration = int(input("Введите время в секундах: "))

# Определяем константы
minute = 60
hour = minute * 60
day = hour * 24

# Для секунд
if 0 < duration < 60:
    print(f"{duration} сек.")

# Для минут
elif  minute < duration < hour:
    print(f"{duration // minute}:{duration % minute} мин.")

# Для часов
elif hour < duration < day:
    print(f"{duration // hour}:{duration // minute % minute}:{duration % minute} ")

# Для дней
elif day < duration:
    print(f"{duration // day}:{duration % day // hour % minute}:{duration // minute % minute}")




















