class Solution:
    def search(self, nums: List[int], target: int) -> int:
        position = 0
        while position < len(nums):
            if nums[position] == target:
                return position
            position += 1
        return -1