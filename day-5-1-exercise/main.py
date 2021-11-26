# Average Height Of Students

student_heights = input("Input a list of student heights ")
student_heights = student_heights.split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# print(len(student_heights)) counts the number of items in a list

number_of_students = 0
for student in student_heights:
    number_of_students += 1

# print(number_of_students) second way of counting

total_height = 0
for heights in student_heights:
    total_height += heights
avg_height = total_height / number_of_students

print(f"The average height of students in a class is: {avg_height} cm.")