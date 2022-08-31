# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        sides = [root.val]
        layer_queue = [(0, root)]

        while len(layer_queue) > 0:
            (h, node) = layer_queue.pop(0)
            if node.left is not None:
                layer_queue.append((h + 1, node.left))
                if h + 1 < len(sides):
                    sides[h + 1] = node.left.val
                else:
                    sides.append(node.left.val)
            if node.right is not None:
                layer_queue.append((h + 1, node.right))
                if h + 1 < len(sides):
                    sides[h + 1] = node.left.val
                else:
                    sides.append(node.left.val)
        return sides

# this solution essentially do a breadth-first-traversal with labelled height for each visited node
# right traversal must come after left traversal as the tree is right-side-viewed
