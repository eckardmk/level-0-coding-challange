def Area_of_Triangle(side1, side2, side3):

    s = (side1 + side2 + side3) / 2
    Area = ((s * (s - side1) * (s - side2) * (s - side3)))**0.5

    return Area


print(Area_of_Triangle(6, 7, 8))
