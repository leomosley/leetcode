class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1

            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1

        for char in s_map:
            if char not in t_map or s_map[char] != t_map[char]:
                return False
        
        return True
