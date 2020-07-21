# 69. Sqrt(x)
# x: non-negative integer
# time complexity: O(1)
# space complexity: O(1) 

class Solution:
    def mySqrt(self, x:int) -> int:
        from math import e, log
        if x<2:
            return x
        left = int(e**(0.5*log(x)))
        right = left + 1
        return left if right*right>x else right

# x^(0.5) = e^(0.5*log(x))
# left < x^(0.5) < right 
