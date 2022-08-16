# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        none_left, none_right = left is None, right is None
        if none_left and not none_right:
            return False
        elif not none_left and none_right:
            return False
        elif none_left and none_right:
            return True
        elif self.is_leaf(left) and self.is_leaf(right):
            return left.val == right.val

        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left) and left.val == right.val

    def is_leaf(self, node):
        return node.left is None and node.right is None

# this solution do comparison on two pairs of subtrees (L.R,R.L)/(L.L,R.R)
# each iteration first null-checks the pair of two nodes, and then branches out if they both contain subtrees

