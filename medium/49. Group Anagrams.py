class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = {}

        for str in strs:
            char_set, char_table = self.get_anagram(str)
            anagram_base_str = self.get_anagram_base_string(char_table)

            if anagram_base_str not in anagram_dict:
                anagram_dict[anagram_base_str] = []
            anagram_dict[anagram_base_str].append(str)

        return list(anagram_dict.values())

    def get_anagram(self, str):
        char_set = set()
        char_table = self.get_char_table()

        for s in str:
            char_set.add(s)
            char_table[s] += 1
        return char_set, char_table

    def get_char_table(self):
        char_dict = {}
        for i in range(ord('a'), ord('z') + 1):
            char_dict[chr(i)] = 0
        return char_dict

    def get_anagram_base_string(self, char_table):
        anagram_base_str = ""
        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if char_table[char] > 0:
                anagram_base_str += "%s%d" % (char, char_table[char])
        return anagram_base_str

sol = Solution()
c = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(c)

# this is a solution (slow approach) that take advantages of the isomorphic property of anagrams
# and associate a UID for each anagram with its ordered alphabet values (like a1b12d4h5)
# grouping and filtering are done on the basis of this OAV
