# 70. Climbing stairs 
# Fibonacci Number: Fib(n) = Fib(n-1) + Fib(n-2)
# time complexity: O(n)
# space complexity: O(1) 

class Solution:
    def climbStairs(self, n:int) -> int:
        if n==0 or n==1 or n==2: return n
        else:
            s,s1,s2=0,1,2
            for i in range(2,n):
                s=s1+s2
                s1=s2
                s2=s
            return s
