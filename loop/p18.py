n = int(input("Enter N: "))
i = 1
a = 1
b = 2

while i <= n:
    print(a, end=" ")
    c = a * b
    a = b
    b = c
    i += 1