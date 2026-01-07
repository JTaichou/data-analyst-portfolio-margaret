expenses = [
    {"date": "2026-01-01", "category": "food", "amount": 800},
    {"date": "2026-01-02", "category": "transport", "amount": 150},
    {"date": "2026-01-03", "category": "games", "amount": 2000},
    {"date": "2026-01-04", "category": "food", "amount": 600},
    {"date": "2026-01-05", "category": "cat food", "amount": 1200},
    {"date": "2026-01-06", "category": "food", "amount": 700},
    {"date": "2026-01-07", "category": "transport", "amount": 200},
    {"date": "2026-01-08", "category": "games", "amount": 900},
    {"date": "2026-01-09", "category": "food", "amount": 1300},
    {"date": "2026-01-10", "category": "cat food", "amount": 3000},
]

# Total expenses amount
total_amount = sum(item["amount"] for item in expenses)

# Average daily expense
average_per_day = total_amount / len(expenses)

# Maximum expense
max_expense = max(expenses, key=lambda x: x["amount"])

# Output
print("📊 Expense Report")
print("-" * 30)
print(f"Total expenses: {total_amount} ₽")
print(f"Average daily expense: {average_per_day:.2f} ₽")
print(
    f"Highest expense: {max_expense['amount']} ₽ "
    f"(category: {max_expense['category']}, date: {max_expense['date']})"
)