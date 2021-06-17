print("Please enter a positive integer: ")
n = int(input())

for i in range(1,n + 1):
    # if i != n:
    line = (n - i)*' ' + i*'*'
    # else:
    #     line = i*'*'
    print(line)