class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if n == 1:
            return s

        z = [""] * n
        n -= 1

        for i in range(len(s)):
            z[abs((i + n) % (2 * n) - n)] += s[i]
        return "".join(z)