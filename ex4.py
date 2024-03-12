import unittest

class Heap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range(n, -1, -1):
            self._sift_down(i, n)
    
    def enqueue(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)
    
    def dequeue(self):
        if len(self.heap) == 0:
            raise Exception("You cannot dequeue from an empty heap")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removed_element = self.heap.pop()
        self._sift_down(0, len(self.heap))
        return removed_element
    
    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._sift_up(parent_index)
    
    def _sift_down(self, index, n):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest, n)

# Unit tests

class TestSimpleHeap(unittest.TestCase):

    def test_heapify_already_heap(self):
        heap = SimpleHeap()
        input_list = [1, 2, 3, 4, 5, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        heap.heapify(input_list)
        result = heap.heap
        print(f"test_heapify_already_heap: Expected {expected_output}, got {result}")
        self.assertEqual(result, expected_output)
    
    def test_heapify_empty(self):
        print(" ")
        heap = SimpleHeap()
        input_list = []
        expected_output = []
        heap.heapify(input_list)
        result = heap.heap
        print(f"test_heapify_empty: Expected {expected_output}, got {result}")
        self.assertEqual(result, expected_output)
    
    def test_heapify_random_list(self):
        print(" ")
        heap = SimpleHeap()
        input_list = [12, 3, 5, 7, 1, 13, 9]
        expected_output = [1, 3, 5, 7, 12, 13, 9]
        heap.heapify(input_list)
        result = heap.heap
        print(f"test_heapify_random_list: Expected {expected_output}, got {result}")
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

