class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenCount = 0
        oddCount = 1
        newNums = [0 for _ in range(len(nums))]
        for n in nums:
            if n % 2 == 0:
                newNums[evenCount] = n
                evenCount += 2
            else:
                newNums[oddCount] = n
                oddCount += 2
        return newNums

sol = Solution()
c = sol.sortArrayByParityII([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
print(c)

# this solution separately records the evens and odds by two separatly in-place counters
