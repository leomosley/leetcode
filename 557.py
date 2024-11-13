class Solution(object):
    def reverseWords(self, s):
        
        string = ""; s = s.split()
        for i in range(len(s)):
            string += s[i][::-1] + " "
        return string[:(len(string)-1)]
        