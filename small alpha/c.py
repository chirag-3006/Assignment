for i in range(3):
    for j in range(4):
        if (i==0 or i==2) or (j==0) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
