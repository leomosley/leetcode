class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        s = n
        while s >= 10:
            s = sum(int(c) for c in str(s))
        return s
        