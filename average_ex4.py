def main():
    print("Enter grades in seperate lines. To end type 'done'")
    curr_input_lst = []
    calc_average = calculate_average(curr_input_lst) 
    print("The class average is ", calc_average)
    print_str = prepare_print_line(curr_input_lst, calc_average)
    print(print_str)

def calculate_average(inp_lst):
    grades_sum = 0
    students_count = 0
    seen_done = False
    index = 0

    while(seen_done == False):
        inp_lst.append(input())
        if(inp_lst[index] == 'done'):
            seen_done = True
            break
        else:
            grades_sum += int(inp_lst[index])
            students_count += 1
        index += 1

    average = grades_sum / students_count
    return average

def prepare_print_line(input_list, calc_average):
    above_average_lst = []
    for num in input_list:
        if(num != 'done'):
            if(float(num) >= calc_average):
                above_average_lst.append(num)
                if len(above_average_lst) == 1:
                    counter_avg = 0
                    print_str = f"The grades above the average are: {above_average_lst[counter_avg]}"
                else:
                    counter_avg += 1
                    print_str = print_str + ", " + f"{above_average_lst[counter_avg]}"
        else:
            break
    return print_str


main()