class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        intA = 0
        intB = 0

        a = a[::-1]
        b = b[::-1]

        for i in range(len(a)):

            if a[i] == "1":
                intA += (2 ** i)
            
        for i in range(len(b)):

            if b[i] == "1":
                intB += (2 ** i)
        
        comb = intA + intB

        return bin(comb)[2:len(bin(comb))]