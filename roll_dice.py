import random

def main():
    print("Please enter a positive integer: ")
    input_num = int(input())
    result_lst = list_of_dice_rolls(input_num)
    print(result_lst)

def list_of_dice_rolls(n):
    dice_rolls_lst = []
    for count in range(n):
        curr_role = random.randint(1, 6)
        dice_rolls_lst.append(curr_role)
    return dice_rolls_lst


main()