def main():
    print("Enter grades in seperate lines. To end type 'done'")
    grades_list = read_list()
    calc_average = calculate_average(grades_list) 
    print("The class average is ", calc_average)
    above_avg_list = filter_above_value(grades_list, calc_average)
    print(above_avg_list)
    
def read_list():
    seen_done = False
    res_list = []
    while(seen_done == False):
        curr_input = input()
        if(curr_input == 'done'):
            seen_done = True
        else:
            curr = int(curr_input)
            res_list.append(curr)
    return res_list

def calculate_average(inp_lst):
    grades_sum = 0

    for elem in inp_lst:
        grades_sum += elem
    average = grades_sum / len(inp_lst)
    return average

def filter_above_value(lst, val):
    res_list = []
    for elem in lst:
        if(elem > val):
            res_list.append(elem)
    return res_list


main()