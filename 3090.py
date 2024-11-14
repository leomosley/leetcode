class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        l = 0
        s_map = {}

        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1

            while any(count > 2 for count in s_map.values()):
                s_map[s[l]] -= 1
                if s_map[s[l]] == 0:
                    del s_map[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)
        
        return max_length
