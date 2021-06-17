print("Please input several words, so a line of text, seperated with spaces: ")
line = input()

spaces_count = 0
for index in range(len(line)):
    curr_char = line[index]
    if(curr_char == " "):
        spaces_count += 1
number_of_words = spaces_count + 1
print("You typed", number_of_words, "words")