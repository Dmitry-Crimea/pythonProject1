########################################################################################################################
#
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = True

    def running(self):
        while True:
            self.__color = "Red"
            print(f'{self.__color}')
            sleep(7)
            self.__color = "Yellow"
            print(f'{self.__color}')
            sleep(3)
            self.__color = "Green"
            print(f'{self.__color}')
            sleep(7)


traffic_light = TrafficLight()
traffic_light.running()


########################################################################################################################

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = int
    _width = int

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def calculated(self):
        res = self.__length * self.__width * 25 * 5 / 1000
        print(f'{res} тонн')


result = Road(3000, 200)

result.calculated()


########################################################################################################################

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    name = str
    surname = str
    position = str
    _income = dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f"Имя сотрудника: {self.name, self.surname} \n Занимаемая должность: {self.position}")

    def get_total_income(self):
        print(f"Средний доход {self.name} {self.surname} равен {sum(self._income.values())} р.")


john = Position("John", "Doe", "Manager", {"wage": 500, "bonus": 300})

john.get_full_name()
john.get_total_income()


########################################################################################################################

# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = int
    color = str
    name = str
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name}, {self.color} цвета поехала"

    def stop(self):
        return f"Машина {self.name}, {self.color} остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"

    def show_speed(self):
        return f"Скорость машины {self.name} - {self.speed} "


class TownCar(Car):
    def car_speed(self):
        if self.speed > 60:
            return f"Вы ревысили скорость!"


class SportCar(Car):
    pass


class WorkCar(Car):
    def car_speed(self):
        if self.speed > 40:
            return f"Вы ревысили скорость!"


class PoliceCar(Car):
    pass


print("Список автомобилей: town_car, sport_car, work_car, police_car")

# user_car = input("Введите автомобиль из списка: ")
# user_speed = input("Введите скорость: ")
# user_color = input("Введите цвет автомобиля: ")
# user_name = input("Введите марку автомобиля: ")

print(user_car.go(), user_speed.show_speed(), user_car.turn("right"))
