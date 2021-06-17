print("Enter an odd length string: ")
odd_len_string = input()

index = int(len(odd_len_string)/2)
middle_character = odd_len_string[index]
print("Middle character: ", middle_character)
first_half = odd_len_string[:index]
print("First half: ", first_half)
second_half = odd_len_string[(index +1):]
print("Second half : ", second_half)