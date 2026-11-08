# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:7A
def isValid(width, height):
    if width + height > 30:
        print("This is a valid rectangle")
        return True
    else:
        print("This is an invalid rectangle")
        False
        return

def area(width, height):
    print(f'The area is: {width * height}')
    return

def perimeter(width, height):
    print(f'The perimeter is: {width + height + width + height}')
    return

x = 0
while x == 0 :
    width = float(input('Enter width: '))
    height = float(input('Enter height: '))
    if isValid(width,height) == True:
        area(width, height)
        perimeter(width, height)
    again = input("Do you want to enter another width and height (Y/N)?: ")
    if again == "Y":
        True
    else:
        print('Program Ends')
        x += 1




