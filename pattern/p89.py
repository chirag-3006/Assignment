
for i in range(1,7):
    for j in range(1,12-i):
        print(end=" ")

    for k in range(1,2*i):
        if(k%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print()
