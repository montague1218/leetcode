class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n % 2 != 0:
                count += 1
            n = n >> 1
        return count

sol = Solution()
c = sol.hammingWeight(11)
print(c)