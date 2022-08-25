# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        top_previous, top = None, head
        current, i = head, 1
        while current is not None:
            if i >= n:
                top_previous, top = top, top.next
            current = current.next
            i += 1
        top_previous.next = top.next
        return head

# this solution transforms the linked-list into an array,
# and pays attention to the edge cases

# this solution seems not optimized

# def removeNthFromEnd(self, head, n):
# nodes = []
# current = head
# while current is not None:
#     nodes.append(current)
#     current = current.next
#
# if len(nodes) == 1:
#     return None
# elif n + 1 > len(nodes):
#     return nodes[-n].next
# nodes[-n - 1].next = nodes[-n].next
# return head

# it turns out the following approach without array takes longer time (unknown reason)

# def removeNthFromEnd(self, head, n):
#     """
#     :type head: ListNode
#     :type n: int
#     :rtype: ListNode
#     """
#
#     top_previous, top = None, head
#     current, i = head, 1
#     while current is not None:
#         if i > n:
#             top_previous, top = top, top.next
#         current = current.next
#         i += 1
#
#     if top_previous is None:
#         if i == 2:
#             return None
#         return top.next
#
#     top_previous.next = top.next
#     return head
