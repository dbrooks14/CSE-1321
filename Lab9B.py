print('[Friend List]')
print()
friends = []


while True:
    print('1 - Add friend')
    print('2 - List friends')
    print('3 - Quit')
    choice = int(input('Make your selection: '))
    print()
    if choice == 1:
        name = input("Enter your friend's name: ")
        age = input("Enter your friend's age: ")
        friendsList = (name, age)
        friends.append(friendsList)
        print('Friend added')
        print()
    elif choice == 2:
        for i in friends:
            print(f'Name: {i[0]}, Age: {i[1]}')
        print()
    elif choice == 3:
        print('Shutting down...')
        break

