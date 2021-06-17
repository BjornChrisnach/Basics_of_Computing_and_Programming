print("Please enter the number of students in the class: ")
number_of_students = int(input())

print("Please enter the students' grades (in seperate lines): ")
calc_sum = 0
for i in range(number_of_students):
    student_i = int(input())
    calc_sum += student_i 
    
average = calc_sum / number_of_students
print("The class average is", average)