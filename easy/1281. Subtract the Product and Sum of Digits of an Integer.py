class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, s = 1, 0
        while n > 0:
            d = n % 10
            n //= 10

            p *= d
            s += d
        return p - s


sol = Solution()
c = sol.subtractProductAndSum(4421)
print(c)
