# problem link: https://leetcode.com/problems/kth-missing-positive-number/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def findKthPositive(self, arr, k):
        missing = 0
        current =1
        arr_set = set(arr)

        while True:
            if current not in arr_set:
                missing+=1
                if missing == k:
                    return current
            current +=1 
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        