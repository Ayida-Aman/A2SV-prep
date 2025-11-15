# problem link: https://leetcode.com/problems/sort-array-by-increasing-frequency/?envType=problem-list-v2&envId=array

class Solution(object):
    def frequencySort(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        for i in range(len(nums)):
            j=i
            while j>0:
                a, b = nums[j], nums[j-1]
                if freq[a] < freq[b]:
                    nums[j] , nums[j-1] = nums[j-1], nums[j]
                elif freq[a] == freq[b] and a>b:
                    nums[j] , nums[j-1] = nums[j-1], nums[j]
                j-=1
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        