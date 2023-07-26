from node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_max(self):
        if self.head is None:
            return None

        max_data = self.head.data
        current = self.head.next

        while current is not None:
            if current.data > max_data:
                max_data = current.data
            current = current.next

        return max_data

    def find_min(self):
        if self.head is None:
            return None

        min_data = self.head.data
        current = self.head.next

        while current is not None:
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return min_data


    def list_to_bst(self, arr):
        def sorted_list_to_bst(arr):
            if not arr:
                return None

            mid = len(arr) // 2
            root = Node(arr)

            root.left = sorted_list_to_bst(arr[:mid])
            root.right = sorted_list_to_bst(arr[mid + 1:])

            return root

        arr.sort()
        self.head = sorted_list_to_bst(arr)
