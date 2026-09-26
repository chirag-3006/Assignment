



for i in range(1,6):
    for k in range(i,6):
        print(end=" ")
    for j in range(1,i+1):
           if(j==1 or i==5 or j==i):
                print('X',end=" ")
           else:
                print("_ ",end="")
    print()