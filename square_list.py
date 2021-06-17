def main():
    lst = [1,2,3]

    sqr_lst = create_square_list(lst)
    print(sqr_lst)
    square_list_in_place(lst)

def create_square_list(sqr_list):
    square_list = []
    for element in sqr_list:
        square_list.append(element * element)
    return square_list

def square_list_in_place(sq_lst):
    for index in range(len(sq_lst)):
        sq_lst[index] = (sq_lst[index] * sq_lst[index])
    print(sq_lst)


main()