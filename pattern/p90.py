
for i in range(1,8):

    # for k in range(1,8):
    #     print(end=" ")
    for j in range(1,7):
        if(i==7 and j==3):
            print(end=" ")
        elif (i%2!=0 and j==5) or (i==5 and j==4):
            print("*",end=" ")
        elif (i-j==4 or j-i==4 or (i==7 and j==1) or i==j)and (i!=5 ):
            print("*",end="")
        else:
            print(end=" ")
    print()