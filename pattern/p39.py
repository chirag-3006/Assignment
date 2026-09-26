
for i in range(0,6):
  t=i
  for j in range(6-i,0,-1):
        if i%2==1:
            print(j,end=" ")
        else:
            t+=1
            print(t,end=" ")
  print()