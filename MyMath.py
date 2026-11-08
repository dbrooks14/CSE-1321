# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# MyMath
def my_max(num1, num2):
    if num1 > num2:
        print(f'Max is {num1}')
        return
    elif num2 > num1:
        print(f'Max is {num2}')
        return

def my_min(num1, num2):
    if num1 < num2:
        print(f'Min is {num1}')
        return
    elif num2 < num1:
        print(f'Min is {num2}')
        return

def my_avg(num1, num2):
    print(f'Avgerage is {(num1 + num2)/2}')
    return