class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        color_count = [0, 0, 0]
        for n in nums:
            color_count[n] += 1

        count = 0
        for i, color in enumerate(color_count):
            for j in range(color):
                nums[count] = i
                count += 1
        return nums


sol = Solution()
c = sol.sortColors([2, 0, 2, 1, 1, 0])
print(c)

# this solution requires a direct counting sort
