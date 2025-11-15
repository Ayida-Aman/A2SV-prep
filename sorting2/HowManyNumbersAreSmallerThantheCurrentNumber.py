# problem link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# attempt 1 (brute force)

# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         result=[0] * len(nums)
#         for i in range (len(nums)):
#             for j in range(len(nums)):
#                 if nums[j] < nums[i]:
#                     result[i]+=1
#         return result

#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
# attempt 2 (insertion sort)

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = nums[:]
        for i in range(len(result)):
            j=i
            while j>0 and result[j] < result[j-1]:
                result[j] , result[j-1] = result[j-1], result[j]
                j-=1
        hashMap = {}
        for i, num in enumerate (result):
            if num not in hashMap:
                hashMap[num] = i
        
        return [hashMap[num] for num in nums]

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        