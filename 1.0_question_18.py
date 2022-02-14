""" Collect the times of a race and find the fastest
Version 2
Created by Amy Jorgensen
14/02/22
"""


# number checking function
def int_check(question, min, max):
    valid = False
    error = "Please enter a valid number"
    while not valid:
        try:
            response = float(input(question))
            # Check number is within the range
            if max != 0:
                if response <= min or response >= max:
                    print(error)
                    print()
                else:
                    return response
            elif min != 0:
                if response <= min or response == 0:
                    print(error)
                    print()
                else:
                    return response
        # if not a number print error
        except ValueError:
            print(error)
            print()


# time input function
def get_times():
    times = []
    time = int_check("Enter a time (s) for the race (or '-1' to exit)"
                     ": ", -2, 0)
    # get times
    while time != -1:
        times.append(time)
        time = int_check("Enter a time (s) for the race (or '-1' to "
                         "exit): ", -2, 0)

    return times


# calculate average function
def get_avg(list):
    t_num = 0
    t_speed = 0
    for speed in list:
        t_num += 1
        t_speed += speed

    avg = t_speed / t_num
    return avg


# list printing function
def print_list(speeds, fast_speed, avg_speed, race):
    # print info
    print()
    if len(speeds) >= 1:
        print(f"The times for the {race}m race:")
        for speed in speeds:
            print(f"{speed:.0f}s")
        print()
        print(f"The fastest time in the {race}m race was "
              f"{fast_speed:.0f}s")
        print(f"The average speed for the {race}m race was "
              f"{avg_speed:.0f}s")
    else:
        print("No times have been input for this race")


# MAIN ROUTINE
print("Welcome to the program that will simplify your life :)")
print()

# Option menu
# variables
times_100 = []
fast_100 = 9999999
avg_100 = 0

times_200 = []
fast_200 = 9999999
avg_200 = 0

times_400 = []
fast_400 = 9999999
avg_400 = 0

choice = 0
while choice != 4:
    print()
    choice = int_check("What would you like to do?"
                       "\n1. Enter in times for a race"
                       "\n2. View the times for an event"
                       "\n3. Delete a times list"
                       "\n4. Exit the program"
                       "\n: ", 0, 5)

    if choice == 1:
        race_input = 0
        while race_input != 4:
            # Get what race user wants to input
            print()
            race_input = int_check("What race would you like to input "
                                   "times for?"
                                   "\n1. 100m"
                                   "\n2. 200m"
                                   "\n3. 400m"
                                   "\n4. Go back to option menu"
                                   "\n: ", 0, 5)

            # get the 100m race times
            if race_input == 1:
                # get times
                times_100 = get_times()
                # calculate fastest and avg time
                fast_100 = min(times_100)
                avg_100 = get_avg(times_100)

            # Get the 200m race times
            elif race_input == 2:
                # get times
                times_200 = get_times()
                # calculate fastest and avg time
                fast_200 = min(times_200)
                avg_200 = get_avg(times_200)

            # Get the 400m race times
            elif race_input == 3:
                # get times
                times_400 = get_times()
                # calculate fastest and avg time
                fast_400 = min(times_400)
                avg_400 = get_avg(times_400)

            # Break the loop
            elif race_input == 4:
                break

    # If user wants to view the race times
    elif choice == 2:
        view_race = 0
        while view_race != 4:
            print()
            # get what list the user wants to print
            view_race = int_check("What race would you like to view?"
                                  "\n1. 100m"
                                  "\n2. 200m"
                                  "\n3. 400m"
                                  "\n4. Go back to option menu"
                                  "\n: ", 0, 5)

            # print the list wanted
            if view_race == 1:
                print_list(times_100, fast_100, avg_100, 100)

            elif view_race == 2:
                print_list(times_200, fast_200, avg_200, 200)

            elif view_race == 3:
                print_list(times_400, fast_400, avg_400, 400)

            elif view_race == 4:
                break

    # If the user wants to delete a list
    elif choice == 3:
        delete_race = 0
        while delete_race != 4:
            print()
            # get what list the user wants to delete
            delete_race = int_check("What race would you like to delete?"
                                    "\n1. 100m"
                                    "\n2. 200m"
                                    "\n3. 400m"
                                    "\n4. Go back to option menu"
                                    "\n: ", 0, 5)

            # delete the chosen list
            if delete_race == 1:
                times_100.clear()
                fast_100 = 9999999
                avg_100 = 0
                print("The times for the 100m race have been deleted")

            elif delete_race == 2:
                times_200.clear()
                fast_200 = 9999999
                avg_200 = 0
                print("The times for the 200m race have been deleted")

            elif delete_race == 3:
                times_400.clear()
                fast_400 = 9999999
                avg_400 = 0
                print("The times for the 400m race have been deleted")

            elif delete_race == 4:
                break
