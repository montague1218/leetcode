class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        distance = [n for _ in range(n)]
        pos_char = [i for i in range(n) if s[i] == c]

        for p in pos_char:
            distance[p] = 0

            # spread pos to the left from the string base
            for i in range(p - 1, -1, -1):
                if s[i] != c and distance[i] > p - i:
                    distance[i] = p - i
                else:
                    break

            # spread pos to the right from the string base
            for i in range(p + 1, n, 1):
                if s[i] != c and distance[i] > i - p:
                    distance[i] = i - p
                else:
                    break

        return distance


sol = Solution()
c = sol.shortestToChar("loveleetcode", "e")
print(c)

# this solution searches positions of characters that matched the input target (c),
# then spread from each matched characters to left/right and spread the relative distances from the base.
# There should be an optimized approach as some spreads are duplicated, and they are symmetric

