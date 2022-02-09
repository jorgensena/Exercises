""" Calculate the volume of concrete needed for buildings and find the total
volume of concrete needed
Created by Amy Jorgensen
06/02/22
"""


# number checking function
def int_check(question, error, max):
    valid = False

    while not valid:
        try:
            response = float(input(question))
            # If not a valid number
            if response <= 0:
                print(error)
            elif max > 0:
                if response > max:
                    print(error)
                else:
                    return response
            else:
                return response
        # if not a number print error
        except ValueError:
            print(error)


def building():
    # Get building type and int check (using multi choice to remove possible
    # spelling errors)
    type = int_check("Enter the building type"
                     "\n1. Commercial"
                     "\n2. Residential"
                     "\n3. Exit"
                     "\n"
                     "\nEnter here: ", "Please enter a valid number, "
                                       "1, 2, or 3", 3)
    return type


t_vol = 0

# get building type
building_type = building()

# Set up loop
while building_type != 3:

    # Get lengths and int check
    length = int_check("Enter the length (m): ",
                       "Please enter a number higher than 0", 0)
    width = int_check("Enter the width (m): ",
                      "Please enter a number higher than 0", 0)

    # Depth values (m)
    depth = 0
    c_depth = 0.5
    r_depth = 0.25

    if building_type == 1:
        depth = c_depth
    else:
        depth = r_depth

    # calculate volume
    volume = length * width * depth

    # keep running total of volume
    t_vol += volume

    # Output building statement
    print("The volume of concrete required for a slab with the length of {}m,"
          "\nwidth of {}m, and a depth of {}m is {} cubic metres"
          .format(length, width, depth, volume))
    print()

    building_type = building()

# output final statement
print("The total amount of volume for today was {} cubic metres".format(t_vol))
