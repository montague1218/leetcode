# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        elif root.left is not None:
            if self.is_leaf(root.left):
                return root.left.val + self.sumOfLeftLeaves(root.right)
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.right)

    def is_leaf(self, node):
        return node.left is None and node.right is None
