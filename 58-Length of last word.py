# 58.Length of Last Word
# time complexity: O(n)
# space complexity: O(n)

# str.isspace(): this function determines if the str contains only spaces
# str.split(delimiter): this function could split the input string into several substrings

class Solution:
    def LengthOfLastWord(self, s: str) -> int:
        return 0 if not s or s.isspace() else len(s.split()[-1])
    
