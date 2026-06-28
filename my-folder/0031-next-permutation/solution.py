class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0:
            if nums[i-1] < nums[i]:
                r = len(nums)-1
                while r >= 0 and nums[r] <= nums[i-1]:
                    r -= 1
                nums[i-1], nums[r] = nums[r], nums[i-1]
                l, r = i, len(nums)-1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                return nums
            i -= 1
        
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

        nums[i:] = reversed(nums[i:])
        
