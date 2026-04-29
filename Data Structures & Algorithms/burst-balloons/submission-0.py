class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        dp[(1, 1)] = 0

        def dfs(nums):
            if tuple(nums) in dp:
                return dp[tuple(nums)]

            maxCoins = 0
            for i in range(1, len(nums)-1):
                coins = nums[i-1] * nums[i] * nums[i+1]
                coins += dfs(nums[:i] + nums[i + 1:])
                maxCoins = max(maxCoins, coins)
            dp[tuple(nums)] = maxCoins
            return dp[tuple(nums)]
        
        return dfs(nums)
        
            

        