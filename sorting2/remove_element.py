# problem link: https://leetcode.com/problems/remove-element/?envType=problem-list-v2&envId=array

# first attempt (index out of range)

# class Solution(object):
#     def removeElement(self, nums, val):

#         for i in range (len(nums)) :
#             if nums[i] == val:
#                 del nums[i]
#                 i-=1

#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
        
# second attempt (accepted) beats 100%

class Solution(object):
    def removeElement(self, nums, val):

        for i in range (len(nums)) :
            if nums[i] == val:
                del nums[i]
                i-=1

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        