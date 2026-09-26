

for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    t=65
    for k in range(2*i-1):
        print(chr(t),end="")
        t+=1
    print()