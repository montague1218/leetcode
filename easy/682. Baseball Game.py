class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        for op in ops:
            if op[0] == "-":
                if op[1].isdigit():
                    scores.append(int(op))
            if op.isdigit():
                scores.append(int(op))
            elif op == "C":
                scores.pop(-1)
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                pass
        return sum(scores)

# can optimize?

# class Solution(object):
#     def calPoints(self, ops):
#         """
#         :type ops: List[str]
#         :rtype: int
#         """
#         backup_previous = None
#         previous_1, previous_2 = None, None
#         last_cancel_pos = 0
#
#         for i in range(len(ops)):
#             print(ops, ops[i], last_cancel_pos)
#             if ops[i] == "C":
#                 ops[last_cancel_pos], ops[i] = 0, 0
#                 last_cancel_pos -= 1
#                 previous_1, previous_2 = backup_previous, previous_1
#             else:
#                 if ops[i].isdigit():
#                     ops[i] = int(ops[i])
#                 elif ops[i][0] == "-":
#                     ops[i] = int(ops[i])
#                 elif ops[i] == "D":
#                     ops[i] = previous_2 * 2
#                 elif ops[i] == "+":
#                     ops[i] = previous_2 + previous_1
#                 last_cancel_pos = i
#                 backup_previous = previous_1
#                 previous_1, previous_2 = previous_2, ops[i]
#
#         return sum(ops)


sol = Solution()
c = sol.calPoints(
    ["8373", "C", "9034", "-17523", "D", "1492", "7558", "-5022", "C", "C", "+", "+", "-16000", "C", "+", "-18694", "C",
     "C", "C", "-19377", "D", "-25250", "20356", "C", "-1769", "-8303", "C", "-25332", "29884", "C", "+", "C", "-29875",
     "-15374", "C", "+", "14584", "13773", "+", "17037", "-28248", "+", "16822", "D", "+", "+", "-19357", "-26593",
     "-8548", "4776", "D", "-8244", "378", "+", "-19269", "-25447", "18922", "-16782", "2886", "C", "-17788", "D",
     "-22256", "C", "308", "-9185", "-19074", "1528", "28424", "D", "8658", "C", "7221", "-13704", "8995", "-21650",
     "22567", "-29560", "D", "-9807", "25632", "6817", "28654", "D", "-18574", "C", "D", "20103", "7875", "C", "9911",
     "23951", "C", "D", "C", "+", "18219", "-20922", "D", "-24923"])
print(c)

# this is essentially a parser
