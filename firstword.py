# Again the call to explicitly leave out anything else then the remainingwords function, so comment out if needed
def main():
    print(remainingwords("The quick brown fox"))

def remainingwords(s):
    ind = s.find(" ")
    ret_str = s[ ind + 1 : ]
    return ret_str


main()