# mod4_act1.py

"""
Tasks
1. Create a Record Keeping App
2. The application will ask the user to choose between:
    a. Add Data
    b. Delete Data
    c. End
3. If Add Data, the application will ask the user to input key and
    its value
    a. Enter Key: Lastname
    b. Enter Value: Doe
4. Store the information in a dictionary
5. Display the result
6. If Delete Data, the application will ask for the key
    a. Enter Key: Lastname
7. Remove the item from the dictionary
8. Display the result
9. If End, display THANK YOU
"""

data_storage = dict()

while True:

    print("Choose: Add Data, Delete Data, End\n")
    choice = input("Action: ")

    if choice.lower() == 'add data':

        key = input("Enter Key: ")
        val = input("Enter Value: ")

        data_storage[key] = val

        print(data_storage)

    if choice.lower() == 'delete data':

        key = input("Enter Key: ")
        data_storage.pop(key)

        print(data_storage)

    if choice.lower() == 'end':
        print("THANK YOU")
        break
