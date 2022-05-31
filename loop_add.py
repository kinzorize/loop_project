# using loop to sum up a list without using the sum() and len() and find the average
# I used for loop to understand how sum() and len() act behind the scene
total = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = total_heights / number_of_students
print(round(average_height))
