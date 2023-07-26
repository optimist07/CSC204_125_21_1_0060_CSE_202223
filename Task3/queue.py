from node import Node

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.head is None

    def enqueue(self, data):
        """
        Add an element to the end (tail) of the queue.

        Parameters:
            data: The data value to be added to the queue.
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Remove and return the element from the front (head) of the queue.

        Returns:
            The data value of the dequeued element, or None if the queue is empty.
        """
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data

    def display(self):
        """
        Display the elements of the queue in order.

        This function will print "None" for an empty queue.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def sort(self):
        """
        Sort the elements of the queue in ascending order.
        """
        if self.is_empty():
            return

        # Convert the queue to a list for sorting
        arr = []
        while not self.is_empty():
            element=self.dequeue()
            arr.append(element)


        # Sort the list
        arr.sort()

        # Convert the sorted list back to the queue
        for element in arr:
            self.enqueue(element)
