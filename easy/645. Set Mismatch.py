class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counters = dict()

        for i in nums:
            if i not in counters:
                counters[i] = 1
            else:
                counters[i] += 1

        duplicate_num = -1
        missing_num = -1
        for i in range(n):
            if i + 1 not in counters:
                missing_num = i + 1
            elif counters[i + 1] == 2:
                duplicate_num = i + 1

        return [duplicate_num, missing_num]


sol = Solution()
c = sol.findErrorNums([1, 2, 2, 4])
print(c)

# this solution simply applies a hash-counter structure.
