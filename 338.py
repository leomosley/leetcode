class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = []

        for i in range(n+1):

            binary = bin(i)
            ans.append(binary.count("1"))
        
        return ans