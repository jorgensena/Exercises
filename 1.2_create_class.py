"""Creating a class
"""
class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour


    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"


# MAIN ROUTINE
dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

