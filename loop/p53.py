start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    temp = n
    sum = 0
    
    while temp > 0:
        digit = temp % 10
        
        fact = 1
        
        for i in range(1, digit + 1):
            fact = fact * i
        
        sum = sum + fact
        temp = temp // 10
    
    if sum == n:
        print(n, end=" ")