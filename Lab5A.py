# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:5A
print("Please enter 10 numbers and this program will display the largest")

largest = 0

for j in range(10):
    num = int(input("Please enter number " + str(j+1) + ": "))
    if num > largest:
        largest = num
print("The largest numeber was " + str(largest))