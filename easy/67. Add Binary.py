class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a

        n1 = len(a)
        n2 = len(b)
        c = ['0' for i in range(n1)]

        carry = '0'
        for i in range(n1):
            s1 = a[n1 - 1 - i]
            s2 = b[n2 - 1 - i] if n2 - 1 - i >= 0 else '0'

            bit, bitCarry = self.addBits(s1, s2)

            if bit == '0' and carry == '1':
                bit = '1'
            elif bit == '1' and carry == '1':
                bit = '0'
                bitCarry = '1'
            carry = bitCarry

            c[n1 - 1 - i] = bit
        if carry == '1':
            return '1' + ''.join(c)
        else:
            return ''.join(c)

    def addBits(self, a, b):
        if a == '0' and b == '0':
            return '0', '0'
        if a == '0' and b == '1':
            return '1', '0'
        elif a == '1' and b == '0':
            return '1', '0'
        elif a == '1' and b == '1':
            return '0', '1'
        else:
            return '', -1


sol = Solution()
c = sol.addBinary("110", "1010")
print(c)

# each pair of bits add itself, the carry produced is pushed to the next digit
# the carry for the current digit is added to the added bits
# note (carry+added_bits) <= 1, so no extra carry is produced
