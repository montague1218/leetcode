class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        complement = 0
        pow2 = 1
        while n > 0:
            digit = n % 2
            n //= 2
            if digit == 0:
                complement += pow2
            pow2 *= 2
        return complement

    def dyadic_encode(self, n):
        encode_str = ""
        count_two = 0
        while n > 0:
            if (n - 1) % 2 == 0:
                n = (n - 1) // 2
                encode_str += "1"
            elif (n - 2) % 2 == 0:
                n = (n - 2) // 2
                encode_str += "2"
                count_two += 1
            else:
                break

        return encode_str.replace("2", "10", count_two)

    def dyadic_invert(self, encode_str):
        complement = ""
        for s in encode_str:
            if s == "1":
                complement += "0"
            elif s == "0":
                complement += "1"
        return complement

    def dyadic_decode(self, encode_str):
        n = 0
        pow2 = 1
        for s in encode_str[::]:
            if s == "1":
                n += 1 * pow2
            elif s == "2":
                n += 2 * pow2
            pow2 *= 2
        return n


sol = Solution()
c = sol.bitwiseComplement(5)
print(c)
