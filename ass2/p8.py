held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))
medical = input("Do you have medical cause? (Y/N): ")

percentage = attended / held * 100

print("Attendance percentage =", percentage)

if percentage >= 75 or medical == "Y":
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")