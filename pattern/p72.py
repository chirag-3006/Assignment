


for i in range(1,6):
    for j in range(1,i):
        print(end=" ")
    n=65
    for k in range((7-i),1,-1):
        print(chr(n),end=" ")
        n+=1
    print()