class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        x = str(x)[::-1]
        if x[-1] == "-":
            x = "-"+x[:len(x)-1]
        if x[0] == "0":
            x = x[1:]
        if int(x) < (-2**31)  or int(x) > (2**31 - 1):
            return 0
        return int(x)
