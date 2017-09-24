from fractions import *
import operator as op
from itertools import product

def answer(m):
    #Input Matrix Dimension
    IMD = len(m)
    if IMD == 1:
        return [1,1]
    #Probability Matrix
    PM=[]
    for state in m:
        if sum(state) != 0:
            PM.append(list(map(lambda x: Fraction(x, sum(state)), state)))
        else:
            PM.append(list(map(lambda x: Fraction(0), state)))
    #Absorbing State Probability Matrix
    ASPM = []
    #Non Absorbing State Probability Matrix
    NASPM = []
    #Initial NASPM and ASPM
    for state_index in xrange(len(PM)):
        if sum(m[state_index]) != 0:
            #Locate the Non Absorbing State Probability Array
            NASPA = PM[state_index]
            NASPM_row = []
            ASPM_row = []
            for NASPA_index in xrange(len(NASPA)):
                if sum(m[NASPA_index]) != 0:
                    NASPM_row.append(NASPA[NASPA_index])
                else:
                    ASPM_row.append(NASPA[NASPA_index])
            ASPM.append(ASPM_row)
            NASPM.append(NASPM_row)
    #Create the Non Absorbing State Porbability Transit Matrix
    I = identity_matrix(len(NASPM))
    NASPTM = []
    for index in xrange(len(I)):
        NASPTM.append(map(op.sub,I[index],NASPM[index]))
    #Inverse Matrix of NASPTM
    NASPTM_Inverse = invert_matrix(NASPTM)
    #Final Probability Array
    FPA = matrix_multiplication(NASPTM_Inverse, ASPM)
    #print FPA
    return standard_answer(FPA[0])
    
    
            
            
def identity_matrix(dimention):
    matrix = []
    for i in range(dimention):
        row = [Fraction(0)]*dimention
        row[i] = Fraction(1)
        matrix.append(row)
    return matrix  

def invert_matrix(matrix):
    dimention = len(matrix)
    inverse_matrix = [[Fraction(0) for col in range(dimention)] for row in range(dimention)]

    for i in xrange(dimention):
        inverse_matrix[i][i] = Fraction(1)

    for i in xrange(dimention):
        for j in xrange(dimention):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(dimention):
                    inverse_matrix[j][k] = inverse_matrix[j][k] - ratio * inverse_matrix[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in xrange(dimention):
        a = matrix[i][i]
        for j in range(dimention):
            inverse_matrix[i][j] = inverse_matrix[i][j] / a

    return inverse_matrix    

def matrix_multiplication(matrix_left, matrix_right):
    rows = len(matrix_right)
    if rows is 0:
        return 0
    cols = len(matrix_right[0])
    resRows = range(len(matrix_left))
    rMatrix = [[0] * cols for _ in resRows]

    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matrix_left[idx][k] * matrix_right[k][j]
    return rMatrix
 
def standard_answer(FPA):
    denominator_list = map(lambda x: x.denominator, FPA)
    numerator_list = map(lambda x: x.numerator, FPA)
    n = len(denominator_list)
    while len(denominator_list) != 1:
        number_0 = denominator_list[0]
        number = denominator_list.pop()
        denominator_list[0] = number * number_0 / gcd(number_0, number)
    LCM = denominator_list[0]
    denominator_list = map(lambda x: x.denominator, FPA)
    result = []
    for val in zip(numerator_list, denominator_list):
        result.append(val[0] * LCM / val[1])
    result.append(LCM)
    return result
    
    
def main ():
    #010001, 400320
    matrix = [[0,2,1,0,0],[0,0,0,4,3],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #matrix = [[0,1,1],[0,0,0],[1,1,0]]
    result = answer(matrix)
    print result
    #print result

if __name__ == "__main__":
    main()