
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Fixed expenses
venue_cost = float(input("Enter venue rental cost: ₹"))
equipment_cost = float(input("Enter equipment cost: ₹"))
transport_cost = float(input("Enter transport cost: ₹"))

# Variable expenses
participants = int(input("Enter expected number of participants: "))
catering_per_person = float(input("Enter catering cost per participant: ₹"))
certificate_per_person = float(input("Enter certificate cost per participant: ₹"))

# Financial details
sponsorship = float(input("Enter sponsorship amount: ₹"))
registration_fee = float(input("Enter registration fee per participant: ₹"))
budget = float(input("Enter available budget excluding sponsorship: ₹"))

# Validate inputs
if (min(venue_cost, equipment_cost, transport_cost,
        catering_per_person, certificate_per_person,
        sponsorship, registration_fee, budget) < 0
        or participants < 0):
    print("Error: Costs, amounts, and participants cannot be negative.")

else:
    # Calculate expenses
    fixed_cost = venue_cost + equipment_cost + transport_cost
    variable_cost = (
        catering_per_person + certificate_per_person
    ) * participants

    total_cost = fixed_cost + variable_cost
    total_funding = budget + sponsorship
    participant_revenue = participants * registration_fee
    total_revenue = total_funding + participant_revenue

    # Calculate financial shortfalls
    sponsorship_shortfall = max(0, total_cost - sponsorship)
    budget_shortfall = max(0, total_cost - total_funding)
    final_balance = total_revenue - total_cost

    # Calculate minimum break-even registrations
    cost_per_participant = (
        catering_per_person + certificate_per_person
    )

    available_funding = budget + sponsorship

    if registration_fee <= cost_per_participant:
        if fixed_cost <= available_funding:
            break_even = 0
            print("\nBreak-even: Fixed costs are already covered.")
            if registration_fee < cost_per_participant:
                print("Warning: Each extra participant increases the loss.")
        else:
            break_even = None
            print("\nBreak-even cannot be reached with this fee.")
    else:
        required = max(0, fixed_cost - available_funding)
        break_even = (
            required + (registration_fee - cost_per_participant) - 1
        ) // (registration_fee - cost_per_participant)

    # Display report
    print("\n===== EVENT FINANCIAL REPORT =====")
    print(f"Fixed expenses: ₹{fixed_cost:.2f}")
    print(f"Participant expenses: ₹{variable_cost:.2f}")
    print(f"Total event cost: ₹{total_cost:.2f}")
    print(f"Sponsorship received: ₹{sponsorship:.2f}")
    print(f"Registration revenue: ₹{participant_revenue:.2f}")
    print(f"Total available budget + sponsorship: ₹{total_funding:.2f}")
    print(f"Sponsorship-only shortfall: ₹{sponsorship_shortfall:.2f}")
    print(f"Funding shortfall before registrations: ₹{budget_shortfall:.2f}")
    print(f"Final surplus / deficit: ₹{final_balance:.2f}")

    if break_even is not None:
        print(f"Minimum break-even registrations: {break_even}")

        if participants >= break_even:
            print("Status: Break-even target achieved.")
        else:
            print(f"Additional registrations needed: {break_even - participants}")
    else:
        print("Consider increasing the registration fee or reducing costs.")
