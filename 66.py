class Solution(object):
    def plusOne(self, digits):
        
        s = ""
        for i in digits:
            s += str(i)
        n = str(int(s) + 1)
        return [i for i in n]
        