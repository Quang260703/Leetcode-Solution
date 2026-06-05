class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        sets = {}
        for i in range(len(s)):
            if s[i] in sets:
                left = max(sets[s[i]] + 1, left)
            sets[s[i]] = i
            max_len = max(max_len, i - left + 1)
        return max_len
