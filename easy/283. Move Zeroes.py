class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        zero_count = 0

        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = n

        for i in range(zero_count):
            nums[len(nums) - zero_count + i] = 0

        return nums


sol = Solution()
c = sol.moveZeroes([0, 1, 0, 3, 12, 0, 0, 0, 1, 2, 3, 0, 1, 2])
print(c)

# this solution counts the number of zeros, while pushing ahead the non-zero elements
# and put back the zeros after a loop of the array
