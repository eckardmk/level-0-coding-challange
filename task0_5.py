def Area_of_Triangle(a, b, c):

    s = (a + b + c) / 2
    Area = ((s * (s - a) * (s - b) * (s - c)))**0.5

    return Area


print(Area_of_Triangle(6, 7, 8))
