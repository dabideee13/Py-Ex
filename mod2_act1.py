# mod2_act1.py


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


# Test data
fahrenheit = 120.25
celsius = 37.38

print(celsius, "celsius is", round(celsius_to_fahrenheit(celsius), 2))
print(fahrenheit, "fahrenheit is", round(fahrenheit_to_celsius(fahrenheit), 2))
