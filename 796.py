class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        def rotate(s1, k):
            s2 = s1[0:-k]
            s1 = s1[-k:]

            for i in s2:
                s1 += i
    
            return s1
        
        n = 1
        while rotate(s, n) != goal and n < len(s):
            n += 1
        
        return rotate(s, n) == goal