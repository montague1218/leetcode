class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_current, count_max = 1, 1
        string_current = s[0]
        for i in range(len(s) - 1):
            if string_current == s[i + 1]:
                count_current += 1
            else:
                count_max = max(count_max, count_current)
                count_current = 1
                string_current = s[i + 1]
        return max(count_max, count_current)


sol = Solution()
c = sol.maxPower("abbcccddddeeeeedcba")
print(c)

# this solution bases on 485. Max Consecutive Ones, with different initialization and conditionals
