import sys

def answer(total_lambs):
    # base case 1:
    #   total_lambs = 1 or 2
    if total_lambs <= 3:
        return 0
    # generous conditon:
    print ('g')
    g = generous_call (1, 2, total_lambs-3)    
    # stingy condition:
    print ('s')
    s = stingy_call (1, 1, total_lambs-2)
    return s-g

def generous_call(last_last, last, avaliable_lambs):
    # base cases
    print(last)
    if avaliable_lambs < (last_last+last):
        return 0
    if avaliable_lambs < (2*last):
        return 1
    last_last = last
    last = 2* last
    avaliable_lambs -= last
    return generous_call(last_last, last, avaliable_lambs)+1
        
def stingy_call(last_last, last, avaliable_lambs):
    # base cases
    print(last)
    if avaliable_lambs < (last_last+last):
        return 0
    # recursive case
    avaliable_lambs -= (last+last_last)
    t = last
    last = last_last + last
    last_last = t
    return stingy_call(last_last, last, avaliable_lambs)+1
	
def main():
    number = 143
    test_answer = answer(number)
    print (test_answer)

if __name__ == "__main__":
    main()
    

