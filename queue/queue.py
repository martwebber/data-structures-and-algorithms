class QueueDS:
    def __init__(self):
        self.queue = []
    def enqueue(self):
        val = input("Enter an element: ")
        self.queue.append(val)
        print(f'{val} has been added to the queue')

    def dequeue(self):
        if not self.queue:
            print("The queue is empty")
        else:
            elem = self.queue.pop(0)
            print(f"{elem} has been removed")

    def display(self):
        print(self.queue)
    def peek(self):
        print(self.queue[0])

if __name__ == '__main__':
    q1 = QueueDS()
    while True:
        print("Select 1 to add an element, 2 to remove an element, 3 to display 4 peek and 5 to quit")
        choice = int(input("What is your choice?"))
        if choice == 1:
            q1.enqueue()
        elif choice == 2:
            q1.dequeue()
        elif choice == 3:
            q1.display()
        elif choice == 4:
            q1.peek()
        elif choice == 5:
            break
        else:
            print("You entered a wrong choice, try again")
