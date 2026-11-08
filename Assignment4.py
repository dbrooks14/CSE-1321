def input_choice(lowest, highest):
    choice = int(input('>'))

    while choice < lowest or choice > highest:
        print(f'Please, enter an option between {lowest} and {highest}')
        choice = int(input('>'))

    return choice

def input_money():
    money = float(input('> $'))

    while money < 0:
        print('Please, enter a valid monetary amount.')
        money = float(input('> $'))

    return money

def order():
    subtotal = 0.0

    while True:
        print('Choose an option:')
        print('1. Burgers')
        print('2. Sides')
        print('3. Drinks')
        print('4. Check out')

        choice = input_choice(1,4)
        if choice == 1:
            subtotal += burgers()
        elif choice == 2:
            subtotal += sides()
        elif choice == 3:
            subtotal += drinks()
        elif choice == 4:
            return subtotal

def burgers():
    amount = 0.0

    while True:
        print('1. Big Owl Burger - Single ($5.99)')
        print('2. Big Owl Burger - Double ($7.99)')
        print('3. Return')

        choice = input_choice(1,3)

        if choice == 1:
            print()
            print('1 Big Owl Burger - Single added')
            amount += 5.99
            print()
        elif choice == 2:
            print()
            print('1 Big Owl Burger - Double added')
            print()
            amount += 7.99
        elif choice == 3:
            return amount

def sides():
    amount = 0.0

    while True:
        print('1. Fries ($3.49)')
        print('2. Onion Rings ($2.99)')
        print('3. Get Back')

        choice = input_choice(1,3)

        if choice == 1:
            print()
            print('1 Fries added')
            print()
            amount += 3.49
        elif choice == 2:
            print()
            print('1 Onion Rings added')
            print()
            amount += 2.99
        elif choice == 3:
            return amount

def drinks():
    amount = 0.0

    while True:
        print('1. Scrappy-Cola - Small ($2.49)')
        print('2. Scrappy-Cola - Medium ($2.79)')
        print('3. Scrappy-Cola - Large ($2.99)')
        print('4. Dr Owl - Small ($2.49)')
        print('5. Dr Owl - Medium ($2.79)')
        print('6. Dr Owl - Large ($2.99)')
        print('7. Get Back')

        choice = input_choice(1,7)
        if choice == 1:
            print()
            print('1 Scrappy-Cola - Small added')
            print()
            amount += 2.49
        elif choice == 2:
            print()
            print('1 Scrappy-Cola - Medium added')
            print()
            amount += 2.79
        elif choice == 3:
            print()
            print('1 Scrappy-Cola - Large added')
            print()
            amount += 2.99
        elif choice == 4:
            print()
            print('1 Dr Owl - Small added')
            print()
            amount += 2.49
        elif choice == 5:
            print()
            print('1 Dr Owl - Medium added')
            print()
            amount += 2.79
        elif choice == 6:
            print()
            print('1 Dr Owl - Large added')
            print()
            amount += 2.99
        elif choice == 7:
            return amount

def calculate_tip(subtotal):
    print('Choose a tip option:')
    print(f'1. ${subtotal * 0.18:.2f} (18%)')
    print(f'2. ${subtotal * 0.20:.2f} (20%)')
    print(f'3. ${subtotal * 0.25:.2f} (25%)')
    print('4. Custom')
    print('5. No Tip')

    choice = input_choice(1,5)

    if choice == 1:
        return subtotal * 0.18
    elif choice == 2:
        return subtotal * 0.20
    elif choice == 3:
        return subtotal * 0.25
    elif choice == 4:
        print('Custom tip:')
        return input_money()
    elif choice == 5:
        return 0.0

def calculate_tax(subtotal):
    return subtotal * 0.06

def print_total(subtotal, tip, tax):
    total = subtotal + tip + tax
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Tip: ${tip:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${total:.2f}')

subtotal = order()
tip = calculate_tip(subtotal)
tax = calculate_tax(subtotal)
print_total(subtotal, tip, tax)


