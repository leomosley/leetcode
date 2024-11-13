from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = []
        nums1_map = Counter(nums1)
        nums2_map = Counter(nums2)

        for n in nums1_map.keys():
            if n in nums2_map:
                freq = min(nums2_map[n], nums1_map[n])

                for _ in range(freq):
                    res.append(n)

        return res