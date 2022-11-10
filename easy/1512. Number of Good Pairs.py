class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = dict()
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        pair_count = 0
        for key in counter.keys():
            n = counter[key] - 1
            pair_count += (n + 1) * n // 2

        return pair_count


sol = Solution()
c = sol.numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(c)

# this solution counts the frequency of each integer in nums,
# and observes the pair has a partial quadratic sum
