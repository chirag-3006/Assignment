held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))

percentage = attended / held * 100

print("Attendance percentage =", percentage)

if percentage >= 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")