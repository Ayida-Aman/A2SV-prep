# problem link: https://leetcode.com/problems/rotate-array/submissions/

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %=n
        new_n = n-k
        nums[:]= nums[new_n:n] + nums[0:new_n]

        def reverse(start, end):
            while start<end:
                nums[start], nums[end] = nums[end] , nums[start]
                start +=1
                end -=1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        