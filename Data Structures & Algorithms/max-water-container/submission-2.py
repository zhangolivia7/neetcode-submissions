class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_area = (j - i) * (min(heights[i], heights[j]))

        while j > i:
            area = (j - i) * (min(heights[i], heights[j]))
            if area > max_area:
                max_area = area

            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        
        return max_area

        
        
