# problem link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return i+1, j+1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        