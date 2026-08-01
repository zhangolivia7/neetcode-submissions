class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash table
        # num: frequency of that number
        # after looping through nums, sort hash table in reverse, loop through k elements of the hash table
        freqs = {}

        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1
        
        sorted_freqs = list(sorted(freqs.items(), key=lambda item: item[1], reverse=True))

        ret = []
        for i in range(k):
            ret.append(sorted_freqs[i][0])

        return ret