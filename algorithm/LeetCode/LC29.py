class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        elif dividend == 0:
            return 0
        else:
            a_d = abs(dividend)
            a_s = abs(divisor)
            num = 0
            while a_d >= a_s:
                temp, i = a_s, 1
                while (a_d >= temp):
                    a_d -= temp
                    num += i
                    i <<= 1 
                    temp <<= 1
                    
            if (dividend < 0) is not (divisor < 0):
                num = -num
            return min(max(-2147483648, num), 2147483647)    
