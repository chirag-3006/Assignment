age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

print("Oldest age =", oldest)
print("Youngest age =", youngest)