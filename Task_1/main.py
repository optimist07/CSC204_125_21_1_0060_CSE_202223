from single_linked_list import SingleLinkedList

if __name__ == "__main__":
    data = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    linked_list = SingleLinkedList()

    for item in data:
        linked_list.insert(item)

    print("Linked List:")
    linked_list.display()
