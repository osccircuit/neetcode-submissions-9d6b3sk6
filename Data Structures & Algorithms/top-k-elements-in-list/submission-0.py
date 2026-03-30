from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        for n, f in counts.items():
            freq[f].append(n)
        
        res = []
        for e in reversed(freq):
            for item in e:
                res.append(item)
                if len(res) == k:
                    return res