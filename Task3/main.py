
from queue import Queue

if __name__ == "__main__":
    # Test binary search algorithm on an unsorted array
    data = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    # Test the queue data structure
    queue = Queue()

    for item in data:
        queue.enqueue(item)

    print("\nQueue:")
    queue.display()

    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")

    print("Queue after dequeue:")
    queue.display()

    # Sort the queue and display the sorted queue
    queue.sort()
    print("\nSorted Queue:")
    queue.display()
