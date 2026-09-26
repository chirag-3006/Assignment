for i in range(5):
    for j in range(9):
        if (i==0 or i==4) and j<5 or (j==0) or (j==4 or j==8) and i>1  or (i==2 and j>4):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
