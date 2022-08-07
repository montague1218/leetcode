class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = []
        while num > 0:
            d = num % 10
            digits.append(d)

            num //= 10

        romans = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"],
        ]

        romanLiteral = []
        for i, d in enumerate(digits):
            r = self.mapDigitToRoman(romans, d, i)
            romanLiteral.append(r)

        return "".join(romanLiteral[::-1])

    def mapDigitToRoman(self, romans, digit, digitPos):
        return romans[digitPos][digit]


sol = Solution()
c = sol.intToRoman(3994)
print(c)

# this solution accepts each digit in the input,
# and return a roman literal mapped by the digit value and the digit's position
