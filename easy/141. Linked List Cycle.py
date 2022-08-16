# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        counts = set()
        current = head
        while current is not None:
            if current not in counts:
                counts.add(current)
                current = current.next
            else:
                return True
        return False
