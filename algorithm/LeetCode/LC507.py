from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        upper = int(sqrt(num))
        s = 0
        for i in range(2, upper + 1):
            if num % i == 0:
                s += (i + num / i)
        s = s + 1
        if s == num:
            return True
        else:
            return False
