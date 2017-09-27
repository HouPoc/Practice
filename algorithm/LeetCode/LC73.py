class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        for x in range(h):
            for y in range(w):
                if matrix[x][y] == 0:
                    for j in range(h):
                        if matrix[j][y] != 0:
                            matrix[j][y] = 'a'
                    for k in range(w):
                        if matrix[x][k] != 0:
                            matrix[x][k] = 'a'

        for x in range(h):
            for y in range(w):
                if matrix[x][y] == 'a':
                    matrix[x][y] = 0