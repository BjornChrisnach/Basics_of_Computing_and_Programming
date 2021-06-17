def isleapyear(test_year):
    if(test_year % 4 == 0):
        if(test_year % 100 == 0):
            if(test_year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Explicitly asked to comment out the rest for the graded version

print("Please enter a year: ")
mybirthyear = int(input())
ret_bool = isleapyear(mybirthyear)
if ret_bool == True:
    print("Year {0} was a leap year".format(mybirthyear))
else:
    print("Year {0} was not a leap year".format(mybirthyear))