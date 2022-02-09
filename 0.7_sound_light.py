""" Calculate the distance of lightning
Created by Amy Jorgensen
08/02/22
"""

# speed of sound
sound = 340

# Get time difference
time = float(input("How many seconds between the lightning and thunder was "
                 "there?: "))

# Calculate the distance and convert to km
distance = (time * sound) / 1000

# Output answer
print("The lightning was {:.2f}km away from you".format(distance))
