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
worst_days_inex = sales. index(worst_days)

best_days_name = days[best_days_index]
worst_day_name = days[worst_days_inex]

print("\nRetail Performance Dashboard")
print("----------------------------")

print("\nDAILY PERFORMANCE")
print("----------------------------")
print("Daily Sales: $", daily_sales)
print("Hours Worked:", hours_worked)
print("Sales Per Hour: $", round(sales_per_hour, 2))
print("Profit: $", profit)

print("\nWEEKLY PERFORMANCE")
print("----------------------------")
print("Weekly Sales: $", total_sales)
print("Average Daily Sales: $", round(average_sales, 2))
print("Best Sales Day:", best_days_name, "- $", best_days)
print("Worst Sales Day: $", worst_day_name, "- $", worst_days)

# Performance Rating
if sales_per_hour >= 200:
    rating = "Excellent"
elif sales_per_hour >= 250:
    rating = "Good"
elif sales_per_hour >= 100:
    rating = "Average"
else:
    rating = "Needs Improvement"

print("Performance Rating:", rating)