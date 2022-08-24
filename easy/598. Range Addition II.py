class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        x, y = m, n
        for op in ops:
            x, y = min(x, op[0]), min(y, op[1])
        return x * y


sol = Solution()
c = sol.maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])
print(c)

# this solution observes the result (no. of maximum int) is equivalent to the area of the
# smallest rectangles contained among all input rectangles.
# Such smallest element always exists, since (0, 0) must always be contained.
