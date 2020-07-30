# time complexity: O((n+m)log(n+m))
# space complexity: O(1)

class Solution:
    def merge(self,nums1:List[int], m:int, nums2:List[int], n:int) ->None:
        nums1[:] = sorted(nums1[:m]+nums2)
        # constraints:
        # nums1.length == m+n
        # nums2.length == n

        # merge both lists into one and then to sort
