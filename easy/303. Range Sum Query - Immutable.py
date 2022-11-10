class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumulator = []
        count = 0
        for n in nums:
            count += n
            self.cumulator.append(count)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.cumulator[right]
        return self.cumulator[right] - self.cumulator[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

sol = NumArray([-2, 0, 3, -5, 2, -1])
c = sol.sumRange(0, 5)
print(c)