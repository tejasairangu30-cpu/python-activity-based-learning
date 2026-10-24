
# Multi-Plan Telecommunications Cost Optimization

plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "data": 2,
        "validity": 28,
        "call_minutes": 500,
        "extra_data_rate": 20,
        "extra_call_rate": 0.50
    },
    {
        "name": "Standard Plan",
        "price": 299,
        "data": 3,
        "validity": 28,
        "call_minutes": 1000,
        "extra_data_rate": 20,
        "extra_call_rate": 0.50
    },
    {
        "name": "Premium Plan",
        "price": 399,
        "data": 5,
        "validity": 56,
        "call_minutes": 1500,
        "extra_data_rate": 15,
        "extra_call_rate": 0.40
    },
    {
        "name": "Unlimited Plan",
        "price": 599,
        "data": 10,
        "validity": 84,
        "call_minutes": 2000,
        "extra_data_rate": 10,
        "extra_call_rate": 0.30
    }
]

# Get user requirements
data_used = float(input("Enter data usage in GB: "))
call_used = int(input("Enter call usage in minutes: "))
required_days = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget in rupees: "))

eligible_plans = []

print("\n----- MOBILE PLAN COMPARISON -----")

for plan in plans:
    # Calculate excess usage
    extra_data = max(0, data_used - plan["data"])
    extra_calls = max(0, call_used - plan["call_minutes"])

    # Calculate extra charges
    data_charge = extra_data * plan["extra_data_rate"]
    call_charge = extra_calls * plan["extra_call_rate"]

    total_cost = plan["price"] + data_charge + call_charge

    # Check validity and budget
    valid = plan["validity"] >= required_days
    within_budget = total_cost <= budget

    print(f"\nPlan: {plan['name']}")
    print(f"Base Price: Rs. {plan['price']:.2f}")
    print(f"Extra Data Charge: Rs. {data_charge:.2f}")
    print(f"Extra Call Charge: Rs. {call_charge:.2f}")
    print(f"Total Cost: Rs. {total_cost:.2f}")
    print(f"Validity: {plan['validity']} days")

    if valid and within_budget:
        eligible_plans.append((total_cost, plan["name"]))

# Identify the most economical eligible plan
print("\n----- OPTIMAL PLAN RESULT -----")

if eligible_plans:
    eligible_plans.sort()

    best_cost, best_name = eligible_plans[0]

    print("Most Economical Eligible Plan:", best_name)
    print(f"Total Cost: Rs. {best_cost:.2f}")

    print("\nOther Eligible Plans:")
    for cost, name in eligible_plans[1:]:
        print(f"{name}: Rs. {cost:.2f}")
else:
    print("No plan satisfies both validity and budget constraints.")
    print("Try increasing your budget or reducing required validity.")
