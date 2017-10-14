class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = list(map(str, range(1, n+1)))
        for i in range(n):
            if int(nums[i])%15 == 0:
                nums[i] = "FizzBuzz"
            elif int(nums[i])%5 == 0:
                nums[i] = "Buzz"
            elif int(nums[i])%3 == 0:
                nums[i] = "Fizz"
        return nums