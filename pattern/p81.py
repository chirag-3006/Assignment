


for i in range(1,5):
    for j in range(1,7-i):
        print(end=" ")
    for k in range(1,i+1):
        if(k==i):
            print("*",end="")
        else:
           print(end="*_")
    print()


for i in range(i,1,-1):
    for j in range(1,8-i):
        print(end=" ")
    for k in range(i,1,-1):
        if(k==2):
         print("*",end="")
        else:
         print(end="*_")
    print()

    """
for i in range(1,5):
    for j in range(1,7-i):
        print(end=" ")
    for k in range(1,i+1):
        if(k==i):
            print("*",end="")
        else:
           print(end="*_")
    print()


for i in range(i-1,1,-1):
    for j in range(1,8-i):
        print(end=" ")
    for k in range(i,1,-1):
        if(k==2):
         print("*",end="")
        else:
         print(end="*_")
    print()
    """