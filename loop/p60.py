import math

n = int(input("Enter N: "))

for i in range(1, n + 1):
    print("Number =", i)
    print("Square =", i ** 2)
    print("Cube =", i ** 3)
    print("Square Root =", math.sqrt(i))
    print()