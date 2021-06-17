grade = int(input("Please enter a grade: "))

if(0 <= grade < 60):
    print(grade, "is F")
elif(60 <= grade < 70):
    print(grade, "is D")
elif(70 <= grade < 80):
    print(grade, "is C")
elif(80 <= grade < 90):
    print(grade, "is B")
elif(90 <= grade <= 100):
    print(grade, "is A")
else:
    print(grade, "is an invalid grade")