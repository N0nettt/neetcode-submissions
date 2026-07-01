class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        f1 = [0] * 26
        f2 = [0] * 26

        for i in range(len(s1)):
            f1[ord(s1[i]) - ord('a')] += 1
            f2[ord(s2[i]) - ord('a')] += 1

        if f1 == f2:
            return True

        l, r = 1, len(s1)

        while r < len(s2):
            print(f"{s2[l]}, {s2[r]}")
            f2[ord(s2[r]) - ord('a')] += 1
            f2[ord(s2[l-1]) - ord('a')] -= 1

            if f1 == f2:
                return True

            l += 1
            r += 1

        return False

        