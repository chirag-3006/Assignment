for i in range(0,6):
    for j in range(1,i+1):
        if i == 5 or j==1 or i==j:
            print(chr(64+j), end="")
        else:
            print(end=" ")
    print()