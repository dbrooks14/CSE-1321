# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Assignment:3C
print("Welcome to the Guess the Word game!")
word = input("Enter a word to guess (lowercase letters only): ")
hidden = ""

for i in range(len(word)):
    hidden += "_"

print("The word to guess is: ", end="")
for x in range(len(hidden)):
    print(hidden[x], end=" ")
print()

while hidden != word:
    guess = input("Guess a letter: ")

    if guess in word:
        print("Good guess!")

        for i in range(len(word)):
            if guess == word[i]:
                hidden = hidden[:i] + guess + hidden[i + 1:]

    else:
        print("Oops! That letter is not in the word.")
    if hidden != word:
        print("The word to guess is: ", end="")
        for x in range(len(hidden)):
            print(hidden[x], end=" ")
        print()

print(f"Congratulations! You've guessed the word: {word}")
