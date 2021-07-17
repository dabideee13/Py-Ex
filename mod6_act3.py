# mod6_act3.py

"""
Tasks:
    1. Create House Class with the following properties and methods
        a. floorSize
        b. noOfFloors
        c. noOfDoors
        d. switchOn()
        e. lightOpen()
        f. ovenOpen()
    2. Create TownHouse Class inherit the House class
    3. Modify the value of the following (noOfFloors and noOfDoors)
    4. Instantiate the TownHouse Class once
    5. Display all the properties
    6. Calling the switchOn() will automatically execute lightOpen()
        and ovenOpen()
"""


class House:

    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

        print(f"No of floors: {self.noOfFloors}")
        print(f"No of doors: {self.noOfDoors}\n")

    def switchOn(self):
        print("switch on")
        self.lightOpen()
        self.ovenOpen()

    def lightOpen(self):
        print("light open")

    def ovenOpen(self):
        print("oven open")


class TownHouse(House):

    def __init__(self, noOfFloors, noOfDoors):
        super().__init__(self, noOfFloors, noOfDoors)


def main():

    town_house = TownHouse(3, 120)
    town_house.switchOn()


if __name__ == '__main__':
    main()
