""" Output the numbers between the chosen values and their sum
Created by Amy Jorgensen
06/02/22
"""


# Get number values
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the end number: "))

sum = 0

# Print consecutive numbers between and including entered values
for i in range(start_number, end_number + 1):
    print(i)
    sum += i

# print final sum
print("The total sum of these numbers is", sum)
