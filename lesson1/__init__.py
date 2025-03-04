import random
from lesson1.task1 import Functon1
from lesson1.task2 import ListFunction
from lesson1.task3 import PasswordGenerator

def switch(value):
    functions = {
        1: Functon1,
        2: ListFunction,
        3: PasswordGenerator
    }
    func = functions.get(value, lambda: print("Invalid input"))
    func()

if __name__ == "__main__":
    action = int(input("Type 1 function: "))
    switch(action)