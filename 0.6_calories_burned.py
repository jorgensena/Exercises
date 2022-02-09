""" Find the kgs a person has burned from the sports: biking, jogging or
swimming
Created by Amy Jorgensen
08/02/22
"""

# setup variables
cal_hr_biking = 200
cal_hr_jogging = 475
cal_hr_swimming = 275

weight_cal = 3500 / 0.454

# Get inputs
biking = int(input("Enter the hours spent biking: "))
jogging = int(input("Enter the hours spent jogging: "))
swimming = int(input("Enter the hours spent swimming: "))

# Calculations
cal_hr_b = 200 * biking
cal_hr_j = 475 * jogging
cal_hr_s = 275 * swimming

t_cal = cal_hr_s + cal_hr_j + cal_hr_b

kilo_burn = t_cal / weight_cal

# Output
print("{:.3f}".format(kilo_burn))
