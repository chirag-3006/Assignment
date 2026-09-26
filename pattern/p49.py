for i in range(0,5):
    for k in range(5,i,-1):
        print(end=" ")
    for j in range(-1,i):
        print(j % 2, end="")
    print()
