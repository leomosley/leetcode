class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        line = [1]
        n = rowIndex

        # using this identity:
        # C(n,k+1) = C(n,k) * (n-k) / (k+1)
        
        for k in range(n):
            line.append(line[k] * (n-k) / (k+1))
        
        return line