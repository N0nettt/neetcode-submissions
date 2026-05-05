class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0

        for n in nums:
            res = n ^ res
        
        for i in range(len(nums)+1):
            res = res ^ i

        return res
            