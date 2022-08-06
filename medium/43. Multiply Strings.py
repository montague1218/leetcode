class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        t1, t2 = self.strToInt(num1), self.strToInt(num2)
        return str(t1 * t2)

    def strToInt(self, num):
        digitMap = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        digitPos1 = 1

        t = 0
        n = len(num)
        for i in range(n):
            d = num[n - i - 1]
            t += digitMap[d] * digitPos1
            digitPos1 *= 10
        return t


sol = Solution()
c = sol.multiply("13579", "24680")
print(c)
