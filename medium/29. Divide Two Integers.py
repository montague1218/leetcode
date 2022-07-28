class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == 0:
            return 0

        positive, d1, d2 = True, dividend, divisor
        if dividend < 0 and divisor < 0:
            d1 = -d1
            d2 = -d2
        elif dividend < 0 or divisor < 0:
            positive = False
            if d1 < 0:
                d1 = -d1
            if d2 < 0:
                d2 = -d2

        quotient, remainder = self.dividePositive(d1, d2)

        if not positive:
            quotient = -quotient

        maxint = 2147483648
        if quotient > maxint - 1:
            return maxint - 1
        elif quotient < -maxint:
            return -maxint
        return quotient

    def dividePositive(self, dividend, divisor):
        quotient = 0
        while dividend >= divisor:
            accumulator = 1
            accumulatedDivisor = divisor
            while dividend >= accumulatedDivisor:
                dividend -= accumulatedDivisor
                quotient += accumulator
                accumulator += 1
                accumulatedDivisor += divisor
        return quotient, dividend


sol = Solution()
c = sol.divide(-2 ** 32, -1)
print(c)

# multiplication/division is fundamentally an aggregate of addition/subtraction
# the subtraction process can be sped up by accumulating the subtracted value
