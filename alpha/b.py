"""for i in range(5):
    for j in range(6):
        if (i==0 or i==2 or i==4) or (j==0) or (j==5 and i+j==10) :
            print("*" ,end="")
        else:
            print(" ",end="")
    print()
"""
for i in range (1,6):
    for j in range(1,6):
        if(i%2==0 and j<5 and j>1) or (i%2==1 and j==5):
            print(end="  ")
        else:
            print(end="* ")
    print()
    