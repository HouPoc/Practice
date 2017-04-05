

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last = 0
    now = 0
    for element in nums:
        old = now 
        now = max(now, last+element)
        last = old
        print [last, now]
    return now
        
def main ():
   
    nums = [1,8,10,6,9,3,4,7,2,5]
    result = rob(nums)
    print result
    #print result

if __name__ == "__main__":
    main()