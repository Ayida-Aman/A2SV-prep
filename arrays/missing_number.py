# problem link: https://leetcode.com/problems/missing-number/submissions/1827640985/?envType=problem-list-v2&envId=sorting

#  first attempt (not efficient)

# class Solution(object):
#     def missingNumber(self, nums):  
#         # for i in range(len(nums)+1):              O(n)
#             # if i not in nums:                       O(n)
#                 return i

#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        

# second attempt (accepted) .. Beats 100% 😎

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

        """
        :type nums: List[int]
        :rtype: int
        """
        