class Solution(object):
    def searchInsert(self, nums, target):
        
        start = 0
        end = len(nums)-1
        found = None
        
        while start <= end:
            i = (start + end) // 2
            if nums[i] == target:
                found = i
                break
            elif target < nums[i]:
                end = i - 1
            else:
                start = i + 1
        
        if not found:
            found = start
        return found
        