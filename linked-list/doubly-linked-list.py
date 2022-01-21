"""
Doubly-linked list
Forward traversal
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data , end=" ")
                n = n.next
            print("\n")
    def print_reverse_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data , end=" ")
                n = n.prev
    def insert_at_the_beginning(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_to_empty_llist(self,new_value):
        if self.head is None:
            new_node = Node(new_value)
            self.head = new_node
        else:
            print("Linked list is not empty")
    def insert_at_the_end(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n
    def insert_after_given_node(self,prev_node,new_value):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if prev_node == n.data:
                    break
                n = n.next
            if n is None:
                print("The value is not in the linked list")
            else:
                new_node = Node(new_value)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_given_node(self,next_node,new_value):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if next_node == n.data:
                    break
                n = n.next
            if n is None:
                print("The value is not in the linked list")
            else:
                new_node = Node(new_value)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

if __name__ == '__main__':
    ll1 = DoublyLinkedList()
    # ll1.insert_at_the_beginning(1)
    # ll1.insert_at_the_beginning(2)
    # ll1.insert_at_the_beginning(3)
    ll1.insert_to_empty_llist(1)
    ll1.insert_at_the_beginning(2)
    ll1.insert_at_the_beginning(3)
    ll1.insert_at_the_end(0)
    ll1.insert_after_given_node(3,33)
    ll1.insert_before_given_node(0,100)
    ll1.print_linked_list()
    ll1.print_reverse_linked_list()