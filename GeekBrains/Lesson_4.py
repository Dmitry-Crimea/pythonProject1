########################################################################################################################

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

"""
salary - зарплата
prod_per_h - выработка в часах (часы)
rate_per_h - ставка (руб. в час)
prize = argv - премия (руб)
"""

script_name, prod_per_h, rate_per_h, prize = argv

salary = float(prod_per_h) * float(rate_per_h) + float(prize)
print("Зарплата сотрудника:", salary)


########################################################################################################################
#
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list = [i for idx, i in enumerate(user_list) if idx > 0 and user_list[idx] > user_list[idx - 1]]
print(my_list)

########################################################################################################################

3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.

my_list = (i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0)
print(list(my_list))

########################################################################################################################

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходный список: {user_list}")

res_list = [x for i, x in enumerate(user_list) if i > 0 and user_list[i] > user_list[i - 1]]

print(res_list)

########################################################################################################################

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [x for x in range(100, 1000 + 2) if x % 2 == 0]
print(f'Список четных элементов: {my_list}')

sum_all = reduce(lambda x, y: x * y, my_list)

print(f'Результат произведения всех элементов списка: {sum_all}')

########################################################################################################################

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# a)

from itertools import count
user_input = int(input("Введите число: "))

for i in count(user_input):
    if i == 10:
        break
    else:
        print(i)

# b)

from itertools import cycle

user_input = input("Введите символ: ")

c = 0
for i in cycle(user_input):
    if c > 10:
        break
    else:
        print(i)
        c += 1

########################################################################################################################

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n)
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def my_gen(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
        yield res


a = int(input("Введите число: "))
for el in my_gen(a):
    print(el)
