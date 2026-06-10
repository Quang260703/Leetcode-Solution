class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maximum = 0
        while i < j:
            new_maximum = min(height[i],height[j])*(j-i)
            if new_maximum > maximum:
                maximum = new_maximum
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maximum
