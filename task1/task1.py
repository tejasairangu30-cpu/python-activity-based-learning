
def calculate_bill(units):
    if units < 0:
        return None

    energy_charge = 0

    # First 100 units
    energy_charge += min(units, 100) * 2

    # Units from 101 to 200
    if units > 100:
        energy_charge += min(units - 100, 100) * 3

    # Units from 201 to 500
    if units > 200:
        energy_charge += min(units - 200, 300) * 5

    # Units above 500
    if units > 500:
        energy_charge += (units - 500) * 7

    fixed_charge = 100
    surcharge = energy_charge * 0.05

    # Rebate for low consumption
    if units <= 100:
        rebate = energy_charge * 0.10
    else:
        rebate = 0

    total_bill = (
        energy_charge
        + fixed_charge
        + surcharge
        - rebate
    )

    return {
        "units": units,
        "energy_charge": energy_charge,
        "fixed_charge": fixed_charge,
        "surcharge": surcharge,
        "rebate": rebate,
        "total_bill": total_bill
    }


# Monthly electricity consumption
monthly_units = {
    "January": 90,
    "February": 110,
    "March": 130,
    "April": 250,
    "May": 400
}

monthly_bills = {}

for month, units in monthly_units.items():
    bill = calculate_bill(units)
    monthly_bills[month] = bill["total_bill"]

    print(f"\n{month}")
    print(f"Units consumed: {units}")
    print(f"Energy charge: ₹{bill['energy_charge']:.2f}")
    print(f"Fixed charge: ₹{bill['fixed_charge']:.2f}")
    print(f"Surcharge: ₹{bill['surcharge']:.2f}")
    print(f"Rebate: ₹{bill['rebate']:.2f}")
    print(f"Total bill: ₹{bill['total_bill']:.2f}")


# Compare consecutive monthly bills
print("\nMONTHLY BILL COMPARISON")

previous_bill = None

for month, bill_amount in monthly_bills.items():
    if previous_bill is not None:
        increase = bill_amount - previous_bill
        percentage = (
            (increase / previous_bill) * 100
            if previous_bill != 0 else 0
        )

        print(
            f"{month}: Change = ₹{increase:.2f}, "
            f"{percentage:.1f}%"
        )

        if percentage > 30:
            print("Warning: Unusual increase in bill!")

    previous_bill = bill_amount
