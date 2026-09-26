
for i in range(1,5):
    for j in range(1,7-i):
        print(end=" ")
    for k in range(1,2*i):
        print(end="*")
    print()


for i in range(i,1,-1):
    for j in range(7-i):
        print(end=" ")
    for k in range(2*(i-1),1,-1):
        print(end="*")
    print()