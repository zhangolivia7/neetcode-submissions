from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # store indices
        d = deque()
        n = len(nums)
        maxes = []

        for r in range(n):
            # remove indices from front if out of window
            if d and d[0] <= r - k:
                d.popleft()

            # remove indices from back if less than or equal to curr num
            while d and nums[d[-1]] <= nums[r]:
                d.pop()

            # add curr index as new candidate
            d.append(r)

            if r >= k - 1:
                maxes.append(nums[d[0]])
        
        return maxes