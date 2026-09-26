salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 5 / 100
else:
    bonus = 0

print("Net bonus amount =", bonus)