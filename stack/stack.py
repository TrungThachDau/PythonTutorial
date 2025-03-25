class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None


a = Stack()
print(a.is_empty()) # True