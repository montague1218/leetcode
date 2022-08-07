class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        regionSets = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]

                if val == ".":
                    continue

                if self.checkSetHasValue(rowSets[i], val):
                    return False
                if self.checkSetHasValue(colSets[j], val):
                    return False

                region = 3 * (i // 3) + (j // 3)  # region number is counted row by col
                if self.checkSetHasValue(regionSets[region], val):
                    return False

        return True

    def checkSetHasValue(self, hashset, val):
        if val in hashset:
            return True
        else:
            hashset.add(val)
            return False


sol = Solution()

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
c = sol.isValidSudoku(board)
print(c)

# this solution uses 9+9+9 hashsets, each 9 for rows, columns and regions
