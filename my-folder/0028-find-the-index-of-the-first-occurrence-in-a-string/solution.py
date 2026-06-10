class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = i + len(needle)
        while j <= len(haystack):
            string = haystack[i:j]
            if string == needle:
                return i
            i += 1
            j += 1
        return -1

