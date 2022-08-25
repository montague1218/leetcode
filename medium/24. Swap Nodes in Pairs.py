# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        oldHead = head.next

        previous, current = None, head

        while current is not None:
            if current.next is None:
                break

            head, tail = self.swap_pair(current, current.next)
            if previous is not None:
                previous.next = head
            previous, current = tail, tail.next
        return oldHead

    def swap_pair(self, n1, n2):
        n1.next = n2.next
        n2.next = n1

        return n2, n1  # return the tail of the swapped pair

# this solution observes swapping requires 2 pair of nodes (head, tail),
# and chaining each adjecent pair requires a pair of (previous, current).
