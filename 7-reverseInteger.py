# 7. Reverse Integer
# time complexity: O(n)
class Solution:
    def reverse(self, x:int) -> int:
        if x>=0:
            re = int(str(x)[::-1])
        else:
            re = -1*int(str(-x)[::-1])
        if re < -2**31 or re > 2**31-1:
            return 0
        return re
    
