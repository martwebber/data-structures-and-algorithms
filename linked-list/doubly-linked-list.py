"""
Doubly-linked list
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.next is not None:
                print(n.data, end=" ")
                n = n.next
    def print_reverse_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, end=" ")
                n = n.prev
    def insert_at_the_beginning(self, new_value):
        print(new_value)
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node.next
        else:
            new_node.prev = new_node
            new_node.next = self.head
            self.head = new_node

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_the_beginning(1)
    ll1.insert_at_the_beginning(2)
    ll1.insert_at_the_beginning(3)
    ll1.print_linked_list()