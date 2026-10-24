# Multi-Day Water Tank Simulation

capacity = int(input("Enter tank capacity: "))
initial_level = int(input("Enter initial water level: "))
days = int(input("Enter number of days: "))
threshold = int(input("Enter target water level: "))

level = initial_level
first_interval = -1

if capacity <= 0 or days <= 0:
    print("Invalid tank capacity or number of days")
elif initial_level < 0 or initial_level > capacity:
    print("Invalid initial water level")
elif threshold < 0 or threshold > capacity:
    print("Invalid threshold")
else:
    for day in range(1, days + 1):
        inflow = int(input(f"Day {day} inflow: "))
        outflow = int(input(f"Day {day} outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid input: quantities cannot be negative")
            break

        level = level + inflow - outflow

        if level > capacity:
            print(f"Day {day}: Overflow of {level - capacity} liters")
            level = capacity

        elif level < 0:
            print(f"Day {day}: Shortage of {-level} liters")
            level = 0

        print(f"Day {day}: Water level = {level} liters")

        if first_interval == -1 and level >= threshold:
            first_interval = day

    else:
        if first_interval != -1:
            print("Threshold first reached on day:", first_interval)
        else:
            print("Threshold was not reached.")
