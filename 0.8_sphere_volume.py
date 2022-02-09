""" Calculate the volume of a sphere
Created by Amy Jorgensen
09/02/22
"""
import math

# Get pi value
pi = math.radians(180)

# Get radius
radius = int(input("Enter the radius of the sphere: "))

# Calculate volume
volume = 4 / 3 * pi * (radius ** 3)

# Calculate surface area
area = 4 * pi * (radius ** 2)

# Output info
print("The volume is {:.2f} cubic cm".format(volume))
print("The surface area is {:.2f} square cm".format(area))
