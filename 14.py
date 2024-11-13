class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strings = sorted(strs)
        first = strings[0]
        last = strings[-1]
        
        longest = ""
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return longest
            longest += first[i]
        
        return longest