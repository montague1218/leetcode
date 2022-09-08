class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        occurrences = {}

        for n in nums:
            if n not in occurrences:
                occurrences[n] = 0
            occurrences[n] += 1

            if n - 1 in occurrences:
                max_length = max(max_length, occurrences[n] + occurrences[n - 1])
            if n + 1 in occurrences:
                max_length = max(max_length, occurrences[n] + occurrences[n + 1])

        return max_length


sol = Solution()
c = sol.findLHS([1,3,2,2,5,2,3,7])
print(c)

# observes the subsequence only counts the number of occurrence, so sorting is not needed
# the question also defined a neighbourhood for each appearing integer (n, n + 1) or (n, n - 1)
# occurrence can be "grown" dynamically for each neighbourhood. Keeping the max_value should suffice.
