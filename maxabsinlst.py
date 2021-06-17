def main():
    max_value = max_abs_val([-19,-3,20,-1,0,-25])
    print(max_value)

def max_abs_val(lst):
    max_num = abs(lst[0])
    for index in range(len(lst) - 1):
        if(max_num > abs(lst[index + 1])):
            continue
        else:
            max_num = abs(lst[index + 1])
    return max_num


main()