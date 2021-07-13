# mod3_act2.py

"""
Tasks
1. Write a program that adds two numbers.
2. The program will ask to enter first and second number.
3. The program will display "The sum of n1 and n2 is nTotal"
4. The program will ask if the user wants to try again. The user will
    input Y/y if Yes and N/n if No.
5. If Yes, refer to step 2.
6. If No, the program will display "Thank you!"
"""


def add(fst_num, snd_num):
    return fst_num + snd_num


yes_list = ['Yes', 'yes', 'Y', 'y']
no_list = ['No', 'no', 'N', 'n']

while True:

    fst_num = float(input("First number: "))
    snd_num = float(input("Second number: "))
    total = add(fst_num, snd_num)

    print(f"The sum of {fst_num} and {snd_num} is {total}\n")

    trial = input("Try again? (Yes or No): ")

    while trial not in (yes_list + no_list):
        print("\nInvalid input.")
        trial = input("Try again? (Yes or No): ")

    if trial in yes_list:
        continue

    elif trial in no_list:
        print("Thank you!")
        break

