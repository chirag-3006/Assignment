for i in range(7):
    for j in range(6):
        if (i%3==0) or (j==0 and i<3) or (j==5 and i>3):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
