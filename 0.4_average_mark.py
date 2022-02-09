""" Calculate the average and highest student marks
Created by Amy Jorgensen
09/02/22
"""


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

    name = input("Enter the student name: ").title()

# Calculate average mark
avg_mark = t_marks / num_students

# Output
print("The student with the highest marks was {} with {} out of 100"
      .format(highest_student, highest_mark))
print("The average score was {:.0f} out of 100".format(avg_mark))


