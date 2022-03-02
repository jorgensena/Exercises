""" Create a program for a small local library
25/02/22
By Amy Jorgensen
"""


# Student class
class Students:
    def __init__(self, name, age, phone, form, subjects, gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.form = form
        self.subjects = subjects
        self.is_male = gender
        self.enrolled = True
        student_list.append(self)
        student_subjects.append(self.subjects)

    def display_info(self):
        print()
        print(f"Name: {self.name}"
              f"\nAge: {self.age}"
              f"\nPhone number: {self.phone}"
              f"\nForm class: {self.form}"
              f"\nSubjects: {self.subjects}")
        if self.is_male:
            print("Gender: Male")
        else:
            print("Gender: Female")
        print(f"Enrolled: {self.enrolled}")


# Teacher class
class Teachers:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        teacher_list.append(self)

    def display_info(self):
        print()
        print(f"Name: {self.name}"
              f"\nSubjects: {self.subject}")


# Print student details
def print_student_details():
    print()
    print("-----------------------------------------------------")
    for student in student_list:
        student.display_info()


# Print student details
def print_teacher_details():
    print()
    print("-----------------------------------------------------")
    for teacher in teacher_list:
        teacher.display_info()


# print students older than certain age
def select_student_age():
    print()
    print("-----------------------------------------------------")
    age = int(input("What student age and older would you like to print: "))
    error = True
    for student in student_list:
        if student.age >= age:
            student.display_info()
            error = False
    if error:
        print("Oops, something went wrong! Nobody seems to be that age or "
              "older")


# Generate students
def generate_students():
    import csv
    with open('student_lists.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Students(line[0], int(line[1]), line[2], line[3], line[4], is_male)


# count number of students in a class
def count_students():
    # Get subject
    print()
    print("-----------------------------------------------------")
    subject = input("What subject are you looking for?: ").upper()
    student_count = 0
    # separate the classes into separate strings
    for classes in student_subjects:
        class_list = classes.split(', ')
        # check if any of the subjects matches the the given subject
        for subjects in class_list:
            if subject == subjects:
                # If matches add a student number to count
                student_count += 1
    if student_count > 0:
        for teacher in teacher_list:
            if teacher.subject == subject:
                print(f"There are {student_count} students taking this subject")
                print(f"{teacher.name} teaches this subject")
    else:
        print("Oops, something went wrong! Nobody takes this class")


# Find students
def find_student():
    print()
    print("-----------------------------------------------------")
    name = input("Enter the name: ").title()
    print("-----------------------------------------------------")
    found_pupil = False
    for pupil in student_list:
        if pupil.name == name:
            pupil.display_info()
            found_pupil = True
    if not found_pupil:
        print("Oops, something went wrong! Nobody has that name")


# Add new student
def new_student():
    print()
    print("-----------------------------------------------------")
    name = input("Enter the name (first and last name): ").title()
    age = int_check("Enter the age: ")
    phone = input("Enter the phone number: ")
    form = input("Enter the form class: ").upper()
    subjects = new_subjects()
    gender = get_gender()
    Students(name, age, phone, form, subjects, gender)


# get the gender
def get_gender():
    get_g = False
    while not get_g:
        gender = input("Enter 'M' if the student is male, or 'F' if "
                       "female: ").upper()
        if gender == "M":
            is_male = True
            return is_male
        elif gender == "F":
            is_male = False
            return is_male


# get the subjects for the new student
def new_subjects():
    loop = False
    subject_list = ""
    while not loop:
        # Get one subject at a time so formatting will be the same
        add_subject = input("Enter one subject code or 'X' if all subjects have "
                            "been entered: ").upper()
        # Check if all subjects are entered
        if add_subject != "X":
            # Create the first subject in the list
            if subject_list == "":
                subject_list = add_subject
            # Add other subjects so all one line
            else:
                subject_list += f", {add_subject}"
        else:
            return subject_list


# number checking function
def int_check(question):
    valid = False
    error = "Please enter a valid number"
    while not valid:
        try:
            response = int(input(question))
            # If not a valid number
            if response <= 0:
                print(error)
            else:
                return response
        # if not a number print error
        except ValueError:
            print(error)


# Delete a student
def delete_student():
    print()
    print("-----------------------------------------------------")
    name = input("Enter the name: ").title()
    print("-----------------------------------------------------")
    find_pupil = False
    for pupil in student_list:
        if pupil.name == name:
            find_pupil = True
            # confirm they want to delete
            confirm_del = input(f"Type 'Y' if you want to delete {name} - or"
                                " any other key to go back to the "
                                "menu: ").upper()
            if confirm_del == "Y":
                student_list.remove(pupil)
                print(f"{name} has been deleted successfully")
    if not find_pupil:
        print("Oops, something went wrong! Nobody has that name")


# Find gender numbers
def count_gender():
    print()
    print("-----------------------------------------------------")
    gender = input("Enter the gender ('M' for male and 'F' for female): ")\
        .upper()
    print("-----------------------------------------------------")
    gender_list = []
    gender_count = 0
    # add the students which match the gender to a list
    for student in student_list:
        if gender == "M":
            if student.is_male:
                gender_list.append(student)
                gender_count += 1
        elif gender == "F":
            if student.is_male is False:
                gender_list.append(student)
                gender_count += 1

    # print list of students
    if len(gender_list) > 0:
        for students in gender_list:
            print(students.name)
        print(f"There is a total of {gender_count} students of this gender")
    else:
        print("Oops, something went wrong! That was not a gender")


# Menu function
def menu():
    new_action = True
    while new_action:
        print()
        print("-----------------------------------------------------")
        print("--------------------MAIN MENU------------------------")
        print()
        print("1. Get details of a particular student"
              "\n2. Print a full list of all students"
              "\n3. Print a list of students above a particular age"
              "\n4. Count students taking a particular subject"
              "\n5. Add a new student"
              "\n6. Delete a student"
              "\n7. Count students of a particular gender"
              "\n8. Print a full list of all teachers"
              "\n9. Exit")

        choice = input("\nWhat would you like to do? - enter a number: ")
        if choice == "1":
            find_student()
        elif choice == "2":
            print_student_details()
        elif choice == "3":
            select_student_age()
        elif choice == "4":
            count_students()
        elif choice == "5":
            new_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            count_gender()
        elif choice == "8":
            print_teacher_details()
        elif choice == "9":
            confirm = input("Type 'Y' if you want to exit the system - or any "
                            "other key to go back to the menu: ").upper()
            if confirm == "Y":
                print("Goodbye")
                new_action = False
        else:
            print("\n*** That was not a valid choice ***\n")


# MAIN ROUTINE
# Student list
student_list = []
student_subjects = []
teacher_list = []
generate_students()

# instantiate the teachers
Teachers("Baker", "GRA")
Teachers("Barker", "MAT")
Teachers("Graham", "BIO")
Teachers("Morgan", "DTC")
Teachers("Bell", "PHY")
Teachers("Nimmo", "ART")
Teachers("McNicol", "ENG")

# Call Main menu
menu()

# print_student_details()
# select_student_age()
# count_students()
# find_student()
# new_subjects()
