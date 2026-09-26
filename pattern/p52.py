


for i in range(1,6):
    for k in range(1,i+1):
        print(end=" ")
    for j in range(1,7-i):
        if(j==1 or j==6-i or i==1 ):
         print(j,end="")
        else:
           print("_",end="")
   
    print()