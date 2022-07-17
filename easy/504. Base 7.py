class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num > 0):
            return self.convertPositiveToBase7(num)
        elif (num < 0):
            n7 = self.convertPositiveToBase7(-num)
            return '-' + n7

        return '0'

    def convertPositiveToBase7(self, num):
        reversedDigits = []
        while num > 0:
            digit = num % 7
            num //= 7
            reversedDigits.append(str(digit))
        reversedDigits.reverse()
        return ''.join(reversedDigits)


sol = Solution()
c = sol.convertToBase7(-100)
print(c)
