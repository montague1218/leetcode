class MyStack(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.q1) == 0:
            self.q1.append(x)
            while len(self.q2) > 0:
                self.q1.append(self.q2.pop(0))
        elif len(self.q2) == 0:
            self.q2.append(x)
            while len(self.q1) > 0:
                self.q2.append(self.q1.pop(0))
        else:
            self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.q1) == 0:
            return self.q2.pop(0)
        if len(self.q2) == 0:
            return self.q1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if len(self.q1) == 0:
            return self.q2[0]
        if len(self.q2) == 0:
            return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) + len(self.q2) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# For a stack to be isomorphic to a group of two queues, it suffices to maintain the relative order
# of the elements in the stack by alternating switches between two queues
