""" Using multiple classes and showing how they interact with each other"""


# Setting up the class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    #method - to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # blank list to hold student details

    # method to add students to a course
    def add_student(self, student):
        # Test that there is room in the class
        if len(self.students) < self.max_students:
            self.students.append(student)  # add to class if room
            return True  # if student added successfully
        return False  # if student not added to course

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()  # using a method from the
            # student class. Could use student.grade above but using the
            # function is more effective and is more future proof - e.g.
            # in the event of a grade being determined a different way
            return total / len(self.students)


# MAIN ROUTINE

# instantiate 3 student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# instantiate course object
course1 = Course("Computer Science", 3)  # low max to test boundaries

# add students to course
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)  # try to add 3rd student

# Get the average grade of all the students in a course
print(f"The average grade in {course1.name} is {course1.get_average_grade()}")
