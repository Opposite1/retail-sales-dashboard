#------------------------------------------------------
# Sales Report
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

sales = []

for day in days:
    sale = float(input(f"Enter {day} Sales: $"))
    sales.append(sale)

#------------------------------------------------------

daily_sales = float(input("Enter daily sales: $"))
hours_worked = float(input("Enter hours worked: "))
labor_cost = float(input("Enter labor cost: $"))

sales_per_hour = daily_sales / hours_worked
profit = daily_sales - labor_cost
total_sales = sum(sales)
average_sales = total_sales / len(sales)
best_days = max(sales)
worst_days = min(sales)

best_days_index = sales.index(best_days)
worst_days_index = sales.index(worst_days)

best_days_name = days[best_days_index]
worst_day_name = days[worst_days_index]

print("\nRetail Performance Dashboard")
print("----------------------------")

print("\nDAILY PERFORMANCE")
print("----------------------------")
print(f"Daily Sales: ${daily_sales:.2f}")
print("Hours Worked:", hours_worked)
print(f"Sales Per Hour: ${sales_per_hour:.2f}")
print(f"Profit: ${profit:.2f}")

print("\nWEEKLY PERFORMANCE")
print("----------------------------")
print(f"Weekly Sales: ${total_sales:.2f}")
print(f"Average Daily Sales: ${average_sales:.2f}")
print(f"Best Sales Day: {best_days_name} - ${best_days:.2f}")
print(f"Worst Sales Day: {worst_day_name} - ${worst_days:.2f}")

# Performance Rating
if sales_per_hour >= 250:
    rating = "Excellent"
elif sales_per_hour >= 200:
    rating = "Good"
elif sales_per_hour >= 100:
    rating = "Average"
else:
    rating = "Needs Improvement"

print("Performance Rating:", rating)

# Weekly Sales Goal
sales_goal = float(input("\nEnter weekly sales goal: $"))

if total_sales >= sales_goal:
    print("Congratulations! Weekly sales goal achieved!")
    print(f"Amount above goal: ${total_sales - sales_goal:.2f}")
else:
    print("Weekly sales goal not achieved.")
    print(f"Amount needed: ${sales_goal - total_sales:.2f}")

# Daily Sales Target
daily_goal = sales_goal / 7
print(f"Average Daily Goal: ${daily_goal:.2f}")

# Sales Trend Analysis
print("\nDAILY SALES CHANGES")
print("---------------------------")
for i in range(1, len(sales)):
    change = sales[i] - sales[i - 1]

    if change > 0:
        print(f"{days[i]}: Up ${change:.2f}")
    elif change < 0:
        print(f"{days[i]}: Down ${abs(change):.2f}")
    else:
        print(f"{days[i]}: No Change")