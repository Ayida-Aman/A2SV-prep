# problem link https://leetcode.com/problems/sort-an-array/

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid: len(nums)])

        return self.merge(left, right)
    def merge(self, left, right):
        i =0
        j=0
        results = []
        while i<len(left) and j < len(right):
            if left[i] < right[j]: 
                results.append(left[i])  
                i += 1
            else:
                results.append(right[j])
                j += 1

        results.extend(left[i:])
        results.extend(right[j:])
        return results