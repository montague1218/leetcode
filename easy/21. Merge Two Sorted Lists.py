# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        # swapping must be done, so that list1 is always the list to be inserted
        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = list1
        a, b = list1, list2

        # handle main body
        while a.next is not None and b.next is not None:
            if a.val <= b.val <= a.next.val:
                tail_a, tail_b = a.next, b.next

                # insert b between a and a's tail
                a.next, a.next.next = b, tail_a
                a, b = a.next, tail_b
            elif a.next.val <= b.val:
                a = a.next
            # no third case, since a.val <= b.val is always true (due to the initial swap)

        # handle edge end-cases
        if a.next is None:
            a.next = b
        elif b.next is None:  # a has tail and remains b to be inserted
            while a is not None:
                if a.next is None:
                    a.next = b
                    break
                elif a.val <= b.val <= a.next.val:
                    tail_a = a.next
                    a.next, b.next = b, tail_a
                    break
                elif a.next <= b.val:
                    if a.next.next is None:
                        a.next.next = b
                        break
                    # move towards a's tail so that the one of the above two insertions happen
                a = a.next
        return head

# this solution inserts list2 to list1
# only one possible situation may happen: insert b in between a and its tail, when added, set b to its next tail,
# if a has no tail, then a's tail is set to b
