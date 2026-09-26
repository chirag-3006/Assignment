start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    print("Table of", i)
    
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    
    print()