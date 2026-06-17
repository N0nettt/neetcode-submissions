class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        maxLeft, maxRight = 0, height[len(height)-1]
        l, r = 0, len(height) - 1

        while l <= r:
            if maxLeft <= maxRight:
                res += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                res += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1
        
        return res
            
