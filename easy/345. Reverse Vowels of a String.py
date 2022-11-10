class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for word in s:
            if word in vowels_set:
                vowels.append(word)

        count = 1
        new_s = ""
        for word in s:
            if word in vowels_set:
                new_s += vowels[-count]
                count += 1
            else:
                new_s += word

        return new_s


sol = Solution()
c = sol.reverseVowels("leetcode")
print(c)
