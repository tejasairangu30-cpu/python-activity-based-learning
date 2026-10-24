
# Campus Event Seating and Entry Validation System

# Nested lists representing seating rows
seating = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"]
]

# Registration IDs of valid participants
registrations = {
    "REG101": "Sai",
    "REG102": "Ravi",
    "REG103": "Teja",
    "REG104": "Priya",
    "REG105": "Arjun",
    "REG106": "Kiran",
    "REG107": "Anu",
    "REG108": "Rahul"
}

# Store allocated seats and entry records
seat_assignments = {}
entered_tickets = set()

# Assign seats to registered participants
all_seats = [seat for row in seating for seat in row]

for i, reg_id in enumerate(registrations):
    seat_assignments[reg_id] = all_seats[i]

print("===== CAMPUS EVENT SEATING SYSTEM =====")

print("\nSEATING ASSIGNMENTS")
for reg_id, seat in seat_assignments.items():
    print(reg_id, "->", seat, "-", registrations[reg_id])

# Ticket validation and entry checking
print("\n===== TICKET ENTRY VALIDATION =====")

tickets_to_check = [
    "REG101",
    "REG102",
    "REG101",
    "REG110",
    "REG105",
    "REG108"
]

valid_entries = 0
duplicate_entries = 0
invalid_tickets = 0

for ticket in tickets_to_check:
    if ticket not in registrations:
        print(ticket, ": INVALID TICKET")
        invalid_tickets += 1

    elif ticket in entered_tickets:
        print(ticket, ": DUPLICATE ENTRY DETECTED")
        duplicate_entries += 1

    else:
        entered_tickets.add(ticket)
        valid_entries += 1
        print(ticket, ": ENTRY APPROVED")

# Calculate seating capacity
total_seats = len(all_seats)
booked_seats = len(seat_assignments)
available_seats = total_seats - booked_seats

print("\n===== EVENT SUMMARY =====")
print("Total Seating Capacity:", total_seats)
print("Registered Participants:", len(registrations))
print("Seats Allocated:", booked_seats)
print("Available Seats:", available_seats)
print("Successful Entries:", valid_entries)
print("Duplicate Entries:", duplicate_entries)
print("Invalid Tickets:", invalid_tickets)
