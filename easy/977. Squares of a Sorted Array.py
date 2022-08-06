class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negatives = []
        nonnegatives = []
        for n in nums:
            if n < 0:
                negatives.append(n ** 2)
            else:
                nonnegatives.append(n ** 2)
        negatives = negatives[::-1]

        mergedNums = self.merge(negatives, len(negatives), nonnegatives, len(nonnegatives))
        return mergedNums

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        c1, c2 = 0, 0
        merged_nums = [0 for _ in range(m + n)]

        while c1 < m or c2 < n:
            if c1 >= m:
                merged_nums[i] = nums2[c2]
                c2 += 1
            elif c2 >= n:
                merged_nums[i] = nums1[c1]
                c1 += 1
            else:
                if nums1[c1] <= nums2[c2]:
                    merged_nums[i] = nums1[c1]
                    c1 += 1
                else:
                    merged_nums[i] = nums2[c2]
                    c2 += 1
            i += 1

        return merged_nums


sol = Solution()
c = sol.sortedSquares([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
print(c)

# this solution separates the negatives and non-negatives
# then use merge for their respective squares
