class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        while abs(n) > 1:
            if n % 2 == 0:
                n //= 2
            else:
                return False
        return True


sol = Solution()
c = sol.isPowerOfTwo(1024-1)
print(c)
