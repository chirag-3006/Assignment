choice = input("Enter choice (+, >, ==): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "+":
    print("Addition =", num1 + num2)
elif choice == ">":
    if num1 > num2:
        print(num1, "is greater")
    elif num2 > num1:
        print(num2, "is greater")
    else:
        print("Both numbers are equal")
elif choice == "==":
    if num1 == num2:
        print("Both numbers are equal")
    else:
        print("Both numbers are not equal")
else:
    print("Invalid choice")