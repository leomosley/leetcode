class Solution(object):
    def fizzBuzz(self, n):
        
        res = []
        for i in range(1, n+1):
            temp = ""
            if i % 3 == 0:
                temp += "Fizz"

            if i % 5 == 0:
                temp += "Buzz"
            
                
            if temp != "":
                res.append(temp)
            else:
                res.append(str(i))

        return res
        