

for i in range(5):
    num = 1
    for k in range(1,7-i):
        print(end=" ")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)


    print()