# problem link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def countHillValley(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        hill, valley = 0, 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                hill +=1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                valley +=1
        return hill+valley
        """
        :type nums: List[int]
        :rtype: int
        """
        