class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def push(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def pop(self):
        if self.front is None:
            return None
        node = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        node.next = None
        return node.data


a = Queue()

a.push(1)
a.push(2)
a.push(3)
a.print_queue()

a.pop()
a.print_queue()