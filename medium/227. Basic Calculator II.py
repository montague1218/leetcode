class TokenLiteral(object):
    def __init__(self, tokenType, literal):
        self.tokenType = tokenType
        self.literal = literal

    def __str__(self):
        return "(%s, %s)" % (self.tokenType, self.literal)


class Lexer(object):
    def __init__(self, input):
        self.input = input
        self.currentPosition = 0
        self.readPosition = 1
        self.tokens = []

    def tokenize(self):
        while self.peekChar() is not None:
            self.readToken()

    def readToken(self):
        token = self.readChar()
        if token is not None:
            self.tokens.append(token)

    def readChar(self):
        char = self.input[self.currentPosition]
        if char.isdigit():
            if self.peekChar() is not None and self.peekChar().isdigit():
                int_literal = self.readInt()
                token = TokenLiteral("INT", int(int_literal))
            else:
                token = TokenLiteral("INT", int(char))
        elif char == "+":
            token = TokenLiteral("OPERATOR", char)
        elif char == "-":
            token = TokenLiteral("OPERATOR", char)
        elif char == "*":
            token = TokenLiteral("OPERATOR", char)
        elif char == "/":
            token = TokenLiteral("OPERATOR", char)
        else:
            token = None

        self.nextChar()

        return token

    def nextChar(self):
        if self.currentPosition == len(self.input):
            self.currentPosition += 1
            self.readPosition += 1
            return None
        if self.readPosition >= len(self.input):
            return None

        nextChar = self.input[self.readPosition]

        self.currentPosition += 1
        self.readPosition += 1

        return nextChar

    def peekChar(self):
        if self.readPosition >= len(self.input):
            return None
        return self.input[self.readPosition]

    def readInt(self):
        current = "%s" % self.input[self.currentPosition]
        while True:
            if self.peekChar() is not None and self.peekChar().isdigit():
                nextChar = self.nextChar()
                current += nextChar
            else:
                break
        return current


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.operators = {"+", "-", "*", "/"}

    def evaluate(self):
        evalutedTokens = self.evaluateByOperatorType({"*", "/"}, self.tokens)
        evalutedTokens = self.evaluateByOperatorType({"+", "-"}, evalutedTokens)

        if len(evalutedTokens) == 1:
            return evalutedTokens[0].literal
        return None

    def evaluateByOperatorType(self, operators, tokens):
        i, evaluatedTokens = 1, [tokens[0]]
        while i < len(tokens):
            if tokens[i].tokenType == "OPERATOR" and tokens[i].literal in operators:
                if evaluatedTokens[-1].tokenType == "INT":
                    result = self.evalutaePair(tokens[i], evaluatedTokens[-1], tokens[i + 1])
                    evaluatedTokens[-1] = result
                    i += 2
                else:
                    evaluatedTokens.append(tokens[i])
                    i += 1
            else:
                evaluatedTokens.append(tokens[i])
                i += 1
        return evaluatedTokens

    def evalutaePair(self, operator, left, right):
        if operator.tokenType == "OPERATOR" and left.tokenType == right.tokenType == "INT":
            if operator.literal == "*":
                return TokenLiteral("INT", left.literal * right.literal)
            elif operator.literal == "/":
                return TokenLiteral("INT", left.literal // right.literal)
            elif operator.literal == "+":
                return TokenLiteral("INT", left.literal + right.literal)
            elif operator.literal == "-":
                return TokenLiteral("INT", left.literal - right.literal)
        return None


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += " "
        lexer = Lexer(s)
        lexer.tokenize()

        parser = Parser(lexer.tokens)
        result = parser.evaluate()

        return result

    def calculate_test(self, s):
        s += " "
        lexer = Lexer(s)
        lexer.tokenize()

        parser = Parser(lexer.tokens)
        result = parser.evaluate()

        return result, lexer, parser


tests = [
    ("1-2-3", 1 - 2 - 3),
    ("30/2*4", 30 // 2 * 4),
    ("1-2*3", 1 - 2 * 3),
    ("1+12", 1 + 12),
    ("1+2*3", 1 + 2 * 3),
    ("1+2*3+4", 1 + 2 * 3 + 4),
    ("1+2*3+4*5", 1 + 2 * 3 + 4 * 5),
    ("1-1+1", 1 - 1 + 1),
    ("1*2", 1 * 2),
    ("1*2*3", 1 * 2 * 3),
    ("1*2*3*4", 1 * 2 * 3 * 4),
    ("1*2*3*4*5", 1 * 2 * 3 * 4 * 5),
    ("11*12*13", 11 * 12 * 13),
    ("11*12*1", 11 * 12 * 1),
    ("51*1*2*3*4*49", 51 * 1 * 2 * 3 * 4 * 49),
]

sol = Solution()

for (input, expected) in tests:
    result, lexer, parser = sol.calculate_test(input)
    print("input='%s', expected=%d, got=%s" % (input, expected, result))
    if expected != result:
        for token in parser.tokens:
            print(token)

# this solution implements a lexer and parser to calculate elementary arithmetic expressions
# it's my first lexer and parser!!!! (although quite slow compared in leetcode)
