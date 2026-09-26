n = int(input("Enter number of terms: "))

x = 0
sum = 0

for i in range(n):
    x = x * 10 + 1
    print(x, end=" ")
    sum = sum + x

print("\nSum =", sum)