




for i in range(1,5):
    for j in range(1,i+1):
        if(j==1 or j==i):
           print(j,end="")
        else:
            print(end=" ")
    print()
    
for j in range(i,1,-1):
    for k in range(1,j):
         if(k==1 or k==j-1):
           print(k,end="")
         else:
             print(end=" ")
    print()