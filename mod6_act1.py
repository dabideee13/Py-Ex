# mod6_act1.py

"""
Tasks:
    1. Create a class called Car. The Car class has the following
        fields:
        - color
        - model
        - Manufacturer
    2. Instansiate the Car class 3 times and display all properties
    3. Modify the properties
"""


class Car:

    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

        print(f"Car")
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Manufacturer: {self.manufacturer}\n")


def main():

    # Instantiate the Car class 3 times
    Car1 = Car('white', '2020 Kia Telluride', 'Kia')
    Car2 = Car('red', '2020 Chevrolet Corvette', 'Chevrolet')
    Car3 = Car('gray', '2020 Jeep Gladiator', 'Jeep')


if __name__ == '__main__':
    main()


