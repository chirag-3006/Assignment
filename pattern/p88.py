


for i in range(1,10):
    for j in range(1,10):
        if (i==5 and j<=5):
            print(j,end="")
            
        elif (j==3 and i<=4):
            print(i,end="")
           
        elif (j==3 and i>5):
            print((10)-i,end="")
            
        elif (i==5 and j>5):
            print((10+1)-j,end="")
            
        else:
            print(" ",end="")
    print()