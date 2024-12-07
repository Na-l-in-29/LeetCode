class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v = len(nums)
        for i in range(v):
            for j in range(i + 1, v):
                if nums[i] + nums[j] == target:
                    return i, j