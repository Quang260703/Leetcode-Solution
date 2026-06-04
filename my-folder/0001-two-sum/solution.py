class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        dic[nums[0]] = 0
        for i in range(1,len(nums)):
            find = target - nums[i]
            if find in dic:
                return [i, dic[find]]
            else:
                dic[nums[i]] = i
            
