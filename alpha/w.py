for i in range(6):
    for j in range(11):
        if (j==0 or j==10) or (i+j==5 or j-i==5) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
