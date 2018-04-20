result = ''
message = 'l'
choice = ''


while choice != 0:
    choice = input('\nDo you want to encrypt or decrypt the message?\nEnter 1 to encrypt, 2 to decrypt, 0 to exit the program.')
    

    if choice == '1':
        message = input('\nEnter message for encryption: ')
        for i in range(0, len(message)):
            
             result = result + chr(ord(message[i]) - 2)

    print(result +  '\n\n')
    result = ''


    if choice == '2':
        message = input('\nEnter message for decrypt: ')
        for i in range(0, len(message)):

            result = result + chr(ord(message[i]) + 2)


            print(result +'\n\n')
            result = ''

    elif choice !='0':
            print('\n')
