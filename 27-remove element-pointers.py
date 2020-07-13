class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0   # faster pointer
        for i in range(len(nums)):  # slower pointer
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
