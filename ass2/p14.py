percentage = float(input("Enter percentage: "))

if percentage > 90:
    print("Grade A")
elif percentage > 80:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
else:
    print("Grade D")