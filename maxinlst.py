def main():
    print(max_val([-19,-3,20,-1,5,-25]))

def max_val(lst):
    max_num = lst[0]
    for index in range(len(lst)-1):
        if max_num > lst[index + 1]:
            continue
        else:
            max_num = lst[index + 1]
    return max_num

main()