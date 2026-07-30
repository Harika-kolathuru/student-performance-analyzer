name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
science = float(input("Enter Science marks: "))

total = maths + python + science
average = total / 3

print("\n--- Student Performance ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")
