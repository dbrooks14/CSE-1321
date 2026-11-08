#Class:CSE 1321L
#Section:B10
#Term:Fall 2026
#Instructor:Lan Vu
#Name:Dyllan Brooks
#Lab:6C

while True:
    rows = int(input("Enter the number of rows or 0 to quit: "))

    if rows == 0:
        break
    for i in range(1, rows+1):
        for j in range(rows-i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2,i +1):
            print(j, end="")
        print()