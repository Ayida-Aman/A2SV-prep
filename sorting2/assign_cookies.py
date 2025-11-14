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
        
# attempt 2 (sorted the array manually which is not very efficient i just want to practice sorting)

class Solution(object):
    def findContentChildren(self, g, s):

        for i in range (len(g)):
            j = i
            while j>0 and g[j] < g[j-1]:
                g[j-1], g[j] = g[j] , g[j-1]
                j-=1
                
        for i in range (len(s)):
            j = i
            while j>0 and s[j] < s[j-1]:
                s[j-1], s[j] = s[j] , s[j-1]
                j-=1

        i, j = 0, 0
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                i+=1
            j+=1
        return i

        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        

