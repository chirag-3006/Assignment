

t=65
for i in range(1,6):
    for j in range(1,7-i):
        print(end=" ")
    for k in range(1,i+1):
        if i==5:
           print("E"*2,end="")
        elif(k==1 or k==i):
            print(chr(t),end=" ")    
        else:
            print(end=" ")
    t+=1
    print()