# problem link : https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        l, res= 0, 0
        r = len(height) -1

        while l<r:
            area = min(height[l], height[r]) * (r-l)
            res = max(res, area)
            if(height[l] < height[r]):
                l+=1
            else:
                r-=1
        return res


        """
        :type height: List[int]
        :rtype: int
        """
        