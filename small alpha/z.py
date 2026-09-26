for i in range(5):
    for j in range(5):
        if (i%4==0) or i+j==4:
            print("*" ,end="")
        else:
            print(" ",end="")
    print()