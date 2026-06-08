class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while True:
            if nums[i] >= target:
                return i
            if nums[j] < target:
                return j + 1
            elif nums[j] == target:
                return j
            i += 1
            j -= 1
            
