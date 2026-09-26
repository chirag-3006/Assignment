


n=5

for i in range(1,6):
    for j in range(1,i):
        print(end=" ")
    for k in range((7-i),1,-1):
        print(n,end=" ")
    print()
    n=n-1