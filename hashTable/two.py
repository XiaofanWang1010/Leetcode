Python 3.8.4rc1 (v3.8.4rc1:6c38841c08, Jun 30 2020, 10:08:47) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1: Brute force
        # Space: O(1)
        # Time: O(N^2)
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i >= j: continue
                if n1 + n2 == target:
                    return [i, j]