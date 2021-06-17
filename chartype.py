curr_character = input("Enter a character: ")
if curr_character.islower():
    print(curr_character, "is a lower case letter.")

curr_character = input("Enter a character: ")
if curr_character.isdigit():
    print(curr_character, "is a digit.")

curr_character = input("Enter a character: ")
if not curr_character.isalpha():
    print(curr_character, "is a non-alphanumeric character.")

curr_character = input("Enter a character: ")
if curr_character.isupper():
    print(curr_character, "is a upper case letter.")