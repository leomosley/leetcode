class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        while n*n <= num:
            n += 1
        sqrt = n-1

        return sqrt ** 2 == num
        