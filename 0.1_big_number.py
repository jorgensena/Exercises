""" Output biggest number
Created by Amy Jorgensen
05/02/22
"""


# Get numbers
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# Loop until 0 entered
while num_1 != 0 and num_2 != 0:

    # FInd biggest/equal
    if num_1 > num_2:
        print("The biggest number is", num_1)
    elif num_2 > num_1:
        print("The biggest number is", num_2)
    else:
        print("Both these numbers are equal")

    # Get numbers
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))

print("Thank you for playing")
