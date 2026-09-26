for i in range(5):
    for j in range(5):
        if (i==0 or i==2) or j==0 or (j==4 and i<3) or (j-i==0 and j>2):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
