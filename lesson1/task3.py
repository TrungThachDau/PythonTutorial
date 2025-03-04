import random
def PasswordGenerator():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')']
    password_list = []
    for char in range(1,len(letters)):
        password_list.append(random.choice(letters))
    for char in range(1,len(numbers)):
        password_list.append(random.choice(numbers))
    for char in range(1,len(symbols)):
        password_list.append(random.choice(symbols))

    print(password_list)
    random.shuffle(password_list)
    for pw in password_list :
        print(pw,end="")