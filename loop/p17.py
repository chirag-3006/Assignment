n = int(input("Enter N: "))
i = 1
num = 1
diff = 1

while i <= n:
    print(num, end=" ")
    num += diff
    diff += 1
    i += 1