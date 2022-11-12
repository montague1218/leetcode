class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 2

        if n == 1:
            return a
        elif n == 2:
            return b

        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b


sol = Solution()
c = sol.climbStairs(3)
print(c)

# T(n) = (T[n - 1] + 1) + (T[n - 2] + 1) - T[2] = T[n - 1] + T[n - 2] + 2 - 2 = a + b.
# we consider "jumping" to T(n) from T(n-1), T(n-2) without intermediate steps, so we subtract by T(2)

# or simply, since the algorithm counts on the uniqueness of paths, the path leading to T[n]
# has uniquely two ways to reach from T[n - 1] and T[n - 2], so T[n] = T[n - 1] + T[n - 2]
