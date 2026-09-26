n = 65

for i in range(1, 5):
    for j in range(2 * i - 1):
        print(chr(n), end="")
        n += 1
    print()