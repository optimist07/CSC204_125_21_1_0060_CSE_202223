from list_to_bst import SingleLinkedList

if __name__ == "__main__":
    data = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    linked_list = SingleLinkedList()

    for item in data:
        linked_list.insert(item)

    print("Linked List:")
    linked_list.display()

    print("Maximum Data:", linked_list.find_max())
    print("Minimum Data:", linked_list.find_min())

    # Convert the linked list to a binary search tree
    bst_data = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    linked_list.list_to_bst(bst_data)

    print("\nBinary Search Tree:")
    linked_list.display()  # Displaying the linked list will now show the sorted order of the BST
