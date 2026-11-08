#Class:CSE 1321L
#Section:B10
#Term:Fall 2026
#Instructor:Lan Vu
#Name:Dyllan Brooks
#Lab:6A

calculator = True

while calculator == True:
    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to exit")
    option = int(input(""))


    if option == 1:
        result = 0
        operand1 = int(input("Enter an operand: "))
        operand2 = int(input("Enter another operand: "))
        for x in range(operand2):
            for y in range(operand1):
                result += 1
        print(f"{operand1} x {operand2} = {result}")

    elif option == 2:
        result = 1
        operand1 = int(input("Enter the base: "))
        operand2 = int(input("Enter the exponent: "))
        for x in range(operand2):
            temp = 0
            for y in range(operand1):
                temp += result
            result = temp
        print(f"{operand1}^({operand2}) = {result}")

    elif option == 3:
        print("Closing the calculator...")
        calculator = False
    else:
        print("Invalid Choice")



