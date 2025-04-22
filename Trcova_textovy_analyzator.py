"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Sabina Trčová
email: sabina.trcova@gmail.com
"""

import string

texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# users = {username: password}
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

login_name = input("Enter your login name: ")
login_password = input("Enter your password: ")
no_texts = len(texts)

user_validation = login_name in users and users[login_name] == login_password
if user_validation:
    print(f"Welcome to the app, {login_name}.\nWe have {no_texts} texts to be analyzed.")
    selected_index_input = input(f"Enter the number of the text between 1 and {no_texts} to be analyzed: ")
    if selected_index_input.isdigit():
        selected_index = int(selected_index_input)
        if 1 <= selected_index <= no_texts:
            selected_text = texts[selected_index - 1]
            texts_split = selected_text.split()
            words_count = len(texts_split)
            titlecase_words = [word for word in texts_split if word.istitle()]
            titlecase_words_count = len(titlecase_words)
            upper_words = [word for word in texts_split if word.isupper()]
            upper_words_count = len(upper_words)
            lower_words = [word for word in texts_split if word.islower()]
            lower_words_count = len(lower_words)
            numbers = [number for number in texts_split if number.isdigit()]
            numbers_count = len(numbers)
            numbers_sum = sum(int(n) for n in numbers)
            print(f"There are {words_count} words in the selected text.")
            print(f"There are {titlecase_words_count} titlecase words in the selected text.")
            print(f"There are {upper_words_count} uppercase words in the selected text.")
            print(f"There are {lower_words_count} lowercase words in the selected text.")
            print(f"There are {numbers_count} numeric strings in the selected text.")
            print(f"The sum of all numbers is {numbers_sum}.")
            print("-" * 40)
            print(f"{'LEN':>3}|{'OCCURENCES':^15}|{'NR.':<}")
            print("-" * 40)
            
            lengths = {}
            for word in texts_split:
                word_clean = word.strip(string.punctuation)
                word_length = len(word_clean)
                if word_length >= 1:
                    lengths[word_length] = lengths.get(word_length, 0) + 1
                
            for length in sorted(lengths):
                stars = '*' * lengths[length]
                print(f"{length:>3}|{stars:<15}|{lengths[length]}")
        else:
            print("Selected text number is not in the range of available texts.")
    else:
        print("You have to enter a valid number.")
else:
    print(f"username: {login_name}\npassword: {login_password}")
    print("unregistered user or incorrect password, terminating the program")


