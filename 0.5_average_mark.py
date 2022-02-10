""" Calculate the average and highest student marks
Created by Amy Jorgensen
10/02/22
"""

exams = []
t_marks = 0
num_students = 0

highest_mark = 0
highest_student = ""

# Set up loop
name = input("Enter the student name: ").title()

while name != "X":
    # Get student marks
    mark = int(input("Enter the students mark: "))

    # Check if student has highest marks
    if mark > highest_mark:
        highest_mark = mark
        highest_student = name

    # Add marks to total
    t_marks += mark
    num_students += 1

    # Calculate grade
    grade = ""
    if mark >= 90:
        grade = "A+"
    elif mark >= 85:
        grade = "A"
    elif mark >= 80:
        grade = "A-"
    elif mark >= 75:
        grade = "B+"
    elif mark >= 70:
        grade = "B"
    elif mark >= 65:
        grade = "B-"
    elif mark >= 60:
        grade = "C+"
    elif mark >= 55:
        grade = "C"
    elif mark >= 50:
        grade = "C-"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "E"

    # Add student to list
    exams.append([name, grade])

    name = input("Enter the student name: ").title()

# Calculate average mark
avg_mark = t_marks / num_students

# Output
print()
print("The student with the highest marks was {} with {} out of 100"
      .format(highest_student, highest_mark))
print("The average score was {:.0f} out of 100".format(avg_mark))
print()

# Output student grades
for student in exams:
    print(f"{student[0]} got {student[1]}")
