class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        shortestString = strs[0]
        for s in strs:
            if len(s) < len(shortestString):
                shortestString = s

        prefixLength = len(shortestString)
        while prefixLength > 0:
            for s in strs:
                if s[prefixLength - 1] != shortestString[prefixLength - 1]:
                    prefixLength //= 2
                    break
            
        print(prefixLength)
        return shortestString


sol = Solution()
c = sol.longestCommonPrefix(['flowers', 'flow', 'flo'])
print(c)