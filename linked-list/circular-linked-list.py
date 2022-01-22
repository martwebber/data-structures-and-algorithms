"""
Circular linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Traverse linked list
    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.next
                if n == self.head:
                    break

    # Insert a new node at the beginning of a linked list
    def insert_at_the_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
        self.head = new_node
        
    # # Insert a new node at the end of a linked list 
    def insert_at_the_end(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head
    
    
if __name__ == '__main__':
     
    l1 = LinkedList()

    l1.insert_at_the_beginning(1)
    l1.insert_at_the_beginning(2)
    l1.insert_at_the_beginning(3)
    l1.insert_at_the_end(4)
    l1.insert_at_the_end(5)
    l1.print_linked_list()
