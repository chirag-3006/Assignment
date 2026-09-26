for i in range(6):
    for j in range(11):
        if i+j==5 or (j>=5 and j-i==4+1) or (j>2 and i==3 and j<8):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
