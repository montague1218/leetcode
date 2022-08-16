class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = dict()
        pos = dict()
        keys = []
        for (i, char) in enumerate(s):
            if char not in counts:
                counts[char] = 0
                pos[char] = i
                keys.append(char)
            counts[char] += 1

        for key in keys:
            if counts[key] == 1:
                return pos[key]
        return -1


sol = Solution()
c = sol.firstUniqChar("loveleetcode")
print(c)

# this solution counts the frequency, first-position, and relative of each unique character of the string
