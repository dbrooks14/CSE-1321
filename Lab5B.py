# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:5B
size = int(input("Please enter a value for the size: "))

print("This is the requested " + str(size) + "x" + str(size) + " box:")

for j in range(size):
    for i in range(size):
        print("*", end="")
    print()

print("This is the requested right-facing " + str(size) + "x" + str(size) + " right-triangle:")

for j in range(size):
    for i in range(j+1):
        print("*", end="")
    print()

print("This is the requested left-facing " + str(size) + "x" + str(size) + " right-triangle:")

for j in range(size):
    for k in range(size-j-1):
        print(" ", end="")
    for i in range(j+1):
        print("*", end="")
    print()
