class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            amountOfWater = min(heights[l], heights[r])  * distance
            res = max(res, amountOfWater)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res