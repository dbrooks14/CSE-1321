# Class:CSE 1321L
# Section:B10
# Term:Fall 2026
# Instructor:Lan Vu
# Name:Dyllan Brooks
# Assignment:2B
bag1 = 35
bag2 = 50
bag3 = 150
while True:
    print("[Owl Airlines - Checked Bag Kiosk]")

    member = input("Are you a Hooty Hoo Preferred Member? (Y/N): ")

    if member == "Y":
        print("Welcome, and thank you for being a Hooty Hoo Preferred Member")
        print("As a perk for being awesome, your first 2 checked bags are free")
        print("Additional bags are $35.00 each")
        print()
        bagCheck = input("Are you checking any bags? (Y/N): ")
        if bagCheck == "Y":
            bagNum = int(input("How many bags are you checking in?: "))
            if bagNum > 0:
                if bagNum > 2:
                    bagFee = bagNum-2
                    bagFee = bagFee*35
                    print("As a Hooty Hoo Preferred Member your first 2 bags are complimentary")
                    print("Checked Bag fees to pay: $" +str(bagFee) + ".00")
                    print("Have a safe flight and thank you for being a Hooty Hoo Preferred Member")
                elif bagNum <= 2:
                    print("As a Hooty Hoo Preferred Member your first 2 bags are complimentary")
                    print("Have a safe flight and thank you for being a Hooty Hoo Preferred Member")

        elif bagCheck == "N":
            print("Have a safe flight and thank you for being a Hooty Hoo Preferred Member")

    elif member == "N":
        print("Checked Bag rates:\n- First Checked bag: $35.00\n- Second Checked bag: $50.00\n- Third+ Checked bag: $150.00 each")
        bagCheck = input("Are you checking any bags? (Y/N): ")
        if bagCheck == "Y":
            bagNum = int(input("How many bags are you checking in?: "))
            if bagNum > 0:
                if bagNum == 1:
                    print("Checked Bag fees to pay: $" +str(bag1) + ".00")
                elif bagNum == 2:
                    print("Checked Bag fees to pay: $" + str(bag1+bag2) + ".00")
                elif bagNum == 3:
                    print("Checked Bag fees to pay: $" + str(bag1+bag2+bag3) + ".00")
                else:
                    print("Checked Bag fees to pay: $" + str((bag1+bag2)+(bagNum-2)*(bag3)) + ".00")









