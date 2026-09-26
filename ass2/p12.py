num = int(input("Enter a 4 digit number: "))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10

reverse = d1 * 1000 + d2 * 100 + d3 * 10 + d4

print("Reversed number =", reverse)