n = int(input("Enter number of terms: "))

x = 0

for i in range(n):
    x = x * 10 + 9
    print(x, end=" ")