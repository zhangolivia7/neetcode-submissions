class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # set window to max, use a dictionary for t one for s
        # keep track of valid window if one exists and the length
        # loop through t and see if key at i exists and value at i matches, if not, return the last valid window. if yes, keep looping

        if not s or not t or len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        formed = 0
        required = len(need)

        best_len = float('inf')
        best_left = 0

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1
        
        if best_len == float('inf'):
            return ""
        return s[best_left:best_left + best_len]

        
