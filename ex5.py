import random
import timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head or self.head.value > value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

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

class HeapPriorityQueue:
    def __init__(self):
        self.heap = SimpleHeap()

    def enqueue(self, value):
        self.heap.enqueue(value)

    def dequeue(self):
        if len(self.heap.heap) == 0:  
            return None  
        return self.heap.dequeue()


def generate_tasks(n=1000):
    return [('enqueue', random.randint(1, 100)) if random.random() < 0.7 else ('dequeue',) for _ in range(n)]

def process_tasks(tasks, queue):
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        elif task[0] == 'dequeue':
            queue.dequeue()

if __name__ == "__main__":
    list_queue_tasks = generate_tasks()
    heap_queue_tasks = list(list_queue_tasks)

    list_queue = ListPriorityQueue()
    heap_queue = HeapPriorityQueue()

    list_time = timeit.timeit(lambda: process_tasks(list_queue_tasks, list_queue), number=1)
    heap_time = timeit.timeit(lambda: process_tasks(heap_queue_tasks, heap_queue), number=1)

    print(f"ListPriorityQueue: Total time: {list_time}, Average time per task: {list_time / 1000}")
    print(f"HeapPriorityQueue: Total time: {heap_time}, Average time per task: {heap_time / 1000}")

# Q4 Explanation : The HeapPriorityQueue typically outperforms the ListPriorityQueue due to its efficient organization for adding and removing tasks. As the ListPriorityQueue grows, it becomes slower because each new task requires finding the correct insertion point. On the other hand, the HeapPriorityQueue, utilizing a heap structure, keeps the smallest item readily accessible, optimizing both additions and removals. Therefore, for handling numerous tasks, the heap-based approach maintains efficiency and speed.
