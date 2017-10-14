class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = format(x, 'b').zfill(31)
        b = format(y, 'b').zfill(31)
        count = 0
        for m,n in zip(a,b):
            if m!=n:
                count = count + 1
        return count 