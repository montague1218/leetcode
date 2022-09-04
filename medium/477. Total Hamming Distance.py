class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cache = {}
        n = len(nums)
        i, j = 0, 0
        while i < n:
            while j < n:
                if i != j:
                    n1, n2 = nums[i], nums[j]
                    if (i, j) not in cache:
                        hamming_distance = self.hammingDistance(n1, n2)

                        cache[(i, j)] = cache[(j, i)] = hamming_distance
                        total += hamming_distance
                    else:
                        total += cache[(i, j)]
                j += 1
            i += 1
            j = i
        return total

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z = x ^ y
        count = 0
        while z > 0:
            if z % 2 != 0:
                count += 1
            z = z >> 1
        return count


sol = Solution()
c = sol.totalHammingDistance([4, 14, 2])
print(c)

# this solution assumes hamming distance of a pair of integers is calculated as in #462.
# iterator of all the pairs is a graph walk of the upper-triangular matrix representing the location indices
