class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """

        win, player = self.next_turn(n, 0)
        return (win and player == 0) or (not win and player == 1)

    def next_turn(self, n, player):
        divisors = self.get_divisors(n)

        if len(divisors) == 0:
            return False, player

        for divisor in divisors:
            other_win, _ = self.next_turn(n - divisor, 1 - player)
            if not other_win:
                return True, player
        return False, player

    def get_divisors(self, n):
        r = int(n ** (1 / 2))
        return [i for i in range(1, r + 1) if n % i == 0 and 0 < i < n]


sol = Solution()
c = sol.divisorGame(3)
print(c)

# this solution accepts a recursive tree structure that passes the winner at optimal at each node to the root
