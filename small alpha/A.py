for i in range(4):
    for j in range(9):
        if ( ((i==0 or i==2) and (j<5)) or (i==1 and (j==0 or j==4))):
            print("*" ,end="")
        elif(((i>3 and i<5) or j-i==4)):
            print("*" ,end="")

        else:
            print(" ",end="")
    print()
