def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


print(fahrenheit_to_celsius(100))


def celsius_to_fahrenheit(celsius):
    fahrenheit = (1.8 * celsius) + 32
    return fahrenheit


print(celsius_to_fahrenheit(200))
