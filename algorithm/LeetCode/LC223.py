class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        Width = min(G, C) - max(A ,E)
        Height = min(D, H) - max(B, F)
        if Width < 0 or Height < 0:
            return (C - A) * (D - B) + (G - E)*(H - F)
        else:
            return (C - A) * (D - B) + (G - E)*(H - F) - Height * Width