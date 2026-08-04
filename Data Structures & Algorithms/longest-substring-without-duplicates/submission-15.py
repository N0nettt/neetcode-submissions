class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setic = set()
        length = 0

        l, r = 0, 0

        for r in range(len(s)):
            while s[r] in setic:
                setic.remove(s[l])
                l += 1

            setic.add(s[r])
            length = max(length, r-l+1)

        return length