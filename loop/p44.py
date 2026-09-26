n = int(input("Enter a number: "))

last = n % 10

temp = n
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

power = 10 ** (count - 1)
first = n // power

middle = (n % power) // 10

result = last * power + middle * 10 + first

print("After interchange =", result)