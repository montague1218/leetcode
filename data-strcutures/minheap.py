from maxheap import MaxHeap, Node


class MinHeap(object):
    def __init__(self, elements):
        negated_elements = [Node(e.name, -e.priority) for e in elements]
        self.maxheap = MaxHeap(negated_elements)

    def peek(self):
        return self.maxheap.peek()

    def top(self):
        return self.maxheap.top()

    def insert(self, p):
        self.maxheap.insert(Node(p.name, -p.priority))

    def pushup(self, index):
        self.maxheap.pushup(index)

    def pushdown(self, index):
        self.maxheap.pushdown(index)

    def heapify(self):
        self.maxheap.heapify()

    def print_by_layer(self):
        self.maxheap.print_by_layer()


if __name__ == "__main__":
    priorities = [6, 5, 4, 3, 2, 1, 0]
    nodes = [Node(str(i), i) for i in priorities]

    min_heap = MinHeap(nodes)
    min_heap.print_by_layer()

    min_heap.insert(Node("big", 9999))
    min_heap.insert(Node("big", 999))
    min_heap.insert(Node("small", 1))
    min_heap.insert(Node("small", -1))

    min_heap.print_by_layer()