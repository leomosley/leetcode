class Solution(object):
    def containsDuplicate(self, nums):
        
        arr = []
        
        for i in nums:
            if i in arr:
                return True
            arr.append(i)
        
        return False