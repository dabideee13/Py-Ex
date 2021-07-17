# mod7_act1.py

"""
Tasks:
    1. Create a Record Keeping App
    2. This will display the following options:
        a. Add Record
        b. View Records
        c. Clear All Records
        d. Exit
    3. If A: The user will input the following information (name,
        email, address)
    4. The app will save the information in a text file
    5. If B, display the saved records
    6. If C, clear the text file and display "No records found."
    7. If D, display "Thank you"
"""


def main():

    with open('records.txt', 'w') as f:
        f.write('')

    print("\nRecord Keeping App")

    while True:

        print(
            "\na. Add Record"
            "\nb. View Records"
            "\nc. Clear All Records"
            "\nd. Exit\n"
        )
        action = input("Enter action: ")

        if action == 'a':
            name = input("\nEnter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            record = f"""
Name: {name}
Email: {email}
Address: {address}
"""

            with open('records.txt', 'a') as f:
                f.write(record)

        elif action == 'b':
            with open('records.txt', 'r') as f:
                print(f.read())

        elif action == 'c':
            with open('records.txt', 'r+') as f:
                f.truncate(0)
                print(f.read())

        elif action == 'd':
            break


if __name__ == '__main__':
    main()
