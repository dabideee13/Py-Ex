# mod6_act2.py

"""
Tasks:
    1. Create a Class called Employee
    2. Use the init function to collect the employee information
        a. Name, email and mobile number
    3. Instantiate the Employee class two times with different
        information
    4. Display all the properties of the object
"""


class Employee:

    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

        print(f"Employee")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Mobile Number: {self.mobile_number}\n")


def main():

    emp1 = Employee(
        'Azman Nads',
        'azman.nads@g.msuiit.edu.ph',
        '09061234567'
    )
    emp2 = Employee(
        'Joseph Abordo',
        'joseph.abordo@g.msuiit.edu.ph',
        '09171234567'
    )


if __name__ == '__main__':
    main()
