def FahToCel(fah):
    celsius = (fah - 32) / 1.8
    return celsius


print(FahToCel(150))


def Celsius_To_Fahrenheit(cel):
    fahrenheit = (1.8 * cel) + 32
    return fahrenheit


print(Celsius_To_Fahrenheit(50))
