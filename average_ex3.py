print("Enter grades in seperate lines. To end type 'done'")

grades_sum = 0
students_count = 0
seen_done = False

while(seen_done == False):
    curr_input = input()
    if(curr_input == 'done'):
        seen_done = True
        break
    else:
        curr_grade = int(curr_input)
        grades_sum += curr_grade
        students_count += 1

average = grades_sum / students_count
print("The class average is ", average)