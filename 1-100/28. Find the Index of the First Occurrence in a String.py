class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        i = 0
        while i < len(haystack):
            if haystack[i:needle_len] == needle:
                return i
            
            i += 1
            needle_len += 1

        return -1


a = Solution()
print(a.strStr('sadbutsad', 'sad')) #0
print(a.strStr('leetcode', 'leeto')) #-1