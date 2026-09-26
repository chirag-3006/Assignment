n = int(input("Enter N: "))
i = 1
count = 0

while count < n:
    if i % 2 != 0:
        print(i, end=" ")
        count += 1
    i += 1