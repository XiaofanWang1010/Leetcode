# 35. search insert position: binary search, next-smallest/largest element
# time complexity: O(logN) faster than linear search 
# space complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left 
                


# compare while(条件不成立时停止) and for(序列穷尽时停止):

for item in iterable:
    do something


while condition:
    do something 
