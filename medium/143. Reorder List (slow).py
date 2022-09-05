# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        elif head.next is None:
            return head

        node_list = []
        while head is not None:
            node_list.append(head)
            head = head.next

        i = 0
        n = len(node_list)
        a, b = self.get_index(n, i), self.get_index(n, i + 1)

        while a < n and b < n and i < n:
            previous, current = node_list[a], node_list[b]
            if previous is not None:
                previous.next = current

            i += 1
            a, b = self.get_index(n, i), self.get_index(n, i + 1)

        node_list[self.get_index(n, n - 1)].next = None

        return node_list[0]

    def get_index(self, n, k):
        if k % 2 == 0:
            return k // 2
        return n - 1 - (k - 1) // 2
