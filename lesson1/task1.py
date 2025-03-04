import random
def Functon1():
    tasks = ["Sleeping", "WC", "Chatting", "Testing", "Coffee", "YouTube"]
    print("All tasks: ")
    for task in tasks:
        print(task,end=", ")
    print("\n")
    print("Your task: ", random.choice(tasks))
    print("Random from 1 to 100: ", random.randint(1, 100))
