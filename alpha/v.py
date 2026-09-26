for i in range(6):
    for j in range(11):
        if (i==j or j+i==10) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
