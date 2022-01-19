"""
Singly linked list
Time complexity(insertion): Insertion at the biginning-O(1), insertion at the end-O(n), insertion after n nodes-O(n)


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

    # Insert a new node at the beginning of a linked list
    def insert_at_the_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end of a linked list 
    def insert_at_the_end(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    # Insert a new node after a given node
    def insert_after(self, prev_node, new_value):
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n:
                if n.data == prev_node:
                    node1 = Node(new_value)
                    node1.next = n.next
                    n.next = node1
                    break
                n = n.next
                if n is None:
                    print("Previous node not found")

    # Insert a new node before a given node
    def insert_before(self, next_node, new_value):
        if self.head is None:
            print("Linked listt is empty")
            return
        elif self.head.data == next_node:
            node1 = Node(new_value)
            node1.next = self.head
            self.head = node1
            return
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == next_node:
                    break
                n = n.next
            if n.next is None:
                print("Node not found")
            else:
                node1 = Node(new_value)
                node1.next = n.next
                n.next = node1
    # Delete a node from the beginning of a linked list
    def delete_at_the_beginning(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            self.head = self.head.next

    # Delete the node at the end of a linked list
    def delete_at_the_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == value:
                break
            n = n.next
        if n.next is None:
            print("Value not found")
        else:
            n.next = n.next.next
if __name__ == '__main__':
     
    l1 = LinkedList()

    l1.insert_at_the_beginning(1)
    l1.insert_at_the_beginning(2)
    l1.insert_at_the_beginning(3)
    l1.insert_at_the_end(4)
    l1.insert_at_the_end(5)
    l1.insert_after(4, 8)
    l1.insert_before(2,79)
    l1.insert_before(3,899)
    l1.insert_before(899,700)
    l1.insert_after(899,500)
    l1.insert_at_the_end(90)
    l1.insert_at_the_beginning(0)
    l1.delete_at_the_beginning()
    l1.delete_at_the_end()
    l1.delete_by_value(5)
    l1.delete_by_value(8)
    l1.print_linked_list()
