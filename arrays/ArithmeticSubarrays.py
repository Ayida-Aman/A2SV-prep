# problem link: https://leetcode.com/problems/arithmetic-subarrays/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        query = [True] * len(l)
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            temp = nums[left:right+1]
            sortedTemp = sorted(temp)
            diff = sortedTemp[1] - sortedTemp[0]
            for j in range(1, len(sortedTemp)):
                if sortedTemp[j] - sortedTemp[j-1] != diff:
                    query[i] = False
                    break

        return query
            
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        