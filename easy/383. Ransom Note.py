class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False

        counter = dict()
        for s in magazine:
            if s not in counter:
                counter[s] = 1
            else:
                counter[s] += 1

        for s in ransomNote:
            if s not in counter:
                return False
            counter[s] -= 1
            if counter[s] < 0:
                return False
        return True
