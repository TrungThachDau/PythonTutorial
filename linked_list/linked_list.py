class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_head(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_tail(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def insert_after_q(self,data,q):
        if q is None:
            self.add_head(data)
        else:
            node = Node(data)
            node.next = q.next
            q.next = node
            if q == self.tail:
                self.tail = node

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=' -> ')
            current = current.next
        print('None')
    def delete_head(self):
        if self.head is not None:
            node = self.head
            self.head = node.next
            node.next = None
            if self.head is None:
                self.tail = None
            return 1
        return 0
    def delete_after_q(self,q):
        if q is not None:
            node = q.next
            if node is not None:
                if node ==self.tail:
                    self.tail = q
                q.next  = node.next
                node.next = None
                return 1
        return 0
    def get_node(self,index):
        node = self.head
        i = 0
        while i!=index and node is not None:
            node = node.next
            i+=1
        if i==index and node is not None:
            return node.data
        return None
    def search(self,data):
        node = self.head
        while node is not None and node.data!=data:
            node = node.next
        if node is not None:
            return node.data
        return None
    def length(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count+=1
        return count

    def destroy_list(self):
        node = self.head
        while node is not None:
            self.delete_head()
            node= self.head
        self.tail=None



a = LinkedList()
a.add_head(data=1)
a.add_tail(data=2)
a.add_head(data=3)
a.insert_after_q(data=4,q=a.head)
a.print_list()
a.delete_head()
a.print_list()
print(a.get_node(index=0))

print(a.search(data=9))
print(a.length())


