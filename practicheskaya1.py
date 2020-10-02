class Point:
    amount = 0

    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = self.y = 0
        Point.amount += 1

    def __del__(self):
        Point.amount -= 1

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return '({}; {})'.format(self.x, self.y)


p = Point(36, 42)
from math import sqrt, pi


class Circle:
    def __init__(self, x, y, radius):
        self.centre = Point(x, y)
        self.radius = radius

    def lencircle(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * self.radius ** 2

    def move(self, x, y):
        self.centre.x = x
        self.centre.y = y
        return(x, y)

    def distance(self):
        return sqrt(self.centre.x ** 2 + self.centre.y ** 2)  # поставить исключение(например дел на 0)

    def __str__(self):
        return "Circle: centre: {}, radius: {}".format(self.centre,
                                                       self.radius)  # создать объект класса, вывести все методы

    def primer(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return(f'На ноль делить нельзя!')






Circle1 = Circle(33, 6, 98)
print("Длина окружности: " + str(Circle1.lencircle()))
print("Площадь окружности: " + str(Circle1.square()))
print("Перемещение центра окружности: " + str(Circle1.move(7, 976)))
print("Дистанция: " + str(Circle1.distance()))
print(str(Circle1))
print(Circle1.primer(5, 0))
