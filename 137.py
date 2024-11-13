from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for n in count:
            if count[n] == 1:
                return n
        
        return -1
        