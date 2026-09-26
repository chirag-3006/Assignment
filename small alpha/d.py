for i in range(5):
    for j in range(6):
        if (i==2 or i==4) or (j==5) or (j==0 and i>2) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
