import random
import timeit

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

vector = list(range(10000))
random.shuffle(vector)

bst = BinarySearchTree()
for value in vector:
    bst.insert(value)

bst_search_times = [timeit.timeit(lambda: bst.search(value), number=10) for value in vector]
avg_bst_search_time = sum(bst_search_times) / len(bst_search_times)
total_bst_search_time = sum(bst_search_times)

sorted_vector = sorted(vector)

binary_search_times = [timeit.timeit(lambda: binary_search(sorted_vector, value), number=10) for value in vector]
avg_binary_search_time = sum(binary_search_times) / len(binary_search_times)
total_binary_search_time = sum(binary_search_times)

print("Average BST search time:", avg_bst_search_time)
print("Total BST search time:", total_bst_search_time)
print("Average binary search time:", avg_binary_search_time)
print("Total binary search time:", total_binary_search_time)

# Q4 :

# In our tests, the Binary Search Tree (BST) was faster than binary search on a sorted array. This might be because the BST organizes data in a way that lets us skip a lot of steps when we're looking for something. Even though both methods are pretty quick, the way BST saves and searches data worked a little better here. However, how fast each method works can change depending on what kind of data you have or how it's arranged. So, in some cases, binary search could be the faster option.