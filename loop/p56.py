start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    fact = 1
    
    for i in range(1, n + 1):
        fact = fact * i
    
    print("Factorial of", n, "=", fact)