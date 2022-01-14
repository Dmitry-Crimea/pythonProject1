

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

# Пользовательский ввод
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




















