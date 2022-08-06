class Solution(object):
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

        # modify the result in-place, stored in nums1
        for i in range(m + n):
            nums1[i] = merged_nums[i]

        # for print purpose
        return nums1


sol = Solution()
c = sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(c)

# this solution is a typical merge for two sorted arrays
