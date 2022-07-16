class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True

        direction = self.getDirection(nums[0], nums[1])
        monotoneDirection = None

        for i in range(len(nums) - 2):
            nextDirection = self.getDirection(nums[i + 1], nums[i + 2])
            if (direction <= 0 and nextDirection <= 0) or (direction >= 0 and nextDirection >= 0):
                direction = nextDirection
                if direction != 0:
                    if monotoneDirection is None:
                        monotoneDirection = direction
                    elif monotoneDirection != direction:
                        return False
                continue
            return False
        return True

    def getDirection(self, a, b):
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0


sol = Solution()
c = sol.isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5])
print(c)
0,0,-1,1,1