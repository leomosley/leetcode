class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total = 0
        for i in stones:
            if i in jewels:
                total += 1
        return total