class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, amount):
            if (i, amount) in dp:
                return dp[(i, amount)]
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            
            not_take = dfs(i+1, amount)
            take = 0
            if amount >= coins[i]:
                take = dfs(i, amount-coins[i])

            dp[(i, amount)] = not_take + take
            return dp[(i, amount)]

        return dfs(0, amount)