class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        n = len(digits)

        digits[-1] += 1

        for i in range(n):
            if carry:
                digits[n - 1 - i] += 1
                carry = False
            if (digits[n - 1 - i]) == 10:
                digits[n - 1 - i] = 0
                carry = True

        if not carry:
            return digits
        return [1] + digits

sol = Solution()
c = sol.plusOne([9,8,7,5])
print(c)
