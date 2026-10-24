
from datetime import datetime
import math

def calculate_parking_fee():
    print("===== SMART PARKING FEE MANAGEMENT =====")

    # Vehicle category and hourly rates
    rates = {
        "bike": 20,
        "car": 50,
        "truck": 100
    }

    vehicle = input("Enter vehicle category (bike/car/truck): ").lower()

    if vehicle not in rates:
        print("Invalid vehicle category!")
        return

    entry = input("Enter entry time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter exit time (YYYY-MM-DD HH:MM): ")

    # Validate date and time
    try:
        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        exit_time = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format!")
        return

    if exit_time <= entry_time:
        print("Error: Exit time must be after entry time.")
        return

    # Calculate parking duration
    duration = exit_time - entry_time
    total_minutes = duration.total_seconds() / 60
    hours = math.ceil(total_minutes / 60)

    # Calculate number of calendar days
    days = (exit_time.date() - entry_time.date()).days + 1

    # Calculate base parking fee
    hourly_rate = rates[vehicle]
    daily_limit = {
        "bike": 100,
        "car": 300,
        "truck": 600
    }

    fee = min(hours * hourly_rate, days * daily_limit[vehicle])

    # Overnight parking charge
    overnight_fee = 0
    if entry_time.date() != exit_time.date():
        overnight_fee = 50
        fee += overnight_fee

    # Penalty for parking longer than 24 hours
    penalty = 0
    if total_minutes > 24 * 60:
        penalty = 200
        fee += penalty

    # Display bill
    print("\n===== PARKING BILL =====")
    print("Vehicle category:", vehicle)
    print("Parking duration:", round(total_minutes / 60, 2), "hours")
    print("Charged hours:", hours)
    print("Base parking fee: Rs.", fee - overnight_fee - penalty)
    print("Overnight fee: Rs.", overnight_fee)
    print("Penalty: Rs.", penalty)
    print("Total amount: Rs.", fee)


calculate_parking_fee()
