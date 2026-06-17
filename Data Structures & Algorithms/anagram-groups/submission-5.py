class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('z')] += 1

            d[tuple(key)].append(s)

        res = []
        for k, v in d.items():
            res.append(v)

        return res