"""Creating a class
"""
class Dog:
    def bark(self):
        print("Bark")

# MAIN ROUTINE
# instantiate a new instance of the class Dog
spot = Dog()  # spot is now apart of the class Dog (an instance of it)
print(type(spot))

spot.bark()  # Call the bark method on spot
