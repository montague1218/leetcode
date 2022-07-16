class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numSet = set()
        indices = {}
        compliments = {}
        for (i, n) in enumerate(nums):
            numSet.add(n)
            indices[n] = i
            compliments[n] = target - n
        for n in nums:
            if compliments[n] in numSet and n != compliments[n]:
                return [indices[n], indices[compliments[n]]]
        return [-1, -1]

