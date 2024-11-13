class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        
        for i, num in enumerate(nums):
            c = target - num
            if c in hashmap:
                return [hashmap[c], i]
            hashmap[num] = i

        return []   
        