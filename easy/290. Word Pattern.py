class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words_pattern = self.getPattern(s, " ")
        pattern_pattern = self.getPattern(pattern, "")

        return words_pattern == pattern_pattern

    def getPattern(self, s, delimiter):
        if len(delimiter) == 0:
            words = s
        else:
            words = s.split(delimiter)

        words_index_map = {}
        words_index = 0
        words_pattern = ""

        for word in words:
            if word not in words_index_map:
                words_index_map[word] = words_index
                words_index += 1
            words_pattern += str(words_index_map[word])

        return words_pattern


sol = Solution()
c = sol.wordPattern("abba", "dog cat cat dog")
