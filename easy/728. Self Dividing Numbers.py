class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for i in range(right - left + 1):
            n = left + i
            if self.number_is_self_dividing(n):
                nums.append(n)
        return nums

    def number_is_self_dividing(self, n):
        origin = n
        while n > 0:
            digit = n % 10
            if digit != 0 and origin % digit == 0:
                n //= 10
            else:
                return False
        return True


sol = Solution()
c = sol.selfDividingNumbers(47, 85)
print(c)

# this solution decompose each number to its digits, and check self-divideness
