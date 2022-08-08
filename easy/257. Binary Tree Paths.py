# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        if root.left is None and root.right is None:
            return [str(root.val)]

        if root.left is not None:
            left_paths = self.addRootToPaths(root.val, self.binaryTreePaths(root.left))
        else:
            left_paths = []

        if root.right is not None:
            right_paths = self.addRootToPaths(root.val, self.binaryTreePaths(root.right))
        else:
            right_paths = []

        return left_paths + right_paths

    def addRootToPaths(self, val, paths):
        return ["%s->%s" % (val, path) if path != "" else "%s" % val for path in paths]

# this solution branches by left/right subtrees, and the recursion terminates once both subtrees are empty,
# which returns an array containing the node's value ready for path extension with its parent
