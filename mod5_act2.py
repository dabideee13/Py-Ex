# mod5_act2.py

"""
Tasks:
    1. Create a calculator app
    2. The user will choose between the 4 math operations (Add,
        Subtract, Multiply and Divide)
    3. The application will ask for 2 numbers
    4. Display the result
    5. The application will ask again if the user wants to try again
    6. Use the appropriate Exception (ex: Invalid input such as text
        zero division)
"""


def formatter(x):
    print(f"Answer: {x}\n")


def perform_operation(operation, first, second):

    operation = operation.strip().lower()
    operation_list = ['add', 'subtract', 'multiply', 'divide']

    if operation not in operation_list:
        print("Invalid input: operation not allowed\n")

    if operation == 'add':
        result = first + second
        formatter(result)

    elif operation == 'subtract':
        result = first - second
        formatter(result)

    elif operation == 'multiply':
        result = first * second
        formatter(result)

    elif operation == 'divide':
        try:
            result = first / second
            formatter(result)
        except ZeroDivisionError:
            print("Invalid input: zero division error\n")


def main():

    yes_list = ['yes', 'y']
    no_list = ['no', 'n']

    while True:

        operation = input("Add, Subtract, Multiply, or Divide: ")
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        perform_operation(operation, first, second)

        trial = input("\nTry again? (Yes/No): ")

        if trial.strip().lower() in yes_list:
            continue

        elif trial.strip().lower() in no_list:
            break


if __name__ == '__main__':
    main()
