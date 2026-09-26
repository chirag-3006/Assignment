for i in range(8):
    for j in range(10):
        if (i==j or i+j==8) and i<4 or (j==4 and i>3):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
