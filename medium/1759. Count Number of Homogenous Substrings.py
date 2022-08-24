class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        count_current = 1
        string_current = s[0]
        for i in range(len(s) - 1):
            if string_current == s[i + 1]:
                count_current += 1
            else:
                count += self.count_substring_of_homogeneous(count_current)
                count_current = 1
                string_current = s[i + 1]

        modulo = pow(10, 9) + 7
        count_all = count - 1 + self.count_substring_of_homogeneous(count_current)
        return count_all % modulo

    def count_substring_of_homogeneous(self, n):
        return (1 + n) * n // 2


sol = Solution()
c = sol.countHomogenous("abbcccaa")
print(c)
