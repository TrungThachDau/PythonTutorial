class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        node.next = None
        return node.data
    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
if __name__ == '__main__':
    a = Stack()
    print(a.is_empty()) # True
    a.push(1)
    a.push(2)
    a.print_stack()
    a.pop()
    a.print_stack()
    print(a.length()) # 1