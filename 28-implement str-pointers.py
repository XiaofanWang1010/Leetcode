class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        for i in range(n-L+1):
            if haystack[i:i+L] == needle:
                return i
        return -1
