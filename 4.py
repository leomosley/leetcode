class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) >= len(nums2):
            merged = nums1
            for i in nums2:
                merged.append(i)
        else:
            merged = nums2
            for i in nums1:
                merged.append(i)
                
        merged = sorted(merged)
        length = len(merged)
        
        if length % 2 != 0:
            median = merged[length//2]
        else:
            median = (merged[length//2] + merged[(length//2)-1]) * 0.5
            
        return float(median)
            