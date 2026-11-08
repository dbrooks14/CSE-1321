# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:3C
small = int(input("Enter the number of small sandwiches: "))
medium = int(input("Enter the number of medium sandwiches: "))
large = int(input("Enter the number of large sandwiches: "))
exlarge = int(input("Enter the number of extra-large sandwiches: "))
print()
print("You've entered " + str(small) + " small sandwiches.")
print("You've entered " + str(medium) + " medium sandwiches.")
print("You've entered " + str(large) + " large sandwiches.")
print("You've entered " + str(exlarge) + " extra-large sandwiches.")

small = small * 30
medium = medium * 60
large = large * 75
exlarge = exlarge * 135
totalmin = int((small + medium + large + exlarge) / 60)
totalsec = int((small + medium + large + exlarge) % 60)
print()
print("Total cooking time is " + str(totalmin) + " minutes " + "and " + str(totalsec) + " seconds." )
