for i in range(5):
    for j in range(6):
        if (i==0 or i==4) or (j==0 or j==5) or (i==j-1):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
