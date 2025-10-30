# problem link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution(object):
    def longestSubarray(self, nums):
        res,l, zeroes = 0,0, 0
        k = 1
        if set(nums) == {1}:
            return len(nums) -1
        for r in range (len(nums)):
            if nums[r] != 1:
                zeroes +=1
            while zeroes > k:
                if nums[l] != 1:
                    zeroes-=1
                l+=1
            res = max(res, r-l+1)
        return res-1



        """
        :type nums: List[int]
        :rtype: int
        """
        