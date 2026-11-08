# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Assignment:3A
size = int(input("Enter an odd number for the size of the diamond: "))
half = size // 2
number = 0

if size % 2 == 0:
    print("Size must be an odd number; we will increase it to", size + 1)
    size += 1

for i in range(half + 1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print(number % 10, end="")
        number += 1
    print()

for i in range(half - 1, -1, -1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print(number % 10, end="")
        number += 1
    print()
