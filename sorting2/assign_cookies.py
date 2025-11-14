# problem link: https://leetcode.com/problems/assign-cookies/submissions/1829549164/?envType=problem-list-v2&envId=sorting

# attempt 1 (accepted)

class Solution(object):
    def findContentChildren(self, g, s):

        sortedG = sorted(g, reverse=True)
        sortedS = sorted(s, reverse=True)
        i, j, count = 0,0, 0
        while i<len(g) and j<len(s):
            if sortedS[j] < sortedG[i]:
                i+=1
            else:
                count +=1
                i+=1
                j+=1
        return count

        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
# 