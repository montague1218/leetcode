class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, A, low, high):
        # ensure indices are in correct order
        if low >= high or low < 0:
            return None

        p = self.partition(A, low, high)

        # sort the two partitions
        self.quicksort(A, low, p - 1)
        self.quicksort(A, p + 1, high)

    def partition(self, A, low, high):
        pivot = A[high]
        i = low - 1

        for u in range(high - low):
            j = low + u
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]

        i += 1
        A[i], A[high] = A[high], A[i]

        return i


sol = Solution()
c = sol.sortArray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1])
print(c)

# this solution is essentially a quick sort
