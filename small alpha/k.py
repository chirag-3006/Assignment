for i in range(5):
    for j in range(11):
        if (j==0) or (i+j==3) or (j-i==-1) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
