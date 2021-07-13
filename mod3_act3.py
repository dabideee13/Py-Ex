# mod3_act3.py

"""
Tasks
1. Write a word bank program.
2. The program will ask to enter a word.
3. The program will store the word in a list.
4. The program will ask if the user wants to try again. The user will
    input Y/y if Yes and N/n if No.
5. If Yes, refer to step 2.
6. If No, display the total number of words and all the words that
    user entered.
"""

yes_list = ['Yes', 'yes', 'Y', 'y']
no_list = ['No', 'no', 'N', 'n']

word_list = []
while True:

    word = input("Enter a word: ")
    word_list.append(word)

    add_word = input("Try again? (Yes or No): ")

    while add_word not in (yes_list + no_list):
        print("\nInvalid input.")
        add_word = input("Try again? (Yes or No): ")

    if add_word in yes_list:
        continue

    elif add_word in no_list:
        print(f"\nTotal words: {word_list}")
        break

