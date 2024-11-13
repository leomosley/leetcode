class Solution(object):
    def largeGroupPositions(self, s):
        
        i   = 0
        arr = []
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if (j - i) > 2:
                arr.append([i, j - 1])
            i = j
            
        return arr