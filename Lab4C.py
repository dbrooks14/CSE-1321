# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:4C
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))


if side1 <=0 or side2 <=0 or side3 <=0:
    print("Invalid input. All sides must be greater than 0.")

elif (side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2):
    print("The sides do not form a valid triangle.")

elif side1 == side2 and side1 == side3 and side2 == side3:
    print("The triangle is an equilateral triangle.")

elif (side1 == side2 or side2 == side3 or side1 == side3) and (side1 != side3 or side2 != side1):
    print("This triangle is an isosceles triangle.")

else:
    print("This triangle is a scalene triangle.")