class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max = ""

        if s == s[::-1]:
            return s

        for i in range(len(s)):
            for j in range(1,len(s)+1):
                
                temp = s[i:j]

                if len(temp) > len(max) and temp == temp[::-1]:
                    max = temp
        
        return max