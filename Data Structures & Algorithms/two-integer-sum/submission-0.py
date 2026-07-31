class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        acc_i = 0
        acc_j = 0
        for i in nums:
            acc_j = acc_i + 1
            for j in nums[acc_j:]:
                if i + j == target:
                    return [acc_i, acc_j]
                acc_j = acc_j + 1
            acc_i = acc_i + 1

        return []