class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r = 0,x
        while l < r:
            mid = (l+r) / 2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l-1 if l>1 else l