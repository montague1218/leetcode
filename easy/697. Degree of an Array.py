class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        counter = dict()
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
            max_count = max(max_count, counter[n])

        max_frequency = [key for key in counter.keys() if counter[key] == max_count]

        min_sequence_length = len(nums)
        for key in max_frequency:
            left, right = -1, -1
            frequency = counter[key]
            for i, n in enumerate(nums):
                if n == key:
                    if left == -1:
                        left = i

                    frequency -= 1
                    if frequency == 0:
                        right = i
                        break
            min_sequence_length = min(min_sequence_length, right - left + 1)

        return min_sequence_length


sol = Solution()
c = sol.findShortestSubArray([1, 2])
print(c)

# this solution first prepare a hashtable counting the frequency for all integers in A,
# then for each integer k, we observe the answer is |S|, where S is the smallest subset of A containing all k in A.
