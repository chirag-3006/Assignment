for i in range(5, 0, -1):
    for j in range(i):
        if (j==1 and i>2 and i<5) or (i==4 and j==2):
            print(end=" ")
        else:
            print("*", end="")
    print()
