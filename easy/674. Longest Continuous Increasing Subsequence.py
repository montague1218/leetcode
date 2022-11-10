class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        max_length = 0
        counter = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                counter += 1
            else:
                max_length = max(max_length, counter)
                counter = 1

        if nums[-2] < nums[-1]:
            max_length = max(max_length, counter)

        return max_length