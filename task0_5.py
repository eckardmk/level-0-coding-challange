import math


def Area_of_Triangle(a, b, c):

    s = (a + b + c) / 2
    Area = math.sqrt((s * (s - a) * (s - b) * (s - c)))

    return Area


print(Area_of_Triangle(6, 7, 8))