class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) ==0: return 0
        j = 0  # slower pointer, only move when meet unique number 
        for i in range(1, len(nums)):  # faster pointer, interate over all elements
            if nums[i] != nums[i-1]:   # when nums[i] is a unique number, assign it to nums[j]
                j += 1
                nums[j] = nums[i]
        return j+1
