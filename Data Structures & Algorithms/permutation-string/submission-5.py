class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        n = len(s2)
        letters = sorted(s1)
        # print(letters)

        for i in range(n - window_size + 1):
            window = s2[i:i+window_size]
            sorted_window = sorted(window)
            # print(sorted_window)

            if sorted_window == letters:
                return True

        return False