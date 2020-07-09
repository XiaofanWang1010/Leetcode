class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:       
        if not strs: 
            return ""
        min_s = min(strs)  # the smallest item
        max_s = max(strs)
        if not min_s: 
            return ""
        for i in range(len(min_s)):  # interately access each item by index
            if max_s[i] != min_s[i]:
                return max_s[:i]    # char from index 0 to i-1
        return min_s[:]  # note: correspond to for-loop
