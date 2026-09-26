for i in range(0,6):
    for k in range(5,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        if i == 5 or j==1 or i==j:
            print("1", end="")
        else:
            print(end="*")
    print()