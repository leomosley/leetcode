class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        count = 0
        for i in range(len(s)-1):
            if hashmap[s[i]] < hashmap[s[i+1]]:
                count -= hashmap[s[i]]
            else:
                count += hashmap[s[i]]
        
        count += hashmap[s[-1]]
        
        return count
            