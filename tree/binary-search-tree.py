import random

class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
    def insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data: # ignore dublicates
            return

        if self.key > data:
            if self.left_child:
                self.left_child.insertion(data)
            else:
                self.left_child = BinarySearchTree(data)
        else:
            if self.right_child:
                self.right_child.insertion(data)
            else:
                self.right_child = BinarySearchTree(data)

    def search(self,data):
        if self.key == data:
            print("Node exists")
            return
        if data < self.key:
            if self.left_child:
                self.left_child.search(data)
            else:
                print("Node not found")
        else:
            if self.right_child:
                self.right_child.search(data)
            else:
                print("Node not found")
    def deletion(self,data):
        if self.key is None:
            print("The tree is empty")
            return
        if data < self.key:
            if self.left_child:
                self.left_child = self.left_child.deletion(data)
            else:
                print("The node is not present")
        elif data > self.key:
            if self.right_child:
                self.right_child = self.right_child.deletion(data)
            else:
                print("The node is not present")
        else:
            if self.left_child is None:
                temp =self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp =self.left_child
                self = None
                return temp
            node = self.right_child
            while  node.left_child:
                node = node.left_child
            self.key = node.key
            self.right_child = self.right_child.deletion(node.key)
        return self

    def preorder_traversal(self):
        print(self.key, end=' ')
        if self.left_child:
            self.left_child.preorder_traversal()
            if self.right_child:
                self.right_child.preorder_traversal()
    def inorder_traversal(self):
        if self.left_child:
            self.left_child.inorder_traversal()
        print(self.key, end=' ')
        if self.right_child:
            self.right_child.inorder_traversal()
    def postorder_traversal(self):
        if self.left_child:
            self.left_child.postorder_traversal()
        if self.right_child:
            self.right_child.postorder_traversal()
        print(self.key, end=' ')
def count(node):
    if node is None:
        return 0
    return 1+count(node.left_child)+count(node.right_child)
if __name__ == '__main__':
    root = BinarySearchTree(50)
    l1 = [random.randrange(0,100)*random.randrange(0,100) for x in range(5)]
    print(l1)
    for i in l1:
        root.insertion(i)
    root.search(40)
    print("Pre-order")
    root.preorder_traversal()
    print("\nin-order")
    root.inorder_traversal()
    print("\npost-order")
    root.postorder_traversal()
    if count(root)>1:
        root.deletion(50)
    else:
        print("You cannot perform the deletion operation")
    print("\npost-order after deleting node")
    root.postorder_traversal()