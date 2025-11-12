# problem link: https://leetcode.com/problems/intersection-of-two-arrays/?envType=problem-list-v2&envId=sorting

# first attempt (brute force) 

# class Solution(object):
#     def intersection(self, nums1, nums2):
#         result = []

#         for i, num1 in enumerate(nums1):
#             for j , num2 in enumerate(nums2):
#                 if num1 == num2:
#                     result.append(num1)
#                     result.append(num2)
#         unique_num = set(result)
#         return list(unique_num)
    
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
        

# second attempt (hashmap) accepted ... Beats 5% 🫢

# class Solution(object):
#     def intersection(self, nums1, nums2):
#         unique_nums1 = set(nums1)
#         unique_nums2 = set(nums2)
#         result = []
#         for num2 in (list(unique_nums2)):
#             if num2 in unique_nums1:
#                 result.append(num2)
#         return result

#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
        

# 3rd attempt (cool one line using set) accepted ... Beats 100%

class Solution(object):
    def intersection(self, nums1, nums2):
        return list (set(nums1) & set(nums2))

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        