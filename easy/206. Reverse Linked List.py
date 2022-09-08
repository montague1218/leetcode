# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        elif head.next is None:
            return head

        next, right_tail = self.reverseBody(head, head)
        return right_tail

    def reverseBody(self, current, right_tail):
        if current.next is None:
            return current, current

        next, right_tail = self.reverseBody(current.next, right_tail)
        next.next, current.next = current, None
        return current, right_tail

# treat the linked list as a spring
# recurse to the right-most tail to the spring
# when it's springing back towards the left, keeping returning its right-most-tail
# and reverse points for each pair during the motion
