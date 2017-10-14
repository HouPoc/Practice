class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index in range(len(nums)):
            if nums[index] in dic:
                return [dic[nums[index]],index]
            else:
                dic[target-nums[index]] = index

