class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        reversedDigits = []
        while num > 0:
            digit = num % 2
            num //= 2
            reversedDigits.append(digit)

        pow2 = 1
        complement = 0
        for d in reversedDigits:
            complement += (1 - d) * pow2
            pow2 *= 2

        return complement


sol = Solution()
c = sol.findComplement(2**31)
print(c)

# Derived by 504. Base7, which is to convert k into its n-ary representation
# Then calculate by complementary condition
