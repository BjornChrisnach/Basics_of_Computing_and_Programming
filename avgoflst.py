# Again the ask to comment out the rest and only leave avg_val function for autograder, so do so if needed
def main():
    input_lst = [19,2,20,1,0,18]
    average = avg_val(input_lst)
    print(average)

def avg_val(lst):
    calc_sum = 0
    for elem in lst:
        calc_sum += elem
    
    calc_average = (calc_sum / len(lst))
    calc_average = round(calc_average)
    return calc_average


main()