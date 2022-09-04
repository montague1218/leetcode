# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        left_height, left_balanced = self.getHeight(root.left)
        right_height, right_balanced = self.getHeight(root.right)
        return left_balanced and right_balanced and abs(left_height - right_height) <= 1

    def getHeight(self, node):
        if node is None:
            return 0, True
        elif self.is_leaf(node):
            return 1, True
        left_height, left_balanced = self.getHeight(node.left)
        right_height, right_balanced = self.getHeight(node.right)

        self_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, self_balanced

    def is_leaf(self, node):
        return node.left is None and node.right is None

# this solution observes that a pair of information (height, balanced) is required to carry by each node up to the root
# and subtrees' heights & balances are compared at each level
