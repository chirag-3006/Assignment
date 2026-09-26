for i in range(6):
    for j in range(5):
        if(i==5 and j<=1):
            print(end="*")
        elif (j==2 and i!=1) :
            print("*" ,end="")
        else:
            print(end=" ")
    print()
