class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        memo = {}
        memo[(len(prices), True)] = 0

        def dfs(i, buying):
            if (i, buying) in memo:
                return memo[(i, buying)]
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
                
            else:
                sell = dfs(i+2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            return memo[(i, buying)]

        return dfs(0, True)