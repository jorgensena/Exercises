""" Collect the times of a 200m race and find the fastest
Created by Amy Jorgensen
11/02/22
"""

times = []
time = int(input("Enter a time for the 200m race (or '-1' to exit): "))
total_t = 0
num = 0
fastest = 1000

# get times
while time != -1:
    times.append(time)

    if time < fastest:
        fastest = time

    total_t += time
    num += 1

    time = int(input("Enter a time for the 200m race (or '-1' to exit): "))


#calculate avg
avg_t = total_t / num

# output
for speed in times:
    print(speed)

print(f"The fastest time is: {fastest}s")
print(f"The average time is: {avg_t:.2f}s")
