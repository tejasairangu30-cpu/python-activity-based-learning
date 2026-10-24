# Employee Payroll and Deduction Analysis

# Read employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross_salary = basic + allowances + overtime + incentives

# Calculate progressive deductions
if gross_salary <= 20000:
    tax = gross_salary * 0.05
elif gross_salary <= 50000:
    tax = (20000 * 0.05) + ((gross_salary - 20000) * 0.10)
else:
    tax = (20000 * 0.05) + (30000 * 0.10)
    tax += (gross_salary - 50000) * 0.15

# Other deductions
pf = basic * 0.12
total_deductions = tax + pf

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name     :", name)
print("Employee ID       :", emp_id)
print("--------------------------------------")
print("Basic Salary      : Rs.", round(basic, 2))
print("Allowances        : Rs.", round(allowances, 2))
print("Overtime          : Rs.", round(overtime, 2))
print("Incentives        : Rs.", round(incentives, 2))
print("--------------------------------------")
print("Gross Salary      : Rs.", round(gross_salary, 2))
print("Income Tax        : Rs.", round(tax, 2))
print("PF Deduction      : Rs.", round(pf, 2))
print("Total Deductions  : Rs.", round(total_deductions, 2))
print("--------------------------------------")
print("Net Salary        : Rs.", round(net_salary, 2))
print("======================================")

