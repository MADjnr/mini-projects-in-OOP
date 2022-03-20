import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(math.pi * (self.radius ** 2))


circle_one = Circle(23)
circle_one.calculate_area()




import random


class Die:

    def __init__(self, value):
        self.value = value

    def roll_die(self):
        random_value = random.randint(1,6)
        self.value = random_value


my_die = Die(5)

print(my_die.value)
my_die.roll_die()
print(my_die.value)