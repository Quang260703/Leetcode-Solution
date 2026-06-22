class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0) or (x == 1):
            return x

        low = 0
        high = x
        ans = 0

        while low <= high:
            multi_base = (low + high) // 2
            multi_result = multi_base * multi_base

            if (multi_result > x):
                high = multi_base - 1
            elif (multi_result == x):
                return multi_base
            else:
                ans = multi_base
                low = multi_base + 1

        return ans
