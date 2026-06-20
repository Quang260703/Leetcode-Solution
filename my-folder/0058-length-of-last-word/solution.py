class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = ""
        s = s[::-1]
        for i in s:
            if i == " " and len(s1) == 0:
                continue
            if i == " ":
                break
            s1 += i
        return len(s1)
