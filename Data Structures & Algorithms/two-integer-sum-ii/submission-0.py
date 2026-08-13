class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        ret = [0, 0]

        while p1 != p2:
            s = numbers[p1] + numbers[p2]
            if s == target:
                ret[0] = p1 + 1
                ret[1] = p2 + 1
                return ret
            elif s < target:
                p1 += 1
            else:
                p2 -= 1

        return ret
        