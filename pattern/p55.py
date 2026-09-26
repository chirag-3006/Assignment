


for i in range(1,6):
    for k in range(1,i+1):
        print(end=" ")
    t=65
    for j in range(1,7-i):
        print(chr(t),end="")
        t+=1
    print()