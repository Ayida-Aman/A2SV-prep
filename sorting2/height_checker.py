# problem link: https://leetcode.com/problems/height-checker/?envType=problem-list-v2&envId=array

class Solution(object):
    def heightChecker(self, heights):
        arr = heights[:]
        count = 0
        for i in range(1, len(heights)):
            j = i-1
            while j>=0:
                if heights[j+1] < heights[j]:
                    heights[j+1] , heights[j] = heights[j], heights[j+1]
                else:
                    break
                j-=1

        for i in range(len(heights)):
            if heights[i] != arr[i]:
                count+=1
        return count
        """
        :type heights: List[int]
        :rtype: int
        """
        