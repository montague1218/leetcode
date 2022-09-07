class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = nums[0], None, None
        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n < max1:
                if max2 is None:
                    max2 = n
                elif n > max2:
                    max2, max3 = n, max2
                elif n < max2:
                    if max3 is None:
                        max3 = n
                    elif n > max3:
                        max3 = n

        if max3 is None:
            return max1
        return max3


sol = Solution()
c = sol.thirdMax([1, 1, 2])
print(c)

# this solution finds the third maximum by 3 maxima shifting when intermediate value is found
