class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        brackets_map = { ')': '(', '}' : '{', ']' : '['}

        for char in s:
            if char in brackets_map:
                if (len(stack) == 0 or stack[-1] != brackets_map[char]):
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0