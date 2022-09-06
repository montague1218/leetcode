# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        while head is not None and head.val == val:
            head = head.next

        new_head = head
        previous, current = None, head
        while current is not None:
            if current.val == val:
                previous.next = current.next
                current = current.next
            else:
                previous, current = current, current.next

        return new_head

# this solution iterates but ignore duplicated items
# it does twice at the start of the linked list and its middle during looping
