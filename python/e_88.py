class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointer solution for merging sorted
        i = m - 1 # end of nums1
        j = n - 1 # end of nums2
        k = m + n - 1 # end of final
        
        while j >= 0: # stop once were done with nums2
            if i >= 0 and nums1[i] > nums2[j]: # put the bigger number in nums1 going left
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
