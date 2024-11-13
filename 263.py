class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        for k in 2, 3, 5:
            while n % k == 0 < n:
                n = n / k
        
        return n == 1