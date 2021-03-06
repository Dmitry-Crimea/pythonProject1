########################################################################################################################

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


while True:
    inp_1 = int(input('Введите первый аргумент: '))
    inp_2 = int(input('Введите первый аргумент: '))


    def math(a, b):
        try:
            res = a / b
            return res
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")


    print(math(inp_1, inp_2))

########################################################################################################################

# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: # имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    while True:
        try:
            year_of_birth = int(input("Введите год рождения цифрами: "))
            break
        except ValueError:
            print("Вы ввели неверное значение")
    city = input("Введите ваш город проживания: ")
    email = input("Введите ваш e-mail: ")
    while True:
        try:
            phone = input("Введите ваш телефон: ")
            break
        except ValueError:
            print("Вы ввели неверное значение")
    res = (name, surname, year_of_birth, city, email, phone)
    return res


print(user_data())

########################################################################################################################

# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    res_1 = [a, b, c]
    res_1.remove(min(a, b, c))
    return sum(res_1)


print(my_func(10, 20, 30))

########################################################################################################################

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# **Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# var_1

def my_func(x, y):
    res = x ** abs(y)
    return res


print(my_func(2, (-5))) # Проверка функции

# var_2

def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return res


print(my_func(2, (-5)))

########################################################################################################################

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен
# после нескольких чисел,# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def user_sum(args):
    item = 0
    idx = True
    for el in args:
        if el == 'q':
            print("Программа завершена!")
            idx = False
            break
        else:
            item += int(el)
    return item, idx

user_itm = 0
flag = True
while flag:
    print("Для выхода из программы введите 'q' ")
    try:
        user_input = input("Введите числа через пробел: ").split()
        result_sum, flag = user_sum(user_input)
        print(f'Сумма строки: {result_sum}')
        user_itm += result_sum
    except ValueError:
        print("Введите цифры!")
print(f'Итоговая сумма: {user_itm}')

########################################################################################################################

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

user_input = input("Введите слова состоящие из букв: ")


def int_func(user_str):
    if user_str.isalpha() is True:
        return user_str.title()
    else:
        print("Введите слова состоящие из букв!")


print(int_func(user_input))

########################################################################################################################
