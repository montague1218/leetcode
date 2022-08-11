class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        p1, p2, p3 = 0, 1, 1
        for i in range(n - 2):
            current = p1 + p2 + p3
            p1, p2, p3 = p2, p3, current
        return current

sol = Solution()
c = sol.tribonacci(5)
print(c)

