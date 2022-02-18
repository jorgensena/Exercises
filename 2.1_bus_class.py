""" Using multiple classes and showing how they interact with each other"""


# Setting up the class
class Bus:
    bus_list = []

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def print_details(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"The bus {bus.number} on route {bus.route} has driver "
                      f"{bus.driver}")


# MAIN ROUTINE

# instantiate 3 student objects
b1 = Bus(2010, "Y", "George")
b2 = Bus(2015, "100", "Billy")
b3 = Bus(2014, "130", "Sheila")

# print details
for bus in range(len(Bus.bus_list)):
    Bus.print_details(Bus.bus_list[bus])


