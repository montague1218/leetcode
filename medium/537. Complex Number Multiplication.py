class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a, b = self.complexStringToNumber(num1)
        c, d = self.complexStringToNumber(num2)

        u = a * c - b * d
        v = b * c + a * d

        return "%s+%si" % (u, v)

    def complexStringToNumber(self, c):
        a, b = c.split("+")
        return int(a), int(b[:-1])

sol = Solution()
c = sol.complexNumberMultiply("1+2i","3+4i")
print(c)
