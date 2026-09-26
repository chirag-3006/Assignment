
for i in range(1,6):
    for j in range(1,i):
        print(end=" ")
    n=1
    for k in range(2*(6-i),1,-1):
        if(i==1 or k==2*(6-i) or k==2):
         print(n,end="")
        else:
           print(end="+")
        n+=1
    print()