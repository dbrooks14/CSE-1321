#Class:CSE 1321L
#Section:B10
#Term:Fall 2026
#Instructor:Lan Vu
#Name:Dyllan Brooks
#Lab:6B

import random
random_number = random.randint(1,100)
guess = ()
while guess != random_number:
    print("Guess the number I am thinking!")
    guess = int(input("Enter any number between 1 and 100: "))

    if guess == random_number:
        print(f"Correct! I was thinking of {random_number}")
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")