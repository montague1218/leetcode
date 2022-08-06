class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = []
        odds = []
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds

sol = Solution()
c = sol.sortArrayByParity([1,2,3,4,5,6,7,8,9,10,0, -1])
print(c)

# this solution separately records the evens and odds, then combine both
