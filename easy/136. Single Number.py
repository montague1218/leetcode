class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for n in nums:
            xor ^= n
        return xor


sol = Solution()
c = sol.singleNumber([4, 1, 2, 1, 2])
print(c)

# given that xor has the operator "^", A^B := xor(A, B) := xor(Am|Am-1|...|A1|A0, Bm|Bm-1|...|B1|B0)
# := [xor(Am, Bm)|...|xor(A0, B0)]

# Hence xor([n0, ... , nk]) gives the required answer
