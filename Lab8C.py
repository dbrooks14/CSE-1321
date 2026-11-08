# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:8C
import math

first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))

print(f'Ceiling: {math.ceil(first)}')
print(f'Floor: {math.floor(first)}')
print(f'Absolute value: {math.fabs(first):.3f}')
print(f'Square root: {math.sqrt(second):.3f}')
print(f'Cube root: {math.cbrt(second):.3f}')
print(f'Log base 2: {math.log(second,2):.3f}')
