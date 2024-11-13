class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        arr = [i for i in str(x) if i != "-"]
        arr = arr[::-1]
        
        if str(x)[0] == "-":
            s = "-"
        else:
            s=""
        
        for i in arr:
            s+=i
        
        r = int(s)
        
        if r > (2**31)-1 or r < -2**31:
            return 0
        else:
            return r
        