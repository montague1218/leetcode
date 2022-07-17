class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelSet = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewelSet:
                count += 1
        return count


sol = Solution()
c = sol.numJewelsInStones('z', 'ZZ')
print(c)