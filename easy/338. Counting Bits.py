class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        bits = [0 for _ in range(n + 1)]
        bits[0:3] = [0, 1, 1]

        pow2 = 1
        for i in range(n - 1):
            p = i + 2
            if p == pow2 * 2:
                bits[p] = 1
                pow2 *= 2
            else:
                bits[p] = bits[p - pow2] + bits[pow2]

        return bits


sol = Solution()
c = sol.countBits(7)
print(c)
