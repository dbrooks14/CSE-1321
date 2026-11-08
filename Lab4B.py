# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:4B
print("Welcome!")
num = float(input("Please input a number: "))
inverse = num*-1
square = num**2
cube = num**3
exit = ("Thank you, goodbye!")
selection = input("What would you like to do with this number?: \n0) Get the additive inverse of the number\n1) Get the reciprocal of the number\n2) Square the number\n3) Cube the number\n4) Exit the program\n")
if int(selection) < 0 or int(selection) > 4:
    print("Invalid option!")
match selection:
    case "0":
        print("The additive inverse of " + str(num) +" is " + str(inverse))
    case "1":
        if num == 0:
            print("Cannot divide by zero!")
        else:
            reciprocal = 1 / num
            print("The reciprocal of " + str(num) + " is " + str(round(reciprocal,3)))
    case "2":
        print("The square of " + str(num) +" is " + str(square))
    case "3":
        print("The cube of " + str(num) + " is " + str(cube))
    case "4":
        print(exit)