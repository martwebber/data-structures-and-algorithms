import random
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left_child = None
#         self.right_child = None

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
        pass

if __name__ == '__main__':
    root = BinarySearchTree(None)
    l1 = [90,76,90,4,74,23,0,12]
    for i in l1:
        root.insertion(i)
    root.search(40)