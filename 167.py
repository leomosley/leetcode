class Solution(object):
    def twoSum(self, numbers, target):
        
        d = {}
        for i, n in enumerate(numbers):
            m = target - n
            if m in d:
                return [d[m]+1, i+1]
            else:
                d[n] = i