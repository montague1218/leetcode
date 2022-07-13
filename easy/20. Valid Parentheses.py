class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        if n % 2 != 0: return False
        if self.isRight(s[0]): return False

        stack = []
        pointer = -1
        for r in s:
            if self.isLeft(r):
                stack.append(r)
                pointer += 1

            if self.isRight(r):
                if pointer == -1: return False
                if self.matchParenthese(stack[pointer], r):
                    stack.pop()
                    pointer -= 1
                else:
                    return False

        if pointer > 0: return False
        return True

    def isLeft(self, a):
        return a == '(' or a == '[' or a == '{'

    def isRight(self, a):
        return a == ')' or a == ']' or a == '}'

    def matchParenthese(self, a, b):
        return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')


sol = Solution()
c = sol.isValid('([]){}{()}')
print(c)