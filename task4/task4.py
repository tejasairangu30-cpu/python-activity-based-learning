# Multi-Stage ATM Transaction Audit

accounts = {
    "A101": 5000,
    "A102": 3000,
    "A103": 2000
}

transactions = [
    ("A101", "deposit", 1000, None),
    ("A101", "withdraw", 500, None),
    ("A101", "withdraw", 7000, None),
    ("A102", "transfer", 500, "A103"),
    ("A102", "transfer", 500, "A103"),
    ("A102", "transfer", 500, "A103"),
    ("A103", "deposit", -200, None),
    ("A101", "withdraw", 1000, None)
]

invalid_transactions = []
suspicious_transactions = []
withdrawal_history = {}
transfer_history = {}

print("===== ATM TRANSACTION AUDIT =====")

for i, transaction in enumerate(transactions, start=1):
    account, action, amount, target = transaction

    print(f"\nTransaction {i}: {action} Rs.{amount}")

    # Check account existence
    if account not in accounts:
        print("Invalid: Account does not exist.")
        invalid_transactions.append(i)
        continue

    # Check valid amount
    if amount <= 0:
        print("Invalid: Amount must be positive.")
        invalid_transactions.append(i)
        continue

    if action == "deposit":
        accounts[account] += amount
        print("Deposit successful.")

    elif action == "withdraw":
        if amount > accounts[account]:
            print("Invalid: Insufficient balance.")
            invalid_transactions.append(i)
            continue

        accounts[account] -= amount

        withdrawal_history.setdefault(account, []).append(amount)

        # Detect repeated withdrawals
        if len(withdrawal_history[account]) >= 3:
            if len(set(withdrawal_history[account][-3:])) == 1:
                print("Suspicious: Three repeated withdrawals.")
                suspicious_transactions.append(i)

        print("Withdrawal successful.")

    elif action == "transfer":
        if target not in accounts:
            print("Invalid: Receiver account does not exist.")
            invalid_transactions.append(i)
            continue

        if account == target:
            print("Invalid: Cannot transfer to the same account.")
            invalid_transactions.append(i)
            continue

        if amount > accounts[account]:
            print("Invalid: Insufficient balance.")
            invalid_transactions.append(i)
            continue

        accounts[account] -= amount
        accounts[target] += amount

        key = (account, target, amount)
        transfer_history[key] = transfer_history.get(key, 0) + 1

        # Detect repeated identical transfers
        if transfer_history[key] >= 3:
            print("Suspicious: Repeated identical transfers.")
            suspicious_transactions.append(i)

        print("Transfer successful.")

    else:
        print("Invalid: Unknown transaction type.")
        invalid_transactions.append(i)
        continue

    print("Updated balances:", accounts)

# Final audit report
print("\n===== FINAL AUDIT REPORT =====")

print("\nFinal Account Balances:")
for account, balance in accounts.items():
    print(account, ":", "Rs.", balance)

print("\nInvalid Transaction Numbers:", invalid_transactions)
print("Suspicious Transaction Numbers:", suspicious_transactions)

print("\nAudit completed.")

