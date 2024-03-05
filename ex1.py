import timeit
import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)

        current = root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = TreeNode(key)
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = TreeNode(key)
                    break
                current = current.right
            else:
                break

        return root

    def search(self, key):
        current = self.root
        while current is not None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return current

def measure_search_performance(sorted_vector, shuffle=False):
    if shuffle:
        random.shuffle(sorted_vector)

    bst = BinarySearchTree()
    total_time = 0

    for element in sorted_vector:
        bst.insert(element)

    for _ in range(10):
        search_times = []
        for element in sorted_vector:
            start_time = timeit.default_timer()
            bst.search(element)
            end_time = timeit.default_timer()
            search_times.append(end_time - start_time)

        average_time = sum(search_times) / len(search_times)
        total_time += average_time

    return average_time, total_time

sorted_vector = list(range(10000))

average_time_sorted, total_time_sorted = measure_search_performance(sorted_vector)
average_time_shuffled, total_time_shuffled = measure_search_performance(sorted_vector, shuffle=True)

print("Search performance for a sorted vector:")
print(f"Average time: {average_time_sorted} seconds")
print(f"Total time: {total_time_sorted} seconds")

print("\nSearch performance for a shuffled vector:")
print(f"Average time: {average_time_shuffled} seconds")
print(f"Total time: {total_time_shuffled} seconds")


# Searching in a binary search tree built from a sorted vector is faster on average and results in lower total search time compared to a shuffled vector. The main factor for this is the balanced nature of the tree when keys are inserted in a sorted order, leading to more efficient searches.
