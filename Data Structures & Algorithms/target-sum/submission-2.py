class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {0: 1}

        for num in nums:
            newDp = {}
            for d in dp:
                newDp[d+num] = newDp.get(d+num, 0) + dp[d]
                newDp[d-num] = newDp.get(d-num, 0) + dp[d]
            dp = newDp

        return dp.get(target, 0)