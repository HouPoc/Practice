class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = low + (high - low)/2
        while high >= low:
           #result = guess (target)
           if guess(mid) == 0:
               break
           elif guess(mid) == 1:
               low = mid + 1
               mid = low + (high - low)/2
           else:
               high = mid - 1
               mid = low + (high - low)/2
        return mid