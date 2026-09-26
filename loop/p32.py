n = int(input("Enter number of terms: "))

for i in range(n):
    ch = chr(65 + i)
    
    if i % 2 == 0:
        print(ch.upper(), end=" ")
    else:
        print(ch.lower(), end=" ")