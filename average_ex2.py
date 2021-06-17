print("Enter grades in seperate lines. To end type 'done'")

calc_sum = 0
counter = 0
student_grade = 0.0

while str(student_grade) != 'done':
    student_grade = input()
    if student_grade != 'done':
        student_grade = int(student_grade)
    else:
        student_grade = "done"
        break
    calc_sum += student_grade
    counter += 1

average = calc_sum / counter
print("The class average is ", average)