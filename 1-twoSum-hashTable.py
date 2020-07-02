Python 3.8.4rc1 (v3.8.4rc1:6c38841c08, Jun 30 2020, 10:08:47) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
1. two for loops
# time complexity: O(n^2)
# space complexity: O(1) 
class Solution:
    def twoSum(self, nums, target): 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return i, j

2. create dict 
# time complexity: O(n)
# space complexity: O(n) 
用空间换取时间
字典是一种可变容器模型，可存储任意类型对象。

class Solution:
    def twoSum(self, nums, target): 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}     # 创建哈希表
        for i, num in enumerate(nums):   # enumerate列出索引i,元素num
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
        