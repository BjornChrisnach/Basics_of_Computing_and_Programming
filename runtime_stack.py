def main():
    m = 0
    n = 0
    print("Before: m =", m,",n =", n)
    m = m + func(n)
    print("Between: m =", m, ",n = ", n)
    m = m + func(n)
    print("After: m =", m, ",n = ", n)

def func(n):
    n = n + 1
    print("Inside: n =", n)
    return n

main()