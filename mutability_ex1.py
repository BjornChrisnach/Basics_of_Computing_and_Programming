def main():
    lst = [1,2,3]
    n = 10
    print("Before func: lst=", lst, "and n=", n)
    func(lst,n)
    print("After func: lst=", lst, "and n=", n)
def func(lst, n):
    lst.append(4)
    n = n + 1
    print("Inside func: lst =", lst, "and n=", n)


main()