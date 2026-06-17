class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums))] 
        d = Counter(nums)

        print(d)
        for key, value in d.items():
            freq[value-1].append(key)

        res = []
        print(freq)
        for i in range(len(freq)-1, -1, -1):
            if k == 0:
                break
            
            for n in freq[i]:
                if k == 0:
                    break
                res.append(n)
                k -= 1
        
        return res
