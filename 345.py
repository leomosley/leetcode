class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {"a", "e", "i", "o", "u"}  
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() not in vowels:
                l += 1
                continue

            if s[r].lower() not in vowels:
                r -= 1
                continue

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
