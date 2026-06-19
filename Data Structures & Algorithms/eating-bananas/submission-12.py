class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            mid = (l+r) // 2

            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            
            if total > h:
                l = mid + 1

            else:
                r = mid - 1
                res = min(res, mid)
        return res