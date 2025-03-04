

def WhileFunc():
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print('End of loop')

def Menu():
    print('1. Func1')
    print('2. Func2')
    print('3. Func3')
    print('4. Exit')

    action = input('Choose an action: ')

    while action != '':
        if action == '1':
            print('Function 1')
        elif action == '2':
            print('Function 2')
        elif action == '3':
            print('Function 3')
        elif action == '4':
            break
        else:
            print('Invalid input')
        Menu()
        action = input('Choose an action: ')
