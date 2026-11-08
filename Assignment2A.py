# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Assignment:2A
loudness = float(input("Enter input loudness (dB): "))
threshold = float(input("Enter threshold (dB): "))

print("Select a ratio: ")
print("1 - 3:1")
print("2 - 4:1")
print("3 - 10:1")

ratio = int(input("> "))

match ratio:
    case 1:
        if loudness > threshold:
            sound = threshold-loudness
            sound = (sound * 1)/3
            sound = threshold-sound
            print("You have selected the 3:1 ratio")
            print("Output Level: " + str(sound) + " dB")

        else:
            print("You have selected the 3:1 ratio")
            print("Output Level: " + str(loudness) + " dB")
    case 2:
        if loudness > threshold:
            sound = threshold-loudness
            sound = (sound * 1)/4
            sound = threshold-sound
            print("You have selected the 4:1 ratio")
            print("Output Level: " + str(sound) + " dB")
        else:
            print("You have selected the 4:1 ratio")
            print("Output Level: " + str(loudness) + " dB")
    case 3:
        if loudness > threshold:
            sound = threshold-loudness
            sound = (sound * 1)/10
            sound = threshold-sound
            print("You have selected the 10:1 ratio")
            print("Output Level: " + str(sound) + " dB")
        else:
            print("You have selected the 10:1 ratio")
            print("Output Level: " + str(loudness) + " dB")
    case _:
        if loudness > threshold:
            sound = threshold-loudness
            sound = (sound * 1)/2
            sound = threshold-sound
            print("You have selected the 2:1 ratio")
            print("Output Level: " + str(sound) + " dB")
        else:
            print("You have selected the 2:1 ratio")
            print("Output Level: " + str(loudness) + " dB")

