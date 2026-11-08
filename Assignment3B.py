# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Assignment:3B
print("[Character Frequencies]")

word = input("Enter a string: ")

word = word.lower()
word = word.replace(" ","")
remaining = word

for x in word:
    if x in remaining:
        count = 0
        for y in remaining:
            if y == x:
                count += 1
        if count == 1:
            print(f"{x} appears {count} time")
        else:
            print(f"{x} appears {count} times")
        remaining = remaining.replace(x,"")