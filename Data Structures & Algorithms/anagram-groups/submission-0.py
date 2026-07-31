class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for word in strs:
            letters = "".join(sorted(word))
            if letters not in out:
                out[letters] = [word]
            else:
                out[letters].append(word)

        return list(out.values())
