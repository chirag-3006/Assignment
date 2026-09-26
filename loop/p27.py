n = int(input("Enter number of terms: "))

for i in range(n):
    if i % 2 == 0:
        print("*", end=" ")
    else:
        print("#", end=" ")