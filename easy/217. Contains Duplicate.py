class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        counts = set()
        for n in nums:
            if n in counts:
                return True
            else:
                counts.add(n)
        return False