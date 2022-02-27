""" Create a program for a small local library
25/02/22
By Amy Jorgensen
"""


class Students:
    def __init__(self, name, age, phone, form, subjects, gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.form = form
        self.subjects = subjects
        self.gender = gender
        self.enrolled = True

    def display_info(self):
        print()
        print(f"The personal details for {self.name} is shown below:"
              f"\nAge: {self.age}"
              f"\nPhone number: {self.phone}"
              f"\nForm class: {self.form}"
              f"\nGender: {self.gender}"
              f"\nEnrolled: {self.enrolled}"
              f"\nSubjects:")
        for subject in self.subjects:
            print(subject)


# MAIN ROUTINE
Students("Karen", "17", "123-4567", "WNLR", ["13DTC", "13SMX"], "Female")
Students("Bob", "18", "021-0263674", "BNNL", ["13SMX"], "Male")
Students("Lisa", "16", "022-4567123", "SKWR", ["13DTC", "13SMX"], "Female")
Students("Patrick", "18", "023-01234567", "SCBE", ["1ENG", "13CMX", "13"], "Male")
