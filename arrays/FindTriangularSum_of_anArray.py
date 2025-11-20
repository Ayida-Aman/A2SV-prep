# problem link: https://leetcode.com/problems/find-triangular-sum-of-an-array/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def triangularSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        while len(nums) != 1:
            i=0
            newNums = []
            while i < len(nums)-1:
                newNums.append((nums[i] + nums[i+1])% 10)
                i+=1
            nums = newNums
        return nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        