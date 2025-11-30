# problem link: https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        numString = [str(num) for num in nums]
        for i in range(1, len(nums)):
            j = i
            while j>0 and numString[j] + numString[j-1] > numString[j-1] +numString[j]:
                numString[j-1], numString[j] = numString[j], numString[j-1]
                j-=1
        if numString[0] == "0":
            return "0"
        else:
            return "".join(numString)

        """
        :type nums: List[int]
        :rtype: str
        """
        