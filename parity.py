print("Please enter a number: ")
number = int(input())

if number % 2 == 0:
    number_parity = True
    print(number, "is even")
else:
    number_parity = False
    print(number, "is odd")