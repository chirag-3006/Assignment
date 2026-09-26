





for i in range(1,5):
    for j in range(1,6-i):
        print(end=" ")
    for k in range(1,i+1):
         print(k,end="")
    print()

for n in range(i,1,-1):
    for j in range(5,n-1,-1):
        print(end=" ")
    for k in range(1,n):
         print(k,end="")
    print()