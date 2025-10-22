# problem link: https://leetcode.com/problems/rotate-array/submissions/

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %=n
        new_n = n-k
        nums[:]= nums[new_n:n] + nums[0:new_n]


        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        