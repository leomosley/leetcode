class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_map = {char: s.count(char) for char in set(s)}

        for char in set(t):
            if char not in s_map:
                return char 
            elif s_map[char] < t.count(char):
                return char 
