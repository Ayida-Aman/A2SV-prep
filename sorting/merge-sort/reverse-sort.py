# problem link https://leetcode.com/problems/reverse-pairs/description/


# this one is a brute force solution but u will get TLE

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[j] *2
                if x < nums[i]:
                    count +=1

        return count