import random
# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Lab:8A
seed = int(input('Enter a seed value: '))
rolls = int(input('How many times would you like to roll the die? '))

random.seed(seed)
total = 0

for i in range(rolls):
    mystery = random.randint(1,6)
    print(f'Roll {i+1}: {mystery}')
    total += mystery
print(f'Total: {total}')

