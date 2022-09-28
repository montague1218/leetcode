class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


class Trie(object):
    def __init__(self, strings):
        self.root = Node(False)

        for s in strings:
            self.insert(self.root, s)

    def insert(self, node, s):
        if len(s) == 0:
            node.key_node = True
        else:
            c, tail = s[0], s[1:]
            if node.children[c] is not None:
                self.insert(node.children[c], tail)
            else:
                self.add_new_branch(node, s)

    def add_new_branch(self, node, s):
        if len(s) == 0:
            node.key_node = True
        else:
            c, tail = s[0], s[1:]
            node.children[c] = Node(False)
            self.add_new_branch(node.children[c], tail)

    def find_longest_prefix(self, node, s, prefix):


class Node(object):
    def __init__(self, stores_key):
        self.key_node = stores_key
        self.children = {}

        for i in range(26):
            char = chr(ord('a') + i)
            self.children[char] = None
