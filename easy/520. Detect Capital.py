class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        countBig = 0
        countSmall = 0
        firstIsBig = word[0].isupper()

        for s in word:
            if s.islower():
                countSmall += 1
            else:
                countBig += 1

        if len(word) == countSmall or len(word) == countBig:
            return True
        elif firstIsBig and (countBig == 1 and countSmall == len(word) - 1):
            return True
        return False

sol = Solution()
c = sol.detectCapitalUse('')
print(c)