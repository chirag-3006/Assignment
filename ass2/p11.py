age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ")
marital = input("Enter marital status (Y/N): ")

if sex == "F":
    print("She will work only in urban areas")
elif sex == "M" and age >= 20 and age < 40:
    print("He may work anywhere")
elif sex == "M" and age >= 40 and age <= 60:
    print("He will work in urban areas only")
else:
    print("ERROR")