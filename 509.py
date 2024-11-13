class Solution(object):
    def fib(self, n):
        
        if n < 2:
            return n
        
        return Solution().fib(n-1) + Solution().fib(n-2)