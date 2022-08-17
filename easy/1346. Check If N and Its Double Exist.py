class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        doubles = set()
        for n in arr:
            if n in doubles:
                return True

            doubles.add(n * 2)
            if n % 2 == 0:
                doubles.add(n // 2)

        return False


sol = Solution()
c = sol.checkIfExist([3,1,7,11])
print(c)
