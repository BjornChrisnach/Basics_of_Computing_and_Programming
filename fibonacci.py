print("Please enter a positive integer greater than 1: ")
input_num = int(input())

counter = 0
int_num1 = 0
fibonnaci = []
int_num2 = 0

while counter < input_num:
    if (int_num1 == 0 and counter == 0) or (int_num2 == 1 and counter == 1):
        counter += 1
        int_num1 = 0
        int_num2 = 1
        int_num1, int_num2 = int_num2, int_num1 + int_num2
        fibonnaci.append(int_num2)
        print(fibonnaci)
    elif counter >= 2: 
        counter += 1   
        int_num1, int_num2 = int_num2, int_num1 + int_num2
        fibonnaci.append(int_num2)
        print(fibonnaci)