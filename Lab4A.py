# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:4A
grade = float(input("Enter your grade: "))
if grade >97:
    print("Letter grade is: A+")
elif grade > 94 or grade == 97:
    print("Letter grade is: A")
elif grade > 91 or grade == 94:
    print("Letter grade is: A-")
elif grade > 88 or grade == 91:
    print("Letter grade is: B+")
elif grade > 85 or grade == 88:
    print("Letter grade is: B")
elif grade > 82 or grade == 85:
    print("Letter grade is: B-")
elif grade > 79 or grade == 82:
    print("Letter grade is: C+")
elif grade > 76 or grade == 79:
    print("Letter grade is: C")
elif grade > 73 or grade == 76:
    print("Letter grade is: C-")
elif grade > 70 or grade == 73:
    print("Letter grade is: D+")
elif grade > 67 or grade == 70:
    print("Letter grade is: D")
elif grade > 64 or grade == 67:
    print("Letter grade is: D-")
elif grade <= 64:
    print("Letter grade is: F")