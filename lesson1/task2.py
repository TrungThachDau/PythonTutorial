def ListFunction():
    list = []
    print("List: ", list)
    print("1. Add, 2. Remove, 3. Show, 4. Choose by index")
    action = input("Type 1 action: ")
    while action != "4":
        if action == "1":
            list.append(input("Type a value: "))
        elif action == "2":
            list.remove(input("Type a value: "))
        elif action == "3":
            print("List: ", list)
        elif action == "4":
            index = int(input("Choose index of the list: "))
            print("Value: ", list[index])
        else:
            print("Invalid input")
        print("List: ", list)
        action = input("Type 1 action: ")
