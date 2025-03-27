class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def __insert_node(self,current, data):
        if self.root.data != Node(data).data:
            self.root.right = Node(data)
        elif self.root.data < current.data:
            self.insert_node(current.left, data)
        else:
            self.insert_node(current.right, data)
    def __insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)


    def insert_node2(self,current, data):
        if self.root is None:
            self.root = Node(data)
            return
        if current is None:
            return Node(data)
        if data == current.data:
            return current
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self.insert_node2(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self.insert_node2(current.right, data)
    def show_node_of_level_k(self, current, k):
        if current is None:
            return
        if k == 0:
            print(current.data)
        else:
            self.show_node_of_level_k(current.left, k-1)
            self.show_node_of_level_k(current.right, k-1)
    def in_order_traversal(self, root, result):
        if root:
            self.in_order_traversal(root.left, result)
            result.append(root.data)
            self.in_order_traversal(root.right, result)
    def show_Tree(self):
        result = []
        self.in_order_traversal(self.root, result)
        for i in result:
            print(i, end=' ')

        print()
    def search_node(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self.search_node(current.left, data)
        else:
            return self.search_node(current.right, data)
    @staticmethod
    def min_of_tree(current):
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.data
    @staticmethod
    def max_of_tree(current):
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current.data
    def length_of_tree(self):
        if self.root is None:
            return 0
        count = 0
        #Dem ben trai
        current = self.root
        while current.left is not None:
            count += 1
            current = current.left
        #Dem ben phai
        current = self.root
        while current.right is not None:
            count += 1
            current = current.right
        #Dem nut goc
        count += 1
        #Dem nut con
        current = self.root
        if current.left is not None:
            count += 1
        if current.right is not None:
            count += 1
        return count
    def length_of_tree2(self, current):
        if current is None:
            return 0
        return 1 + self.length_of_tree2(current.left) + self.length_of_tree2(current.right)
    def delete_node(self, current, data):
        if current is None:
            return current
        if data < current.data:
            current.left = self.delete_node(current.left, data)
        elif data > current.data:
            current.right = self.delete_node(current.right, data)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            temp = self.min_of_tree(current.right)
            current.data = temp
            current.right = self.delete_node(current.right, temp)
        return current
if __name__ == '__main__':
    bst = Tree()
    nodes = [10, 5, 15, 3, 7, 12, 18,20,20]
    for node in nodes:
        bst.insert_node2(bst.root, node)
    #bst.show_node_of_level_k(bst.root, 1)
    bst.show_Tree()
    print(bst.search_node(bst.root, 20))
    print(bst.min_of_tree(bst.root))
    print(bst.length_of_tree())
    print(bst.length_of_tree2(bst.root))
    bst.delete_node(bst.root, 20)
    bst.show_Tree()