class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z = x ^ y
        count = 0
        while z > 0:
            if z % 2 != 0:
                count += 1
            z = z >> 1
        return count


sol = Solution()
c = sol.hammingDistance(3, 1)
print(c)

# this solution makes use of shift operators XOR, bit shift to measure respectively hamming distance (in terms of
# number of bits) and the actual hamming distance

