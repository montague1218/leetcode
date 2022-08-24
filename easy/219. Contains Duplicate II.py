class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False

        group = dict()
        for (i, n) in enumerate(nums):
            if n not in group:
                group[n] = i
            else:
                if i - group[n][-1] <= k:
                    return True
                group[n] = i
        return False


sol = Solution()
c = sol.containsNearbyDuplicate([1, 2, 3, 1], 3)
print(c)

# this solution group the numbers by their value and compare it to the last indices within the group
