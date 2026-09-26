cost = float(input("Enter cost price of bike: "))

if cost > 100000:
    tax = cost * 15 / 100
elif cost > 50000:
    tax = cost * 10 / 100
else:
    tax = cost * 5 / 100

print("Road tax =", tax)