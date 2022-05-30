def area_of_triangle(side1, side2, side3):

    semiperimeter = (side1 + side2 + side3) / 2
    area = ((semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (s - side3)))**0.5

    return area


print(area_of_triangle(6, 7, 8))
