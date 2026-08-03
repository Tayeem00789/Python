field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
print(f"Total Harvest: {total}kg")
avg = total/5
print(f"Average Harvest in a field: {avg}kg")

price_per_kg = 15
earning = total * price_per_kg
print(f"Total Earning: {earning}taka")

bags = total // 25
print(f"Full bags packed: {bags}")

leftover = total%25
print(f"Remaining Grains: {leftover}kg")

Last_year = 500
print("Better than last year",total > Last_year)
print("Same as last year",total == Last_year)