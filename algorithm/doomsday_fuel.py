from fractions import *

def solution(matrix):
    # State_chain
    state_chain = []
    # Find the denominator for each row
    sum_per_state = dict()
    # Find terminate state index
    terminate_state_probability = dict()
    row_count = 0
    for row in matrix:
        row_sum = sum(row)
        sum_per_state[row_count] = row_sum
        if row_sum == 0:
            terminate_state_probability[row_count] = [0,1]
        row_count += 1
    # Calculate the probalities of each terminate state
    # temp probalities
    calculate_probability(matrix,sum_per_state,terminate_state_probability, 0, state_chain, [1,1])
    result = standard_answer(terminate_state_probability)
    return result
    
    
def calculate_probability(matrix, sum_per_state, terminate_state_probability, row_index, state_chain, temp_p):
    state = matrix[row_index]
    element_index = 0
    previous_numerator = temp_p[0]
    previous_denominator = temp_p[1]
    for element in state:
        if element != 0:
            if element_index in state_chain:
                #print ("find a cycle")
                # initial involved variables
                del state_chain[:]
            else:
                state_chain.append(row_index)
                numerator = previous_numerator * element
                denominator = previous_denominator * sum_per_state[row_index]
                numerator_now = Fraction(numerator, denominator).numerator
                denominator_now = Fraction(numerator, denominator).denominator
                #print ('row: {row}, element: {element}'.format(row = row_index, element = element_index))
                #print [previous_numerator, previous_denominator]
                if sum_per_state[element_index] == 0:
                    numerator = terminate_state_probability[element_index][0]
                    denominator = terminate_state_probability[element_index][1]
                    numerator_new = denominator_now * numerator + denominator * numerator_now
                    denominator_new = denominator_now * denominator
                    result = Fraction(numerator_new, denominator_new)
                    terminate_state_probability[element_index] = [result.numerator, result.denominator]
                    # empty the state chain
                    del state_chain[:]
                else:
                    calculate_probability(matrix, sum_per_state, terminate_state_probability, element_index, state_chain,[numerator_now, denominator_now])
        element_index += 1           
            
def standard_answer(probability_dic):
    dic_len = len(probability_dic)
    result_array = []
    number_list = []
    for key, value in probability_dic.iteritems():
        number_list.append(value[1])
    n = len(number_list)  
    while n != 1:
        number = number_list.pop()
        number_list[0] = number * number_list[0] / gcd (number_list[0],number)
        #print number_list[0]
        n = len(number_list)
    LCM = number_list[0]
    sum = 0
    for key, value in probability_dic.iteritems():
        numerator = value[0]*LCM/value[1]
        sum += numerator
        result_array.append(numerator)
    result_array.append(sum)
    return result_array

def main ():
    #010001, 400320
    #matrix = [[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    matrix = [[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    result = solution(matrix)
    print result

if __name__ == "__main__":
    main()
