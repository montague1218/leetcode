class Node(object):
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "(name: %s, priority: %s)" % (self.name, self.priority)


class MaxHeap(object):
    def __init__(self, elements):
        self.max_children_size = 2

        self.heap = elements
        self.heapify()

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def top(self):
        if len(self.heap) == 0:
            return None

        p = self.heap.pop(-1)
        if len(self.heap) == 0:
            return p

        p_top = self.heap[0]
        self.heap[0] = p
        self.pushdown(0)

        return p_top

    def insert(self, p):
        self.heap.append(p)
        self.pushup(len(self.heap) - 1)

    def pushup(self, index):
        current = self.heap[index]
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[parent_index].priority < current.priority:
                self.heap[index] = self.heap[parent_index]
                index = parent_index
            else:
                break
        self.heap[index] = current

    def pushdown(self, index):
        current = self.heap[index]
        first_leaf_index = self.get_first_leaf_index()

        while index < first_leaf_index:
            child_index, child = self.get_highest_priority_child(index)
            # print(child_index, child, index, self.get_first_leaf_index())
            if child.priority > current.priority:
                self.heap[index] = self.heap[child_index]
                index = child_index
            else:
                break
        self.heap[index] = current

    def heapify(self):
        n = len(self.heap)
        for i in range(len(self.heap)):
            self.pushdown(n - 1 - i)

    def get_parent_index(self, index):
        return (index - 1) // self.max_children_size

    def get_first_leaf_index(self):
        if len(self.heap) == 1:
            return 0

        layer = 1
        head = 1
        while True:
            if head + self.max_children_size * layer >= len(self.heap):
                return head
            head += self.max_children_size * layer
            layer += 1

    def get_highest_priority_child(self, index):
        child_index = self.max_children_size * index + 1
        child = self.heap[child_index]

        for i in range(self.max_children_size):
            node_index = self.max_children_size * index + 1 + i
            if node_index < len(self.heap) and self.heap[node_index].priority > child.priority:
                child_index = node_index
                child = self.heap[child_index]

        return child_index, child

    def print(self):
        for node in self.heap:
            print(node)

    def print_by_layer(self):
        print("[layer %s]" % 0)
        print(self.heap[0])

        layer = 1
        head = 1
        while True:
            print("[layer %s]" % layer)
            for i in range(self.max_children_size * layer):
                index = head + i
                if index < len(self.heap):
                    print("i:%s, %s" % (index, self.heap[index]))
                else:
                    return None
            head += self.max_children_size * layer
            layer += 1


if __name__ == "__main__":
    priorities = [0, 1, 2, 3, 4, 5, 6]
    nodes = [Node(str(i), i) for i in priorities]

    max_heap = MaxHeap(nodes)
    max_heap.print_by_layer()

    max_heap.insert(Node("big", 9999))
    max_heap.insert(Node("small", -1))

    max_heap.print_by_layer()
    for i in range(7):
        pass
        # print(max_heap.top())
        # max_heap.print_by_layer()
