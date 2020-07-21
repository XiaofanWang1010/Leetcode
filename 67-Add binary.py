# 67. Add Binary
# time complexity: O(N+M)

class Solution:
    def addBinary(self, a:str, b:str) -> str:
        return '{0:b}'.format(int(a, 2)+int(b,2))

# Convert a and b into integers
# compute the sum
# convert the sum back into binary form.

    
