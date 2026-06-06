class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefix_len = len(prefix)
        
        for word in strs[1:]:
            while prefix != word[:prefix_len]:
                prefix_len -= 1
                prefix = prefix[:prefix_len]

                if prefix == '':
                    return prefix
        
        return prefix
