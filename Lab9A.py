emailList = []
print('[Mailing List]')
while True:
    print()
    print('1 - Add email')
    print('2 - Delete email')
    print('3 - List all emails')
    print('4 - Quit')
    choice = int(input('Make your selection: '))

    if choice == 1:
        emailList.append(input('Enter the email to be added: '))
        print('Email added to mailing list.')
    elif choice == 2:
        delEmail = input('Enter the email to be removed: ')
        if delEmail in emailList:
            emailList.remove(delEmail)
            print(f'{delEmail} has been removed from the mailing list.')
        else:
            print(f'No such email in mailing list: {delEmail} ')
    elif choice == 3:
        print()
        for i in emailList:
            print(i)
    elif choice == 4:
        print('Shutting down...')
        break

