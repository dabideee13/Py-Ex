# mod2_act1.py

"""
farenheit = 120.25
celsius = 37.38

celsius_to_fahrenheit = ###
fahrenheit_to_celsius = ###

print(celsius, "celsius is", round(celsius_to_fahrenheit, 2), "fahrenheit")
print(fahrenheit, "fahrenheit is", round(fahrenheit_to_celsius, 2), "celsius")

Tasks
1. Modify the given code and assign the correct expressions to convert
    fahrenheit to celsius and vice versa.

Formula:
    (__degree celsius * 9/5) + 32 = __degree fahrenheit
    (__degree fahrenheit * 5/9) = __degree celsius

"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


# Test data
fahrenheit = 120.25
celsius = 37.38

print(celsius, "celsius is", round(celsius_to_fahrenheit(celsius), 2), "fahrenheit")
print(fahrenheit, "fahrenheit is", round(fahrenheit_to_celsius(fahrenheit), 2), "celsius")
