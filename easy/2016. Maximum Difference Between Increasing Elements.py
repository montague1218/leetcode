class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = False
        difference = 0
        min_num, max_num = nums[0], nums[0]
        for n in nums:
            if n >= max_num:
                max_num = n
                if max_num - min_num > difference:
                    difference = max_num - min_num
                    exist = True
            elif n < min_num:
                min_num, max_num = n, n

        if not exist:
            return -1
        return difference


sol = Solution()
c = sol.maximumDifference([9,4,3,2])
print(c)

# this solution is isomorphic to Q.121
